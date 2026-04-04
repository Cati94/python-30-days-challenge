## 🎯 Objective

Build a Python tool that fetches data from a public API and filters it based on user-defined criteria.

This simulates real-world tasks such as:

- Backend API consumption  
- Data pipeline processing  
- Automation scripts  
- Cybersecurity intelligence gathering  

---

## 📌 Problem Statement

Using a public API, your program should:

- Fetch data from an endpoint  
- Parse JSON response  
- Filter results by user ID  
- Search content by keyword  
- Display results in a clean format  

---

## 📥 Input

Data is fetched from:

https://jsonplaceholder.typicode.com/posts


### Example JSON Response

```json id="sk7fdg"
{
  "userId": 1,
  "id": 1,
  "title": "example title",
  "body": "example content"
}

📤 Expected Output

Showing 3 results:

ID: 1
User: 1
Title: sunt aut facere repellat provident occaecati
----------------------------------------

ID: 2
User: 1
Title: qui est esse
----------------------------------------
``` id="7w9nre"

---

## ⚙️ Features

- 🌐 Fetch data using HTTP requests  
- 📦 Parse JSON responses  
- 🔎 Filter by user ID  
- 🔍 Search by keyword  
- 📊 Limit number of results  
- ⚠ Handle API/network errors gracefully  

---

## 🛠️ Technologies Used

- Python 3  
- `requests`  
- `argparse`  
- `logging`  

---

## 🚀 How to Run

### Default:
```bash
python api_fetcher.py

Filter by user:

python api_fetcher.py --user 1

Search keyword:

python api_fetcher.py --keyword "qui"

Combine filters:

python api_fetcher.py --user 1 --keyword "qui" --limit 3

⚠️ Edge Cases Handled

    API request failures

    Empty responses

    Invalid filters

    Network timeouts

⭐ Bonus Features

    Export results to JSON file

    Add pagination support

    Use authenticated APIs (API keys)

    Cache API responses

📁 Folder Structure

Day05_API_Fetching/
│
├── README.md
├── api_fetcher.py
└── output/

🧠 Learning Outcomes

By completing this exercise, you will:

    Understand REST API consumption

    Work with JSON data structures

    Implement filtering logic

    Handle network errors

    Build real-world CLI tools

🌍 Real-World Applications

This type of workflow is used in:

    Web applications

    Data engineering pipelines

    Automation tools

    Cybersecurity (threat intelligence APIs)
