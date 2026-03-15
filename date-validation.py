from datetime import datetime, timezone
import email.utils

def normalize_datetime(value: str) -> str:
    """
    Convert many common date formats into:
    %Y-%m-%dT%H:%M:%S.%fZ
    """

    # Check for SQL-like formats
    iso_formats = [
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%Y%m%d%H%M%S.0Z",
        "%a, %d %b %Y %H:%M:%S %z",
        "%Y-%m-%dT%H:%M:%SZ"
    ]

    for fmt in iso_formats:
        try:
            dt = datetime.strptime(value, fmt)
            dt = dt.replace(tzinfo=timezone.utc)
            return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass

    # Check for form like "Wed, 04 Mar 2026 04:00:02 GMT"
    try:
        dt = email.utils.parsedate_to_datetime(value)
        dt = dt.astimezone(timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    except Exception:
        pass

    return datetime.fromtimestamp(0, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

def to_number_else_zero(field_value):
    """
    Checks if a field can be converted to a number
    and returns the number if successful, otherwise returns 0.
    """
    try:
        return int(field_value)
    except (ValueError, TypeError):
        return 0

if __name__ == "__main__":
    # Checking date conditions
    print("20260312002934.0z", normalize_datetime('20260312002934.0z'))
    print("Wed, 11 Mar 2026 00:01:18 +0000", normalize_datetime("Wed, 11 Mar 2026 00:01:18 +0000"))
    print("2026-03-10 18:59:30", normalize_datetime("2026-03-10 18:59:30"))
    print("0", normalize_datetime("0"))
    print("blank", normalize_datetime(""))
    print("aa", normalize_datetime("aa"))

    #Checking number conditions
    print("Case 1: ", to_number_else_zero('4'))
    print("Case 1: ", to_number_else_zero(5))
    print("Case 1: ", to_number_else_zero('a'))
    print("Case 1: ", to_number_else_zero(''))
