def calculate_risk(ip_address, device, failed_attempts):
    risk_score = 0

    if failed_attempts > 3:
        risk_score += 40

    if device == "unknown":
        risk_score += 30

    if ip_address.startswith("192."):
        risk_score += 10

    return risk_score