import os
import json


def aggregate_metrics():
    """
    Aggregates metrics from processed website data.
    """

    processed_path = "data/processed"

    metrics = {
        "total_websites": 0,
        "websites_with_case_study": 0,
        "active_websites": 0,
        "inactive_websites": 0,
        "content_length_by_section": {}
    }

    for file_name in os.listdir(processed_path):
        metrics["total_websites"] += 1

        file_path = os.path.join(processed_path, file_name)

        with open(file_path, "r", encoding="utf-8") as f:
            records = json.load(f)

        has_case_study = False
        is_active = False

        for record in records:
            section = record["section"]
            content_length = len(record["content"])

            metrics["content_length_by_section"].setdefault(section, [])
            metrics["content_length_by_section"][section].append(content_length)

            if section == "case_study" and content_length > 0:
                has_case_study = True

            if record["isActive"]:
                is_active = True

        if has_case_study:
            metrics["websites_with_case_study"] += 1

        if is_active:
            metrics["active_websites"] += 1
        else:
            metrics["inactive_websites"] += 1

    os.makedirs("data/aggregated", exist_ok=True)

    with open("data/aggregated/metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    print("Aggregated metrics saved successfully")
        


if __name__ == "__main__":
    aggregate_metrics()

