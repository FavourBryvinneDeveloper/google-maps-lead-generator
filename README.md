# Google Maps Lead Generator

## Project Description
A Python application designed to help users find business information using the Google Places API and export the results into an Excel spreadsheet.

## Features
- Search businesses by category and location.
- Choose the number of businesses to retrieve (1–20).
- Display business names and addresses.
- Export business information to Excel.
- Professional Excel formatting.
- Input validation and error handling.

## Technologies Used
- Python
- Google Places API
- Requests
- OpenPyXL
- Python-dotenv

## Installation
Install the required packages:

```bash
py -m pip install requests python-dotenv openpyxl
```

## Configuration
Create a `.env` file and add your Google API key:

```text
GOOGLE_MAPS_API_KEY=your_api_key_here
```

Keep your API key private.

## Running the Application

```bash
py main.py
```

## Current Development Status
Offline testing is available using sample business data. Live Google Places API searches require appropriate billing configuration and API access.