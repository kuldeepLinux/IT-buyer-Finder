from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_cpwd():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    tenders = []
    try:
        driver.get('https://etender.cpwd.gov.in/')
        time.sleep(5)

        links = driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
            if 'New Tenders' in link.text:
                link.click()
                time.sleep(5)
                break

        rows = driver.find_elements(By.CSS_SELECTOR, 'table tr')
        for row in rows[1:21]:
            cols = row.find_elements(By.TAG_NAME, 'td')
            if len(cols) >= 4:
                tenders.append({
                    'nit': cols[0].text.strip(),
                    'title': cols[1].text.strip(),
                    'cost': cols[2].text.strip() if len(cols) > 2 else 'N/A',
                    'deadline': cols[3].text.strip() if len(cols) > 3 else 'N/A'
                })
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

    return tenders


if __name__ == '__main__':
    results = scrape_cpwd()
    for t in results:
        print(t)
