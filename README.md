
# Google Maps Lead Generator

A Python application for searching business information by category and location, displaying results, and exporting business leads into professionally formatted Excel spreadsheets.

## Features

- Search businesses by category and location.
- Choose the number of results (1–20).
- Display business names and addresses.
- Export results to Excel.
- Automatically create timestamped reports.
- View previous search history.
- Validate user input.
- Handle API and network errors.

## Technologies Used

- Python
- Google Places API
- Requests
- OpenPyXL
- Python-dotenv

## Installation

Clone or download this repository.

Install the required packages:

```bash
py -m pip install -r requirements.txt
```

## Configuration

The application currently supports offline demonstration using sample business data.

For optional live Google Places API integration, create a `.env` file in the project folder and add:

```text
GOOGLE_MAPS_API_KEY=your_api_key_here
```

Keep your API key private. Never upload your `.env` file to GitHub.

Live API access may require Google Cloud billing and can incur charges. Review the current pricing and obtain approval before enabling it.

## Running the Application

Run:

```bash
py main.py
```

## Generated Files

- Excel reports are saved in the `reports/` folder.
- Search history is saved in `search_history.csv`.

These generated files are excluded from GitHub.

## Development Status


## Demo Mode

The application currently runs in offline demonstration mode using clearly labelled sample business records.

Sample records are fictional and are not actual Google Maps business listings.

## Live Data Integration

The application includes Google Places API integration for optional live business searches.

Live API access has not been activated or tested. It may require Google Cloud billing and can incur charges.

## Project Status

The offline demonstration, input validation, search history, and Excel report generation are implemented.

The project is being prepared for further development and real-world use.


## License

No license has been specified yet.
