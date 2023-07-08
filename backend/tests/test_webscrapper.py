import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.vectorstore.web_scraper import WebScraper
def test_webscrapper():
    scraper = WebScraper()
    links = "https://api.python.langchain.com/en/latest/api_reference.html"
    return scraper.get_page_data(links)
if __name__ == "__main__":
    test_webscrapper()