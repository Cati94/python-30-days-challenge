# Day 4 – Data Validation Tool ✅

![Day 4 Banner](../images/day4.png)

## 🎯 Objective

Build a Python tool to validate **email addresses** and **phone numbers**.

This simulates real-world scenarios such as:

- Web form validation  
- API input validation  
- Data cleaning pipelines  
- Security input filtering  

---

## 📌 Problem Statement

Given a list (or file) of inputs, your program should:

- Validate email addresses  
- Validate phone numbers  
- Separate valid and invalid entries  
- Display results clearly  

---

## 📥 Input

### Example (default input)


Emails:
test@example.com

invalid-email
user@domain.pt

Phones:
+351912345678
1234
+44 7700 900123


### Or from file (`data.txt`):


test@example.com

invalid-email
user@domain.pt

+351912345678
1234
+44 7700 900123


---

## 📤 Expected Output


Emails:

Valid:

test@example.com
user@domain.pt

Invalid:

invalid-email

Phones:

Valid:

+351912345678
+44 7700 900123

Invalid:

1234

---

## ⚙️ Features

- 📧 Email validation using regex  
- 📱 Phone validation (international formats supported)  
- 🧹 Input cleaning (trimming whitespace)  
- 📊 Classification of valid vs invalid data  
- ⚠ Handles empty or malformed input  

---

## 🛠️ Technologies Used

- Python 3  
- `re` (regular expressions)  
- `argparse`  
- `logging`  

---

## 🚀 How to Run

### Default (built-in data):
```bash
python validator.py
With file input:
python validator.py --file data.txt
⚠️ Edge Cases Handled
Empty lines
Leading/trailing spaces
Invalid formats
Mixed input types
⭐ Bonus Features
Export results to file
Support CSV input
Stricter validation rules
Batch validation for large datasets
📁 Folder Structure
Day04_Validation/
│
├── README.md
├── validator.py
├── data.txt
└── output/
🧠 Learning Outcomes

By completing this exercise, you will:

Understand regex-based validation
Learn input sanitization techniques
Build robust validation logic
Handle real-world messy data
🔐 Real-World Relevance

Validation is critical in:

Backend development
Authentication systems
API design
Cybersecurity (input filtering)

⚠ Poor validation can lead to:

Injection attacks
Data corruption
Security vulnerabilities
