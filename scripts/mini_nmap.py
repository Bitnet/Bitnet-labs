#!/usr/bin/env python3
import socket
import argparse

def scan_port(ip, port):
    """Try to connect to a specific port"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
        return True
    except:
        return False
    finally:
        sock.close()

def main():
    parser = argparse.ArgumentParser(description="Mini Nmap - Simple Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", help="Port range to scan (default 1-1024)", default="1-1024")
    args = parser.parse_args()

    # Parse port range
    start_port, end_port = map(int, args.ports.split("-"))

    print(f"[+] Scanning {args.target} from port {start_port} to {end_port}...")

    for port in range(start_port, end_port + 1):
        if scan_port(args.target, port):
            print(f"[OPEN] Port {port} is open")

if __name__ == "__main__":
    main()
