import json
from pathlib import Path

reports_path = Path("reports")

report_files = list(
    reports_path.glob("run_*.json")
)

if not report_files:
    print("No reports found.")
    exit()

scores = []
recovery_times = []
success_count = 0

for report_file in report_files:

    with open(report_file, "r") as file:
        report = json.load(file)

    scores.append(report["readiness_score"])
    recovery_times.append(
        report["recovery_time_minutes"]
    )

    if report["rto_compliant"]:
        success_count += 1

average_score = sum(scores) / len(scores)

average_recovery = (
    sum(recovery_times)
    / len(recovery_times)
)

success_rate = (
    success_count
    / len(report_files)
) * 100

print()
print("========== DASHBOARD ==========")
print(
    f"Reports: {len(report_files)}"
)
print(
    f"Average Score: {average_score:.2f}"
)
print(
    f"Average Recovery: {average_recovery:.2f} min"
)
print(
    f"Success Rate: {success_rate:.2f}%"
)
print("===============================")