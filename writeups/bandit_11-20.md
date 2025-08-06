# OverTheWire: Bandit (Levels 11→20)

**Author:** YOUR NAME  
**Repository:** [bitnet-labs](https://github.com/YOUR-USER/bitnet-labs)  
**Objective:** Learn file encoding/decoding, compression handling, string manipulation, and SSH private key usage.

---

## 🔹 Level 11 → 12
Goal: Decode a Base64 encoded file.  
Approach: Use `base64 -d` to decode.  
Command:
cat data.txt | base64 -d

🔹 Level 12 → 13
Goal: File is compressed multiple times with different formats.
Approach: Repeatedly use xxd, gzip, bzip2, and tar until you reach the final text file.
Example sequence:
xxd -r data.txt > data.bin
file data.bin
mv data.bin data.gz
gzip -d data.gz
bzip2 -d data.bz2
tar -xvf data.tar
cat final.txt

🔹 Level 13 → 14
Goal: Use a private SSH key to log into the next level.
Approach: Save the key as a file, set proper permissions, and connect with ssh -i.
Command:
chmod 600 sshkey.private
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220

🔹 Level 14 → 15
Goal: Submit the password on port 30000 to get the next password.
Approach: Use nc (Netcat) to send the current password.
Command:
nc localhost 30000
# paste the current password

🔹 Level 15 → 16
Goal: Connect using SSL on port 30001.
Approach: Use openssl s_client to establish the connection.
Command:
openssl s_client -connect localhost:30001

🔹 Level 16 → 17
Goal: Find the correct port among 31000-32000 that requires SSL and gives the next key.
Approach: Scan ports using nmap or a loop with nc, then connect with SSL.
Command (loop example):
for port in {31000..32000}; do
    timeout 1 bash -c "</dev/tcp/localhost/$port" && echo "Open: $port"
done

# Then connect:
openssl s_client -connect localhost:31790

🔹 Level 17 → 18
Goal: Compare two password files and find the difference.
Approach: Use diff to spot the correct password.
Command:
diff passwords.old passwords.new

🔹 Level 18 → 19
Goal: The server immediately closes normal sessions.
Approach: Use ssh with a command to avoid the shell.
Command:
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme

🔹 Level 19 → 20
Goal: A SUID binary reveals the next password when executed.
Approach: Execute the binary, which runs as the next user.
Command:
./bandit20-do cat /etc/bandit_pass/bandit20

✅ Notes
No passwords are shared to avoid spoilers.

This phase focuses heavily on:
Encoding/decoding (Base64, hexdump)
Compression (gzip, bzip2, tar)
Network tools (Netcat, OpenSSL)
SUID and privilege escalation basics

Bandit completed!
