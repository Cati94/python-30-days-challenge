import re
import argparse
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# Regex patterns
EMAIL_PATTERN = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
PHONE_PATTERN = re.compile(r"^\+?\d[\d\s]{7,15}$")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Validate emails and phone numbers"
    )
    parser.add_argument(
        "--file",
        help="Input file with emails and phones"
    )
    return parser.parse_args()


def clean(value):
    return value.strip()


def validate_email(email):
    return bool(EMAIL_PATTERN.match(email))


def validate_phone(phone):
    return bool(PHONE_PATTERN.match(phone))


def process_list(items, validator):
    valid = []
    invalid = []

    for item in items:
        item = clean(item)

        if not item:
            continue

        if validator(item):
            valid.append(item)
        else:
            invalid.append(item)

    return valid, invalid


def read_file(filepath):
    emails = []
    phones = []

    if not Path(filepath).exists():
        logging.error(f"File not found: {filepath}")
        return emails, phones

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            value = line.strip()

            if "@" in value:
                emails.append(value)
            else:
                phones.append(value)

    return emails, phones


def print_results(title, valid, invalid):
    print(f"\n{title}:")

    print("\nValid:")
    for v in valid:
        print(f" - {v}")

    print("\nInvalid:")
    for i in invalid:
        print(f" - {i}")


def main():
    args = parse_arguments()

    if args.file:
        emails, phones = read_file(args.file)
    else:
        # Default test data
        emails = [
            "test@example.com",
            "invalid-email",
            "user@domain.pt"
        ]

        phones = [
            "+351912345678",
            "1234",
            "+44 7700 900123"
        ]

    valid_emails, invalid_emails = process_list(emails, validate_email)
    valid_phones, invalid_phones = process_list(phones, validate_phone)

    print_results("Emails", valid_emails, invalid_emails)
    print_results("Phones", valid_phones, invalid_phones)


if __name__ == "__main__":
    main()
