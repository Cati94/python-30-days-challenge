
## 🎯 Objective
Build a Python tool to analyze server logs and detect suspicious activity.

This simulates a **real-world cybersecurity / IT monitoring task**, where logs are analyzed to identify anomalies such as repeated failed login attempts.

---

## 📌 Problem Statement
Given a log file, your program should:

- Extract IP addresses
- Count total requests per IP
- Track failed login attempts
- Identify suspicious IPs based on a threshold

---

## 📥 Input

A text file `logs.txt` with entries like:


2026-04-01 10:00:01 INFO user1 login_success 192.168.1.10
2026-04-01 10:02:15 INFO user2 login_failed 192.168.1.11
2026-04-01 10:03:20 INFO user2 login_failed 192.168.1.11


### Log Format

[TIMESTAMP] [LEVEL] [USER] [ACTION] [IP]


---

## 📤 Expected Output


=== LOG ANALYSIS REPORT ===

Unique IPs (3):

192.168.1.10
192.168.1.11
10.0.0.5

Most active IPs:

192.168.1.11: 4 requests
10.0.0.5: 4 requests

Failed login attempts:

192.168.1.11: 3 failures
10.0.0.5: 4 failures

Suspicious IPs:
⚠ 192.168.1.11: 3 failed attempts
⚠ 10.0.0.5: 4 failed attempts


---

## ⚙️ Features

- 📊 Count requests per IP
- 🚨 Detect repeated failed logins
- 🔍 Identify suspicious activity
- ⚠ Handle malformed log lines gracefully
- 🧠 Configurable threshold for alerts

---

## 🛠️ Technologies Used

- Python 3
- `collections` (Counter, defaultdict)
- `argparse`
- `logging`

---

## 🚀 How to Run

### Default:
```bash
python log_analyzer.py
Custom file:
python log_analyzer.py logs.txt
Set suspicious threshold:
python log_analyzer.py --threshold 5
⚠️ Edge Cases Handled
Invalid or incomplete log lines
Missing fields
Empty lines
Non-standard formatting
⭐ Bonus Ideas
Export report to JSON/CSV
Detect brute-force attacks (time-based)
Add GeoIP lookup
Real-time log monitoring (tail -f style)
📁 Folder Structure
Day02_Log_Analysis/
│
├── README.md
├── log_analyzer.py
├── logs.txt
└── output/
🧠 Learning Outcomes

By completing this exercise, you will:

Understand log parsing
Work with real-world data formats
Implement basic security detection logic
Use Python collections effectively
Build a CLI tool
🔐 Real-World Relevance

This type of tool is used in:

Security Operations Centers (SOC)
Intrusion detection systems
Server monitoring tools
DevOps pipelines
