    from selenium import webdriver  # type: ignore
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By  # type: ignore
    import time

    # Initialize WebDriver
    driver = webdriver.Chrome()

    # List of URLs to scrape
    urls = ["https://x.com/GTNUK1", "https://twitter.com/whatsapp","https://x.com/aacb_CBPTrade","https://x.com/AAWindowPRODUCT","https://x.com/aandb_kia","https://x.com/ABHomeInc","https://twitter.com/Abrepro","https://x.com/ACChristofiLtd","https://x.com/aeclothing1","https://x.com/aeclothing1","https://x.com/AETechnologies1","https://x.com/wix","https://x.com/AGInsuranceLLC"]

    # Loop through URLs and extract data
    for i, url in enumerate(urls, start=1):
        try:
            driver.get(url)

            # Wait for the page to load (this is a fixed delay now)
            time.sleep(5)  # Adjust the sleep time as necessary

            # Find the element by class name
            elem = driver.find_element(By.CLASS_NAME, 'css-175oi2r')

            # Extract HTML content
            d = elem.get_attribute('outerHTML')

            # Save to a file
            with open(f'data/data_{i}.html', 'w', encoding='utf-8') as f:
                f.write(d)

            print(f"Data extracted from {url} and saved as data_{i}.html")

        except Exception as e:
            print(f"Error processing {url}: {e}")

        time.sleep(2)  # Delay between requests

    # Close the browser
    driver.quit()
