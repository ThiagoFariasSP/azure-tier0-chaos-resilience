# Azure Tier 0 Chaos Resilience

## Overview

This project demonstrates Disaster Recovery (DR), Resilience Engineering, and Observability concepts using Kubernetes workloads monitored by Dynatrace.

The objective is to evaluate workload readiness through chaos testing scenarios and operational metrics.

## Environment

### Platform

- Kubernetes
- Dynatrace Playground

### Tier 0 Workload

- demo-oneagent

## Current Baseline

### Health

- Healthy

### Pods

- Running: 3
- Ready: 3

### Events

- No events detected

### Resource Utilization

- CPU stable
- Memory stable

## Readiness KPIs

- Workload Health
- Pod Availability
- CPU Utilization
- Memory Utilization
- Restart Count
- Recovery Time
- Readiness Score

## Chaos Scenarios

### Pod Failure

Simulates a pod becoming unavailable.

### High CPU Usage

Simulates workload pressure.

### High Memory Usage

Simulates memory exhaustion.

### Network Latency

Simulates communication degradation.

### Node Failure

Simulates node outage impact.

## Python Components

Current implementation:

- Chaos test simulator
- Readiness score calculator
- JSON report generation

## Sample Output

```json
{
  "readiness_score": 50,
  "service": "API-GATEWAY",
  "scenario": "Memory Leak",
  "recovery_time_minutes": 15,
  "target_rto_minutes": 5,
  "rto_compliant": false
}
```

## Future Enhancements

- Dynatrace API integration
- Automated dashboard generation
- Historical readiness tracking
- Kubernetes event correlation
- Recovery trend analysis
