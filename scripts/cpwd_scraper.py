from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_cpwd():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    tenders = []
    try:
        print("CPWD website khol rahe hain...")
        driver.get('https://etender.cpwd.gov.in/')
        
        # Zyada wait karo (10 sec)
        time.sleep(10)
        
        print(f"Page title: {driver.title}")
        print(f"Current URL: {driver.current_url}")

        # Saare links print karo (debug ke liye)
        links = driver.find_elements(By.TAG_NAME, 'a')
        print(f"Total links mile: {len(links)}")
        
        # "New Tenders" dhundho
        new_tender_link = None
        for link in links:
            text = link.text.strip()
            if 'New Tender' in text or 'new tender' in text.lower():
                print(f"Link mila: {text}")
                new_tender_link = link
                break
        
        if new_tender_link:
            new_tender_link.click()
            time.sleep(10)
            print(f"New page title: {driver.title}")
            print(f"New URL: {driver.current_url}")
            
            # Ab table dhundo
            rows = driver.find_elements(By.CSS_SELECTOR, 'table tr')
            print(f"Table rows mile: {len(rows)}")
            
            for row in rows[1:21]:
                cols = row.find_elements(By.TAG_NAME, 'td')
                if len(cols) >= 3:
                    tender = {
                        'nit': cols[0].text.strip(),
                        'title': cols[1].text.strip(),
                        'cost': cols[2].text.strip() if len(cols) > 2 else 'N/A',
                        'deadline': cols[3].text.strip() if len(cols) > 3 else 'N/A'
                    }
                    if tender['title']:
                        tenders.append(tender)
                        print(f"Tender mila: {tender['title'][:50]}")
        else:
            print("New Tenders link nahi mila!")
            # Page source ka kuch part print karo
            print("Page source preview:")
            print(driver.page_source[:1000])
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

    print(f"Total tenders: {len(tenders)}")
    return tenders


if __name__ == '__main__':
    results = scrape_cpwd()
    for t in results:
        print(t)
