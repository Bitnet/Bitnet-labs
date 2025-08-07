# Cheatsheet: tcpdump & Wireshark Basics for Red Teamers

Author: Bitnet-labs  
Phase: Fase 1  
Topic: Networking Basics & Packet Analysis  
---

## 📦 tcpdump – CLI Packet Sniffer

### 🔹 Capture packets on a specific interface
```bash
sudo tcpdump -i eth0
```

### 🔹 Capture only TCP packets to port 80 (HTTP)
```bash
sudo tcpdump -i eth0 tcp port 80
```

### 🔹 Capture DNS queries
```bash
sudo tcpdump -i eth0 port 53
```

### 🔹 Save captured traffic to a file
```bash
sudo tcpdump -i eth0 -w capture.pcap
```

### 🔹 Read a pcap file later
```bash
sudo tcpdump -r capture.pcap
```

---

## 🦈 Wireshark – GUI Packet Analyzer

### 🔹 Steps to use
1. Open with sudo:
   ```bash
   sudo wireshark
   ```
2. Select your interface (e.g., eth0)
3. Apply filters (example: `http`, `ip.addr == 10.0.2.15`)

### 🔹 Common display filters
| Filter               | Description                       |
|----------------------|-----------------------------------|
| `http`               | Show only HTTP traffic            |
| `ip.addr == x.x.x.x` | Filter by IP address              |
| `tcp.port == 80`     | Filter by TCP port                |
| `dns`                | Show DNS queries and responses    |

### 🔹 Follow TCP stream
- Right-click on a packet → **Follow → TCP Stream**
- Useful to inspect HTTP requests/responses or plaintext credentials

---

## 🎯 Practical Example

### 🧪 Test command in terminal:
```bash
curl http://hackthebox.com
```

### 👀 What you see in Wireshark:
- `GET / HTTP/1.1`
- Response: `HTTP/1.1 200 OK`
- Server headers (Cloudflare, content-type, etc.)
- Entire HTML page in plaintext (if not redirected or forced to HTTPS)

---

Red Team Tip: Packet captures are essential during:
- Credential sniffing (plaintext protocols)
- C2 detection/evasion
- Malware analysis
- Lateral movement over SMB, RPC, etc.

