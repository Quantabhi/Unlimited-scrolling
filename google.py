from playwright.sync_api import sync_playwright
import time
import random
from rich import print  # Assuming you have the rich library installed
import pandas as pd

def process_page(page):
    # Locate all the main divs on the page with a specific class
    main_divs = page.locator("//cite[contains(@class, 'qLRx3b tjvcx GvPZzd cHaqb')]").all()
    data = []
    
    # Iterate through each main div and extract text content
    for div in main_divs:
        text_content = div.text_content()
        data.append({'Text Content': text_content})
    
    return data

if __name__ == '__main__':
    # List of URLs to process
    urls_to_process = [
        "https://www.google.co.in/search?q=artificial+intelligence",
        # Add more URLs as needed
    ]

    # Launch Playwright browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        all_data = []

        # Loop through each URL
        for url in urls_to_process:
            # Create a new page in the browser
            page = browser.new_page()

            # Set viewport size
            page.set_viewport_size({"width": 1280, "height": 1080})

            # Navigate to the specified URL
            page.goto(url)

            # Wait for the page to reach a network idle state
            page.wait_for_load_state("networkidle")

            # Introduce a delay (2 seconds) to ensure all content is loaded
            time.sleep(2)

            # Perform a series of actions in a loop
            for iteration in range(15):
                print(f'Iteration: {iteration + 1}')

                # Press the 'End' key on the keyboard
                page.keyboard.press('End')
                print('Pressed the End key.')

                # Introduce a random sleep duration between 2 and 10 seconds
                random_sleep_duration = random.uniform(2, 10)
                time.sleep(random_sleep_duration)

                # Click on an element with the specified selector
                page.click('span.RVQdVd')
                print('Clicked the element.')

                # Introduce a fixed sleep duration of 2 seconds
                time.sleep(2)

            # Process the page and collect data
            data = process_page(page)
            all_data.extend(data)

            # Close the page
            page.close()

        # Close the browser
        browser.close()

        # Create a DataFrame from the collected data
        df = pd.DataFrame(all_data)

        # Save DataFrame to Excel file
        df.to_excel('output.xlsx', index=False)

        print('Data saved to output.xlsx')
