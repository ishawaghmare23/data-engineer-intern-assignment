from bs4 import BeautifulSoup


def extract_sections(html_content):
    """
    Extracts and categorizes content from raw HTML.
    """

    soup = BeautifulSoup(html_content, "html.parser")

    def get_text(tag):
        if tag:
            return tag.get_text(separator=" ", strip=True)
        return ""

    sections = {
        "navbar": get_text(soup.find("nav")),
        "homepage": get_text(soup.find("body")),
        "footer": get_text(soup.find("footer")),
        "case_study": ""
    }

    return sections
if __name__ == "__main__":
    with open("data/raw/example.com/homepage.html", "r", encoding="utf-8") as f:
        html = f.read()

    sections = extract_sections(html)

    for key, value in sections.items():
        print(f"\n--- {key.upper()} ---")
        print(value[:300])  # print first 300 chars

