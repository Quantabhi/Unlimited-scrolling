# Unlimited scrolling in Google and save the output in the Excel file

## This Python script uses Playwright to perform web scraping on Google Search results for a given set of URLs related to "artificial intelligence." The collected data is then processed and saved to an Excel file using Pandas.

## Getting Started

### Prerequisites

- Python 3.x
- Playwright library
- Rich library
- Pandas library

Install the required libraries using:

```bash
pip install playwright rich pandas
## Script Overview

The script does the following:

1. Launches a Playwright browser.
2. Navigates to specified URLs.
3. Performs interactions on the Google Search results page.
4. Utilizes the Rich library for enhanced console output.
5. Collects data by locating and extracting text content from specific div elements on the page.
6. Simulates user actions like pressing the 'End' key and clicking on a specific element multiple times to load additional content.
7. Introduces delays to ensure page content is loaded before interactions.
8. Saves collected data to an Excel file (`output.xlsx`) using Pandas.

## Customization

Feel free to customize the script to fit your needs. You can modify the interaction logic, selectors, and other parameters based on the target website.

## Notes

- The script runs in non-headless mode (`headless=False`) in Playwright to allow for visual debugging.
- This script is designed for educational purposes and may require adjustments for production use.

**Note:** Ensure you comply with the terms of service of the websites you are scraping.
