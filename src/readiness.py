def calculate_readiness_score(
    recovery_time: int,
    target_rto: int
) -> int:

    score = 100

    if recovery_time > target_rto:
        excess = recovery_time - target_rto
        score = max(0, 100 - (excess * 10))

    return score
