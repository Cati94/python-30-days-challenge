import logging
import argparse
from collections import defaultdict, Counter
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Analyze server logs for activity and suspicious behavior"
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="logs.txt",
        help="Path to log file"
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=3,
        help="Failed login threshold for suspicious IPs (default: 3)"
    )
    return parser.parse_args()


def analyze_logs(file_path, threshold):
    if not Path(file_path).exists():
        logging.error(f"File not found: {file_path}")
        return None

    ip_counter = Counter()
    failed_attempts = defaultdict(int)
    unique_ips = set()

    with open(file_path, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, start=1):
            try:
                parts = line.strip().split()

                if len(parts) < 6:
                    raise ValueError("Malformed log line")

                timestamp = parts[0] + " " + parts[1]
                level = parts[2]
                user = parts[3]
                action = parts[4]
                ip = parts[5]

                # Track IP activity
                ip_counter[ip] += 1
                unique_ips.add(ip)

                # Track failed logins
                if action == "login_failed":
                    failed_attempts[ip] += 1

            except Exception as e:
                logging.warning(f"Skipping line {line_num}: {e}")

    # Identify suspicious IPs
    suspicious_ips = {
        ip: count for ip, count in failed_attempts.items()
        if count >= threshold
    }

    return {
        "unique_ips": unique_ips,
        "ip_counter": ip_counter,
        "failed_attempts": failed_attempts,
        "suspicious_ips": suspicious_ips
    }


def print_report(results):
    if not results:
        print("No data to analyze.")
        return

    print("\n=== LOG ANALYSIS REPORT ===\n")

    print(f"Unique IPs ({len(results['unique_ips'])}):")
    for ip in results["unique_ips"]:
        print(f" - {ip}")

    print("\nMost active IPs:")
    for ip, count in results["ip_counter"].most_common(3):
        print(f" - {ip}: {count} requests")

    print("\nFailed login attempts:")
    for ip, count in results["failed_attempts"].items():
        print(f" - {ip}: {count} failures")

    print("\nSuspicious IPs (threshold exceeded):")
    if results["suspicious_ips"]:
        for ip, count in results["suspicious_ips"].items():
            print(f" ⚠ {ip}: {count} failed attempts")
    else:
        print(" None detected")

    print("\n" + "=" * 35)


def main():
    args = parse_arguments()

    results = analyze_logs(args.file, args.threshold)

    print_report(results)


if __name__ == "__main__":
    main()
