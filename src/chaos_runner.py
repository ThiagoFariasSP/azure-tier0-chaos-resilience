import json
import random
from pathlib import Path
from readiness import calculate_readiness_score

services = [
    "AUTH-01",
    "PAYMENT-API",
    "CUSTOMER-DB",
    "API-GATEWAY"
]

chaos_scenarios = [
    "VM Failure",
    "CPU Saturation",
    "Memory Leak",
    "Network Partition",
    "Replication Lag"
]

rto_targets = {
    "AUTH-01": 5,
    "PAYMENT-API": 5,
    "CUSTOMER-DB": 10,
    "API-GATEWAY": 5
}

service = random.choice(services)
scenario = random.choice(chaos_scenarios)

recovery_time = random.randint(1, 15)

target_rto = rto_targets[service]

rto_compliant = recovery_time <= target_rto
readiness_score = calculate_readiness_score(
    recovery_time,
    target_rto
)

report = {
    "readiness_score": readiness_score,
    "service": service,
    "scenario": scenario,
    "recovery_time_minutes": recovery_time,
    "target_rto_minutes": target_rto,
    "rto_compliant": rto_compliant
}

from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

report_path = Path(
    f"reports/run_{timestamp}.json"
)

with open(report_path, "w") as file:
    json.dump(report, file, indent=4)

print()
print("================================")
print("TIER 0 CHAOS TEST RESULT")
print("================================")
print(json.dumps(report, indent=4))
print("================================")
print()
print(f"Report saved to: {report_path}")