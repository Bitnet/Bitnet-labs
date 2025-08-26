import socket
import sys

def scan(host, start_port, end_port):
    print(f"[*] Scanning {host} ports {start_port}-{end_port}")
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")
        finally:
            s.close()
    print("[*] Scan completed.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: python3 {sys.argv[0]} <host> <start_port> <end_port>")
        sys.exit(1)

    target = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])

    scan(target, start, end)
