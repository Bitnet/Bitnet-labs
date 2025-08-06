# OverTheWire: Bandit (Levels 0→10)

**Author:** Bitnet  
**Repository:** https://github.com/Bitnet/Bitnet-labs.git
**Objective:** Practice basic Linux commands, file handling, permissions, and remote access via SSH.

---

## 🔹 Level 0 → 1
**Goal:** Connect to the Bandit server via SSH.  
**Approach:** Use the given user and port.  
**Command:**
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220

🔹 Level 1 → 2
Goal: Read a file named -.
Approach: Use ./ to avoid it being interpreted as an option.
Command:
cat ./-

🔹 Level 2 → 3
Goal: Read a file with spaces in its name.
Approach: Use quotes or escape spaces with \.
Command:
cat spaces\ in\ this\ filename

🔹 Level 3 → 4
Goal: Find and read a hidden file in inhere.
Approach: List hidden files using ls -la.
Command:
cd inhere
ls -la
cat .hidden

🔹 Level 4 → 5
Goal: Identify the human-readable file among many.
Approach: Use file * to check file types.
Command:
cd inhere
file ./*
cat ./-file07

🔹 Level 5 → 6
Goal: Find a file of a specific size (1033 bytes).
Approach: Use find with size filter.
Command:
find inhere/ -type f -size 1033c
cat inhere/maybehere07/.file2

🔹 Level 6 → 7
Goal: Find a file by owner, group, and size.
Approach: Use find filtering user, group, and file size.
Command:
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
cat /var/lib/dpkg/info/bandit7.password

🔹 Level 7 → 8
Goal: Find the line containing the password in data.txt.
Approach: Use grep to search for the word millionth.
Command:
grep "millionth" data.txt

🔹 Level 8 → 9
Goal: Identify the unique line in the file.
Approach: Use sort and uniq -u.
Command:
sort data.txt | uniq -u

🔹 Level 9 → 10
Goal: Find the password in a binary file.
Approach: Use strings and search for = symbol.
Command:
strings data.txt | grep "="

✅ Notes
No passwords are published to avoid spoilers.
Focus on technique and command usage.
This write-up demonstrates practical Linux enumeration relevant to CTFs and pentesting.
