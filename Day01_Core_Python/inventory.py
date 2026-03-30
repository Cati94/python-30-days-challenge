import csv
import logging
import argparse
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Calculate total inventory stock value from CSV file"
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="products.csv",
        help="Path to CSV file"
    )
    parser.add_argument(
        "--export",
        help="Export output to a file"
    )
    return parser.parse_args()


def detect_dialect(file):
    sample = file.read(1024)
    file.seek(0)

    try:
        return csv.Sniffer().sniff(sample)
    except Exception:
        logging.warning("Could not detect delimiter, defaulting to comma")
        return csv.excel


def clean_value(value):
    if value is None:
        return None
    return value.strip()


def calculate_inventory(file_path):
    total_value = 0.0
    product_values = []

    if not Path(file_path).exists():
        logging.error(f"File not found: {file_path}")
        return [], 0.0

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        dialect = detect_dialect(csvfile)
        reader = csv.DictReader(csvfile, dialect=dialect)

        for line_num, row in enumerate(reader, start=2):
            try:
                # Skip empty rows
                if not row or all(v is None or v.strip() == "" for v in row.values()):
                    continue

                name = clean_value(row.get("name"))
                price_str = clean_value(row.get("price"))
                quantity_str = clean_value(row.get("quantity"))

                if not name:
                    raise ValueError("Missing product name")

                if price_str is None or quantity_str is None:
                    raise ValueError("Missing price or quantity")

                price = float(price_str)
                quantity = int(quantity_str)

                if price < 0 or quantity < 0:
                    raise ValueError("Negative values not allowed")

                value = price * quantity
                total_value += value
                product_values.append((name, value))

            except Exception as e:
                logging.warning(f"Skipping line {line_num}: {e}")

    logging.info(f"Processed {len(product_values)} valid rows")

    return product_values, total_value


def format_output(product_values, total_value):
    sorted_products = sorted(product_values, key=lambda x: x[1], reverse=True)

    lines = []
    for name, value in sorted_products:
        lines.append(f"{name}: {value:.2f}")

    lines.append("-" * 30)
    lines.append(f"Total stock value: {total_value:.2f}")

    return "\n".join(lines)


def export_output(content, filepath):
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\nReport exported to: {filepath}")
    except Exception as e:
        logging.error(f"Export failed: {e}")


def main():
    args = parse_arguments()

    product_values, total_value = calculate_inventory(args.file)

    if not product_values:
        print("No valid data to process.")
        return

    output = format_output(product_values, total_value)

    print(output)

    if args.export:
        export_output(output, args.export)


if __name__ == "__main__":
    main()