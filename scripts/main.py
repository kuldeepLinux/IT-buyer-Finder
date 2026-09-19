import os
from cpwd_scraper import scrape_cpwd
from ai_filter import filter_tenders
from notify import send_email

def load_keywords():
    path = os.path.join(os.path.dirname(__file__), '..', 'config', 'keywords.txt')
    with open(path, 'r') as f:
        return f.read().strip()

def main():
    print("Tenders scrape kar rahe hain...")
    keywords = load_keywords()
    print(f"Keywords: {keywords}")

    tenders = scrape_cpwd()
    print(f"Total tenders mile: {len(tenders)}")

    matches = filter_tenders(tenders, keywords)
    print(f"Matches: {len(matches)}")

    send_email(matches)

if __name__ == '__main__':
    main()
