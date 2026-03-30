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

## 📁 `Day01_Core_Python/inventory.py` (Reference Solution)

```python
import csv
import logging

logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")

def calculate_inventory(file_path):
    total_value = 0
    product_values = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for line_num, row in enumerate(reader, start=2):
            try:
                name = row["name"]
                price = float(row["price"])
                quantity = int(row["quantity"])

                if price < 0 or quantity < 0:
                    raise ValueError("Negative values not allowed")

                value = price * quantity
                total_value += value
                product_values.append((name, value))

            except Exception as e:
                logging.warning(f"Skipping line {line_num}: {e}")
                continue

    return product_values, total_value


def main():
    file_path = "products.csv"

    product_values, total = calculate_inventory(file_path)

    for name, value in product_values:
        print(f"{name}: {value:.2f}")

    print("-" * 20)
    print(f"Total stock value: {total:.2f}")


if __name__ == "__main__":
    main();
