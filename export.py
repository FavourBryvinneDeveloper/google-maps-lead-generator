from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill


def export_to_excel(businesses):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Business Leads"

    sheet.append(["Business Name", "Address", "Phone Number", "Website"])

    for business in businesses:
        name = business.get("displayName", {}).get("text", "Unknown")
        address = business.get("formattedAddress", "No address")
        phone = business.get("nationalPhoneNumber", "Not available")
        website = business.get("websiteUri", "Not available")

        sheet.append([name, address, phone, website])

        for cell in sheet[1]:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill(
            start_color="1F4E78",
            end_color="1F4E78",
            fill_type="solid"
            )

        sheet.freeze_panes = "A2"
        sheet.auto_filter.ref = sheet.dimensions

    sheet.column_dimensions["A"].width = 30
    sheet.column_dimensions["B"].width = 35
    sheet.column_dimensions["C"].width = 20
    sheet.column_dimensions["D"].width = 35

    try:
        workbook.save("business_leads.xlsx")
        print("Leads successfully exported to business_leads.xlsx")

    except PermissionError:
        print("Error: Close the Excel file and try again.")

    except Exception as error:
        print("Export failed:", error)