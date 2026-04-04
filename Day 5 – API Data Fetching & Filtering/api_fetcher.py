import requests
import argparse
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

API_URL = "https://jsonplaceholder.typicode.com/posts"


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Fetch and filter API data"
    )
    parser.add_argument(
        "--user",
        type=int,
        help="Filter by user ID"
    )
    parser.add_argument(
        "--keyword",
        help="Search keyword in title/body"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Limit number of results"
    )
    return parser.parse_args()


def fetch_data():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")
        return []


def filter_data(data, user_id=None, keyword=None):
    results = []

    for post in data:
        if user_id and post["userId"] != user_id:
            continue

        if keyword:
            text = (post["title"] + post["body"]).lower()
            if keyword.lower() not in text:
                continue

        results.append(post)

    return results


def print_results(posts, limit):
    if not posts:
        print("No results found.")
        return

    print(f"\nShowing {min(limit, len(posts))} results:\n")

    for post in posts[:limit]:
        print(f"ID: {post['id']}")
        print(f"User: {post['userId']}")
        print(f"Title: {post['title']}")
        print("-" * 40)


def main():
    args = parse_arguments()

    data = fetch_data()

    if not data:
        print("No data retrieved.")
        return

    filtered = filter_data(data, args.user, args.keyword)

    print_results(filtered, args.limit)


if __name__ == "__main__":
    main()
