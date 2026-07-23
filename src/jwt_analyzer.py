from datetime import datetime, UTC

def analyze_jwt(payload):
    current_time = datetime.now(UTC)
    status = "Valid."
    issued_at = None
    not_before = None
    expiration_time = None
    remaining_time = None
    
    iat = payload.get('iat')
    if iat is not None:
        issued_at = datetime.fromtimestamp(iat, tz=UTC)

    nbf = payload.get('nbf')
    if nbf is not None:
        not_before = datetime.fromtimestamp(nbf, tz=UTC)
        if current_time < not_before:
            status = "Not yet valid."

    exp = payload.get('exp')
    if exp is not None:
        expiration_time = datetime.fromtimestamp(exp, tz=UTC)
        remaining = expiration_time - current_time
        if remaining.total_seconds() < 0:
            status = "Expired."
        else:
            remaining_time = {
                "days": remaining.days,
                "hours": remaining.seconds // 3600,
                "minutes": (remaining.seconds % 3600) // 60,
                "seconds": remaining.seconds % 60
            }

    return {
        "issued_at": issued_at,
        "not_before": not_before,
        "expiration_time": expiration_time,
        "remaining_time": remaining_time,
        "status": status
    }