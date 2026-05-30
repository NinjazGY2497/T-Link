from datetime import datetime, timezone

def genTimestamp() -> int:
    utcNow = datetime.now(timezone.utc)
    return int(utcNow.timestamp())