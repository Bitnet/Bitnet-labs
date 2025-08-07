!/bin/bash

# Simple Bash Port Scanner - v2
# Author: bitnet-labs

target=$1
start_port=$2
end_port=$3
timeout_value=1

if [ -z "$target" ] || [ -z "$start_port" ] || [ -z "$end_port" ]; then
  echo "Usage: $0 <target> <start_port> <end_port>"
  echo "Example: $0 hackthebox.com 20 100"
  exit 1
fi

echo "[*] Scanning $target ports $start_port to $end_port ..."
echo

open_ports=0

for ((port=$start_port; port<=$end_port; port++)); do
  timeout $timeout_value bash -c "echo > /dev/tcp/$target/$port" 2>/dev/null &&
  { echo "[+] Port $port is open"; ((open_ports++)); }
done

echo
echo "[*] Scan completed. $open_ports open ports found."
