# Day 1 – Inventory Stock Value Calculator

## 🎯 Objective
Build a Python script that processes a CSV file containing product inventory data and computes:

- Total value per product
- Global inventory value

This simulates a **real-world business task** (inventory valuation).

---

## 📥 Input

You are given a CSV file `products.csv` with the following structure:

name,price,quantity
Pen,1.2,100
Notebook,2.5,50
Backpack,25,10

---

## 📤 Expected Output

Pen: 120.0
Notebook: 125.0
Backpack: 250.0
--------------------
Total stock value: 495.0

---

## ⚙️ Requirements

- Use Python standard library (`csv`)
- Convert data types properly:
  - `price → float`
  - `quantity → int`
- Handle invalid rows gracefully (skip and log warning)
- Output must be formatted clearly

---

## ⚠️ Edge Cases

Your program should handle:

- Missing values
- Non-numeric price or quantity
- Empty lines
- Negative values (ignore or warn)

---

## 🧠 Hints

- Use `csv.DictReader`
- Use `try/except` for parsing errors
- Keep a running total variable
- Consider rounding output to 2 decimal places

---

## ⭐ Bonus (Professional Level)

- Sort output by highest stock value
- Export results to `report.txt`
- Add logging using `logging` module
- Accept file path as CLI argument

---

## 🧪 Example File

Create `products.csv`:
name,price,quantity
Pen,1.2,100
Notebook,2.5,50
Backpack,25,10
Invalid,abc,10

---

## 🚀 Deliverable

A Python script:
inventory.py


that when executed:

```bash
python inventory.py

Expected Skills
File handling
CSV parsing
Data validation
Basic error handling
Clean output formatting

---
