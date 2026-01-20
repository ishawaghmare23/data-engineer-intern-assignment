import requests
import os
from datetime import datetime


def crawl_website(url):
    """
    Crawls a website homepage and stores raw HTML.
    """
    try:
        response = requests.get(url, timeout=10)
        crawl_time = datetime.utcnow().isoformat()

        # Clean domain name for folder
        domain = url.replace("https://", "").replace("http://", "").replace("/", "")
        folder_path = f"data/raw/{domain}"
        os.makedirs(folder_path, exist_ok=True)

        # Save raw HTML
        file_path = f"{folder_path}/homepage.html"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response.text)

        metadata = {
            "url": url,
            "status_code": response.status_code,
            "crawl_time": crawl_time
        }

        print(f" Crawled successfully: {url}")
        return metadata

    except Exception as e:
        print(f" Error crawling {url}: {e}")
        return None



# CRAWLER FOR MULTIPLE WEBSITES

if __name__ == "__main__":

    websites = [
        "https://example.com",
        "https://stripe.com",
        "https://slack.com",
        "https://notion.so",
        "https://airbnb.com"
    ]

    for site in websites:
        result = crawl_website(site)
        print(result)
