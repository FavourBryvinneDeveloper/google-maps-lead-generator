from export import export_to_excel
from google_maps import search_businesses

USE_LIVE_API = False

print("\nGOOGLE MAPS LEAD GENERATOR")
print("--------------------------")

while True:
    category = input("Enter business category: ").strip()

    if category:
        break

    print("Business category cannot be empty.")

while True:
    location = input("Enter location: ").strip()

    if location:
        break

    print("Location cannot be empty.")

while True:
    try:
        limit = int(input("How many businesses do you want to find? (1-20): "))

        if 1 <= limit <= 20:
            break
        else:
            print("Please enter a number between 1 and 20.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

if USE_LIVE_API:
    businesses = search_businesses(category, location, limit)

else:
    print("\nUsing sample data for testing...")

    businesses = [
        {
            "displayName": {"text": "Eldoret Electronics"},
            "formattedAddress": "Eldoret, Kenya"
        },
        {
            "displayName": {"text": "Eldoret Auto Garage"},
            "formattedAddress": "Eldoret, Kenya"
        }
    ]

if not businesses:
    print("\nNo businesses found.")
    print("Try another category or location.")

else:
    for business in businesses:
        name = business.get("displayName", {}).get("text", "Unknown")
        address = business.get("formattedAddress", "No address")
        phone = business.get("nationalPhoneNumber", "Not available")
        website = business.get("websiteUri", "Not available")

        print("\nBusiness:", name)
        print("Address:", address)
        print("Phone:", phone)
        print("Website:", website)
        print("--------------------------")

    print("\nTotal businesses found:", len(businesses))

    export_to_excel(businesses)