from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from datetime import datetime
from pathlib import Path
import re


def export_to_excel(businesses, category, location):

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Business Leads"

    sheet.append(["Business Name", "Address", "Phone Number", "Website"])

    for cell in sheet[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(
            start_color="1F4E78",
            end_color="1F4E78",
            fill_type="solid"
        )

    for business in businesses:
        name = business.get("displayName", {}).get("text", "Unknown")
        address = business.get("formattedAddress", "No address")
        phone = business.get("nationalPhoneNumber", "Not available")
        website = business.get("websiteUri", "Not available")

        sheet.append([name, address, phone, website])

    sheet.freeze_panes = "A2"
    sheet.auto_filter.ref = sheet.dimensions

    # Automatically adjust column widths
    for column in sheet.columns:
        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))

        sheet.column_dimensions[column_letter].width = max_length + 5

    # Create a unique filename
    clean_category = re.sub(r'[^\w-]', '_', category.lower())
    clean_location = re.sub(r'[^\w-]', '_', location.lower())

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{clean_category}_{clean_location}_{timestamp}.xlsx"

    try:
        reports_folder = Path(__file__).resolve().parent / "reports"
        reports_folder.mkdir(exist_ok=True)

        workbook.save(reports_folder / filename)
        print(f"Leads successfully exported to: {reports_folder / filename}")

    except PermissionError:
        print("Error: Close the Excel file and try again.")

    except Exception as error:
        print("Export failed:", error)