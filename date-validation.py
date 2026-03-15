from datetime import datetime, timezone
import email.utils
 
def to_es_iso(value: str) -> str:
    """
    Convert many common date formats into:
    %Y-%m-%dT%H:%M:%S.%fZ
    """
 
    # 1. Try ISO-8601 / SQL-like formats
    iso_formats = [
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d"
    ]
    for fmt in iso_formats:
        try:
            dt = datetime.strptime(value, fmt)
            dt = dt.replace(tzinfo=timezone.utc)
            return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
 
    # 2. Try RFC-1123 (e.g., "Wed, 04 Mar 2026 04:00:02 GMT")
    try:
        dt = email.utils.parsedate_to_datetime(value)
        dt = dt.astimezone(timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    except Exception:
        pass
 
    # 3. Try epoch seconds or milliseconds
    try:
        num = float(value)
        # Detect ms vs seconds
        if num > 1e12:  # too large for seconds → treat as ms
            num /= 1000.0
        dt = datetime.fromtimestamp(num, tz=timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    except Exception:
        pass
 
    raise ValueError(f"Unrecognized date format: {value}")
 

def to_utc_string(value: str) -> str:
    value = value.strip()
 
    # Try format: YYYYmmDDHHMMSS.0Z  (e.g., 20260311002934.0z)
    try:
        dt = datetime.strptime(value.upper(), "%Y%m%d%H%M%S.0Z")
        return dt.replace(tzinfo=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        pass
 
    # Try RFC‑1123 format (e.g., Wed, 11 Mar 2026 00:01:18 +0000)
    try:
        dt = datetime.strptime(value, "%a, %d %b %Y %H:%M:%S %z")
        return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        pass
 
    # Try "YYYY-MM-DD HH:MM:SS" (assume UTC if no timezone)
    try:
        dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        dt = dt.replace(tzinfo=timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        pass
 
    raise ValueError(f"Unrecognized date format: {value}")
 
 
Code
from datetime import datetime, timezone
 
def normalize_datetime(value: str) -> str:
    """
    Convert YYYYmmDDHHMMSS.0Z → YYYY-mm-DDTHH:MM:SSZ
    If already in ISO format, return as-is.
    """
    # Try detecting ISO-8601 format
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
        return value  # Already normalized
    except ValueError:
        pass
 
    # Otherwise parse the compact format
    dt = datetime.strptime(value, "%Y%m%d%H%M%S.0Z")
    dt = dt.replace(tzinfo=timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
 
 
 

 
def to_timestamp_if_needed(value: str) -> float:
    """
    Convert RFC-1123 datetime (e.g., 'Wed, 04 Mar 2026 04:00:02 GMT')
    to a Unix timestamp, but only if it's not already a timestamp.
    """
 
    # 1. Check if it's already a numeric timestamp
    try:
        return float(value)
    except ValueError:
        pass
 
    # 2. Parse RFC-1123 format
    dt = datetime.strptime(value, "%a, %d %b %Y %H:%M:%S GMT")
    dt = dt.replace(tzinfo=timezone.utc)
 
    return dt.timestamp()
 
 
from datetime import datetime, timezone
 
def to_timestamp_if_needed(value: str) -> float:
    """
    Convert 'YYYY-MM-DD HH:MM:SS' to a Unix timestamp,
    but only if the value is not already a timestamp.
    """
 
    # 1. Check if it's already numeric (timestamp)
    try:
        return float(value)
    except ValueError:
        pass
 
    # 2. Parse the datetime string
    dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
 
    # Assume the datetime is in UTC; adjust if needed
    dt = dt.replace(tzinfo=timezone.utc)
 
    return dt.timestamp()
 
20260311002934.0z
Wed, 11 Mar 2026 —:01:18 +0000
2026-03-10 18:59:30
 
If a date string received as following (“20260311002934.0z” or “Wed, 11 Mar 2026 00:01:18 +0000”, or “2026-03-10 18:59:30”) convert it as date string in UTC in python
 
 
 
