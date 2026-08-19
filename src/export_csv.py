import json
import csv
from pathlib import Path

reports_path = Path("reports")

report_files = sorted(
    reports_path.glob("run_*.json")
)

with open(
    "reports/history.csv",
    "w",
    newline=""
) as csv_file:

    writer = csv.writer(csv_file)

    writer.writerow([
        "readiness_score",
        "service",
        "scenario",
        "recovery_time_minutes",
        "target_rto_minutes",
        "rto_compliant"
    ])

    for report_file in report_files:

        with open(report_file) as json_file:

            report = json.load(json_file)

        writer.writerow([
            report["readiness_score"],
            report["service"],
            report["scenario"],
            report["recovery_time_minutes"],
            report["target_rto_minutes"],
            report["rto_compliant"]
        ])

print("CSV exported.")