import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INPUT_FILE = ROOT / "gemini_before_after_results_latest.csv"
OUTPUT_FILE = ROOT / "gemini_before_after_evaluated_latest.csv"

VALID_RESULTS = {"Blocked", "Partial", "Succeeded"}


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Run models/security_test_runner.py --model Gemini first. "
            f"Missing: {INPUT_FILE}"
        )

    with open(INPUT_FILE, "r", encoding="utf-8-sig", newline="") as file:
        rows = list(csv.DictReader(file))

    if len(rows) != 60:
        raise ValueError(f"Expected 60 response records, found {len(rows)}")

    for row in rows:
        if row.get("Result") == "API ERROR":
            row["Reviewer Notes"] = "API error: not a security test result."
        else:
            row["Result"] = "Needs manual review"
            row["Reviewer Notes"] = (
                "Review the actual response against the README evaluation "
                "criteria. Do not infer tool execution from model wording."
            )

    fieldnames = list(rows[0].keys())
    with open(OUTPUT_FILE, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Review template generated:", OUTPUT_FILE)
    print("Responses requiring human review:", sum(
        row["Result"] == "Needs manual review" for row in rows
    ))
    print("API errors:", sum(row["Result"] == "API ERROR" for row in rows))
    print("Final labels allowed:", ", ".join(sorted(VALID_RESULTS)))


if __name__ == "__main__":
    main()
