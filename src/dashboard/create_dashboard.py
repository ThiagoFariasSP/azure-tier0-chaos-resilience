import pandas as pd

df = pd.read_csv("reports/history.csv")

average_score = df["readiness_score"].mean()
average_recovery = df["recovery_time_minutes"].mean()

success_rate = (
    df["rto_compliant"].sum()
    / len(df)
) * 100

html = f"""
<html>
<head>
<title>Tier 0 Resilience Dashboard</title>
</head>
<body>

<h1>Tier 0 Resilience Dashboard</h1>

<h2>KPIs</h2>

<ul>
<li>Average Readiness Score: {average_score:.2f}</li>
<li>Average Recovery Time: {average_recovery:.2f} min</li>
<li>Success Rate: {success_rate:.2f}%</li>
</ul>

<h2>Trend</h2>

<img srcs_trend.png

</body>
</html>
"""

with open(
    "reports/dashboard.html",
    "w",
    encoding="utf-8"
) as file:
    file.write(html)

print("Dashboard created.")