#  Simple TCP Port Scanner

A lightweight and user-friendly TCP port scanner written in Python. This tool scans one or multiple ports on a target host, supports custom port ranges and shows banners (if available).

---

##  Features

*  Multi-port & port-range scanning
*  Banner grabbing (if service responds)
*  Adjustable timeout for responsiveness
---

## Installation

Clone the repository and install required dependencies:

```bash
git clone https://github.com/SaadAzil3/port_scan.git
cd port_scan
pip install -r requirements.txt
```

---

## Usage

```bash
python3 port_scanner.py <host> -p <port1> <port2>  ...
python3 port_scanner.py <host> -r <start_port> <end_port>
```
```bash
python3 port_scanner.py <host> -r <start_port> <end_port> -t <timeout>
```
### Examples

Scan specific ports:

```bash
python3 port_scanner.py 127.0.0.1 -p 22 80 443
```

Scan a range of ports:

```bash
python3 port_scanner.py example.com -r 1 1024
```

Customize timeout:

```bash
python3 port_scanner.py localhost -p 21 22 -t 0.5
```

---

## Arguments

| Argument          | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| `host`            | Target hostname or IP address (e.g., `127.0.0.1`, `example.com`) |
| `-p`, `--ports`   | One or more specific ports to scan (e.g., `-p 22 80 443`)        |
| `-r`, `--range`   | Range of ports to scan (e.g., `-r 1 1000`)                       |
| `-t`, `--timeout` | Connection timeout in seconds (default is 1.0)                   |

---

## ⚠️ Disclaimer

This tool is for **educational and authorized security testing** only.
Do **NOT** use it on systems you do not own or have permission to test.
Unauthorized use is **illegal** and **unethical**.

---
