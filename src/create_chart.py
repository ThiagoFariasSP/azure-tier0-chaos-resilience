import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reports/history.csv")

plt.plot(df.index + 1, df["readiness_score"])

plt.title("Readiness Score Trend")
plt.xlabel("Execution")
plt.ylabel("Readiness Score")

plt.grid(True)

plt.savefig("reports/readiness_trend.png")

print("Chart generated.")