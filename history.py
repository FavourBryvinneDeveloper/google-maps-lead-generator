import csv
from datetime import datetime
from pathlib import Path


HISTORY_FILE = Path(__file__).resolve().parent / "search_history.csv"


def save_search_history(category, location, requested, found):

    file_exists = HISTORY_FILE.exists()

    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Time",
                "Category",
                "Location",
                "Businesses Requested",
                "Businesses Found"
            ])

        now = datetime.now()

        writer.writerow([
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S"),
            category,
            location,
            requested,
            found
        ])

    print("Search history saved successfully.")


def view_search_history():

    if not HISTORY_FILE.exists():
        print("\nNo search history available yet.")
        return

    with open(HISTORY_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("\nNo previous searches found.")
        return

    print("\n============== BUSINESS SEARCH HISTORY ==============\n")

    headers = rows[0]
    data = rows[1:]

    widths = [
        max(len(str(row[i])) for row in rows)
        for i in range(len(headers))
    ]

    header_line = " | ".join(
        headers[i].ljust(widths[i])
        for i in range(len(headers))
    )

    print(header_line)
    print("-" * len(header_line))

    for row in data:
        print(" | ".join(
            row[i].ljust(widths[i])
            for i in range(len(headers))
        ))

    print("\nTotal previous searches:", len(data))
    print("\n======================================================")