from datetime import datetime
import json
import os


def transform_to_records(website, extracted_sections):
    """
    Transforms extracted sections into standardized records.
    """

    records = []
    crawl_timestamp = datetime.utcnow().isoformat()

    for section, content in extracted_sections.items():
        record = {
            "website": website,
            "section": section,
            "content": content,
            "crawl_timestamp": crawl_timestamp,
            "isActive": True
        }
        records.append(record)

    return records


def save_processed_data(domain, records):
    """
    Saves processed records as JSON in processed zone.
    """
    os.makedirs("data/processed", exist_ok=True)

    file_path = f"data/processed/{domain}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)


# -------------------------
# TESTING TRANSFORMER
# -------------------------
if __name__ == "__main__":

    from extractor import extract_sections

    website = "https://example.com"
    domain = "example.com"

    with open("data/raw/example.com/homepage.html", "r", encoding="utf-8") as f:
        html = f.read()

    sections = extract_sections(html)

    records = transform_to_records(website, sections)

    save_processed_data(domain, records)

    print("Processed data saved successfully")
