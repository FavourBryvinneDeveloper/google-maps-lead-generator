from export import export_to_excel
from history import save_search_history, view_search_history
from google_maps import search_businesses


USE_LIVE_API = False


def search_for_businesses():

    print("\n========== BUSINESS SEARCH ==========")

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

            print("Please enter a number between 1 and 20.")

        except ValueError:
            print("Invalid input. Enter numbers only.")

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

    save_search_history(category, location, limit, len(businesses))

    if not businesses:
        print("\nNo businesses found.")
        return

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

    export_to_excel(businesses, category, location)


def main():

    while True:

        print("\n================================")
        print("   GOOGLE MAPS LEAD GENERATOR")
        print("================================")
        print("1. Search for businesses")
        print("2. View previous searches")
        print("3. Exit")
        print("================================")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            search_for_businesses()

        elif choice == "2":
            view_search_history()

        elif choice == "3":
            print("\nThank you for using Google Maps Lead Generator!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()