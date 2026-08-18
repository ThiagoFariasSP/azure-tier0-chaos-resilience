def calculate_readiness_score(
    recovery_time: int,
    target_rto: int
) -> int:

    if recovery_time <= target_rto:
        return 100

    return 50