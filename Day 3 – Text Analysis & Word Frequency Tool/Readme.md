# Day 3 – Text Analysis & Word Frequency Tool 📊

![Day 3 Banner](../images/day3.png)

## 🎯 Objective

Build a Python tool that analyzes a text file and identifies the most frequent words.

This simulates **real-world text processing tasks**, such as:

- Log analysis  
- Natural Language Processing (NLP) preprocessing  
- Data mining and analytics  

---

## 📌 Problem Statement

Given a text file, your program should:

- Normalize text (lowercase, remove punctuation)
- Extract words
- Count frequency of each word
- Display the most common words

---

## 📥 Input

A text file `document.txt`:


Python is great. Python is powerful!
Data analysis with Python is fun.
Fun and powerful tools make Python great.


---

## 📤 Expected Output


Top 5 most common words:

python: 4
is: 3
great: 2
powerful: 2
fun: 2


---

## ⚙️ Features

- 🔤 Case-insensitive processing  
- ✂️ Punctuation removal using regex  
- 📊 Word frequency counting  
- 📈 Sorted output (most frequent first)  
- ⚡ Efficient processing (line by line)  

---

## 🛠️ Technologies Used

- Python 3  
- `collections.Counter`  
- `re` (regular expressions)  
- `argparse`  
- `logging`  

---

## 🚀 How to Run

### Default:
```bash
python word_analyzer.py
Show top 10 words:
python word_analyzer.py --top 10
Remove stopwords:
python word_analyzer.py --no-stopwords
⚠️ Edge Cases Handled
Empty lines
Punctuation and special characters
Mixed uppercase/lowercase text
Large files (processed efficiently line by line)
⭐ Bonus Features
Remove common stopwords (e.g., "the", "is", "and")
Export results to file
Extend to support multiple languages
Generate word clouds
📁 Folder Structure
Day03_Text_Analysis/
│
├── README.md
├── word_analyzer.py
├── document.txt
└── output/
🧠 Learning Outcomes

By completing this exercise, you will:

Understand text normalization
Use regular expressions (regex) effectively
Work with efficient data structures (Counter)
Build a scalable text-processing pipeline
🌍 Real-World Applications

This type of processing is used in:

Search engines
Chatbots & AI models
Log and error analysis
Social media analytics
