"""Task 1: number of days between a given date and today."""

from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    """Return the number of days from `date` ('YYYY-MM-DD') to today.

    The result is negative if `date` is in the future. Time of day is ignored.
    Returns None and prints a message if the input is not a valid date string.
    """
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        print(f"Invalid date: {date!r}. Expected format 'YYYY-MM-DD'.")
        return None

    today = datetime.today().date()
    return (today - given_date).days


if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))
    print(get_days_from_today("2099-01-01"))
    print(get_days_from_today("09.10.2021"))
