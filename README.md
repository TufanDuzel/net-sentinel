# 🛡️ Net-Sentinel: Automated Security Analysis Suite

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)

**Net-Sentinel** is a full-stack cybersecurity application designed to automate complex network reconnaissance and data interception tasks. By bridging the gap between low-level network tools and high-level user interfaces, it provides a unified platform for real-time security intelligence.

---

## 🔍 The Motivation

Modern security analysis often requires managing multiple terminal windows, which can be inefficient and error-prone. **Net-Sentinel** solves this by automating the workflow into a single, professional dashboard. 

The project demonstrates the risks associated with **unencrypted protocols** (HTTP, FTP, Telnet) and how easily sensitive data can be intercepted in an insecure network environment.

---

## 🏗️ System Architecture

Net-Sentinel is built on a modular **Three-Layer Architecture**:

1.  **Reconnaissance Layer:** Utilizes **Nmap** to identify active targets and perform deep service enumeration.
2.  **Attack & Interception Layer:** Automates **ARP Cache Poisoning** via **Bettercap** and executes **Deep Packet Inspection (DPI)** using **Scapy**.
3.  **Presentation Layer:** A web dashboard built with **Flask** and **Bootstrap 5** that visualizes background operations in real-time.

---

## 🔬 Experimental Results

Tests were performed in a controlled laboratory environment using **Virtual Machines** (Kali Linux and Metasploitable 2).

* **Discovery Speed:** Identified 15+ open ports in under 45 seconds.
* **Interception Accuracy:** 100% identification rate for unencrypted services.
* **Real-time Delivery:** Credentials appear on the dashboard within **2 seconds** of user action.

---

## ⚠️ Legal & Ethical Disclaimer

> **IMPORTANT:** This tool was developed for **educational and defensive purposes only**.

1.  **Authorized Testing:** Net-Sentinel should only be used on your own equipment or where you have written permission.
2.  **Scope Limitation:** The scanning and attack logic is restricted to the **local network segment**.
3.  **Liability:** The developer assumes no liability for any misuse or damage caused by this program.

---

## 👤 Author

**Tufan Şahin Düzel**
* **Department:** Computer Engineering
* **University:** International Balkan University
* **Portfolio:** [tufanduzel.com](https://tufanduzel.com)
* **LinkedIn:** [linkedin.com/in/tufanduzel](https://linkedin.com/in/tufanduzel)