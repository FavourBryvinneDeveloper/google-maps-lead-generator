import os
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parent / ".env")


def search_businesses(category, location, limit = 10):

    api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    if not api_key:
        print("API key not found. Check your .env file.")
        return []

    url = "https://places.googleapis.com/v1/places:searchText"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": (
            "places.id,"
            "places.displayName,"
            "places.formattedAddress"
        )
    }

    data = {
        "textQuery": f"{category} in {location}",
        "pageSize": limit
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=30
        )

        if response.status_code == 200:
            return response.json().get("places", [])

        print("Google API Error:", response.status_code)
        print(response.text)

    except requests.RequestException as error:
        print("Network error:", error)

    return []