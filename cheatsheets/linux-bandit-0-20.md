# Linux Cheat Sheet – OverTheWire Bandit (0→20)

**Author:** Bitnet  
**Repository:** https://github.com/Bitnet/Bitnet-labs.git
**Purpose:** Quick reference of commands and techniques used during Bandit levels 0→20

---

## 🗂 Navigation & Exploration
| Command       | Description                        | Example                   |
|---------------|------------------------------------|---------------------------|
| `pwd`         | Show current working directory     | `pwd`                     |
| `ls -la`      | List files (including hidden ones) | `ls -la`                  |
| `cd`          | Change directory                   | `cd /var/log`             |
| `file`        | Show file type                     | `file script.sh`          |

---

## 📄 File Viewing & Editing
| Command       | Description                        | Example                   |
|---------------|------------------------------------|---------------------------|
| `cat`         | Print entire file                  | `cat file.txt`            |
| `less`        | Paginated file viewer              | `less file.txt`           |
| `head`        | Show first 10 lines (default)      | `head -n 20 file.txt`     |
| `tail`        | Show last 10 lines (default)       | `tail -f /var/log/syslog` |
| `strings`     | Extract printable strings from bin | `strings binaryfile`      |
| `xxd`         | Convert binary to hex (hexdump)    | `xxd file`                |
| `xxd -r`      | Convert hex back to binary         | `xxd -r file.hex`         |
| `nano`        | Simple text editor                 | `nano script.sh`          |

---

## 🔑 Users & Permissions
| Command       | Description                        | Example                   |
|---------------|------------------------------------|---------------------------|
| `whoami`      | Show current user                  | `whoami`                  |
| `id`          | Show UID, GID and groups           | `id`                      |
| `chmod`       | Change file permissions            | `chmod 755 script.sh`     |
| `chown`       | Change file owner                  | `chown user:group file`   |

---

## 🔍 File & Content Search
| Command       | Description                        | Example                   |
|---------------|------------------------------------|---------------------------|
| `find`        | Search by filename                 | `find / -name passwd 2>/dev/null` |
| `find`        | Search by file size                | `find ./ -size 33c`       |
| `find`        | Search by permissions/user/group   | `find / -user bandit7 -group bandit6` |
| `grep`        | Search text in file                | `grep root /etc/passwd`   |
| `grep -R`     | Recursive text search              | `grep -R "password" .`    |
| `sort`        | Sort lines                         | `cat file | sort`         |
| `uniq`        | Remove duplicate lines             | `cat file | sort | uniq`  |
| `wc -l`       | Count lines                        | `wc -l file.txt`          |
| `diff`        | Compare files                      | `diff file1 file2`        |

---

## 📦 Compression & Archives
| Command       | Description                        | Example                   |
|---------------|------------------------------------|---------------------------|
| `tar -xvf`    | Extract `.tar` archive             | `tar -xvf file.tar`       |
| `gzip -d`     | Decompress `.gz` file              | `gzip -d file.gz`         |
| `bzip2 -d`    | Decompress `.bz2` file             | `bzip2 -d file.bz2`       |
| `xz -d`       | Decompress `.xz` file              | `xz -d file.xz`           |

---

## 🔡 Encoding & Transformation
| Command       | Description                        | Example                   |
|---------------|------------------------------------|---------------------------|
| `base64 -d`   | Decode Base64                      | `cat file.txt | base64 -d`|
| `tr`          | Translate/delete characters        | `cat file.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'` |
| `rev`         | Reverse lines of text              | `rev file.txt`            |

---

## 🌐 Remote Access & Transfer
| Command       | Description                        | Example                   |
|---------------|------------------------------------|---------------------------|
| `ssh`         | Remote SSH connection              | `ssh bandit0@host -p 2220`|
| `ssh -i`      | Connect using private key          | `ssh -i keyfile bandit@host -p 2220` |
| `scp`         | Copy file over SSH                 | `scp file user@host:/tmp` |
| `nc`          | Netcat TCP/UDP connection          | `nc -lvp 4444`            |

---

## 🔁 Redirection & Pipes
| Command       | Description                        | Example                   |
|---------------|------------------------------------|---------------------------|
| `>`           | Redirect output (overwrite file)   | `echo data > file.txt`    |
| `>>`          | Redirect output (append)           | `echo data >> file.txt`   |
| `|`           | Pipe output to another command     | `cat file | grep word`    |
| `2>/dev/null` | Suppress error messages            | `find / -name file 2>/dev/null` |

---

### ✅ Notes
This cheat sheet summarizes **all commands used in Bandit 0→20**, useful for:  
- Initial **Linux privilege escalation**  
- **CTF challenges and file enumeration**  
- Future **Red Teaming and pentesting labs**
