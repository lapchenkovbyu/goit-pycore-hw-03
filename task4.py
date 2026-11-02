"""Task 4: upcoming birthdays for the next 7 days (including today)."""

from datetime import date, datetime, timedelta

DAYS_AHEAD = 7
DATE_FORMAT = "%Y.%m.%d"


def _birthday_in_year(birthday: date, year: int) -> date:
    """Return the birthday in `year`; Feb 29 becomes Mar 1 in non-leap years."""
    try:
        return birthday.replace(year=year)
    except ValueError:
        return date(year, 3, 1)


def get_upcoming_birthdays(users: list[dict], today: date | None = None) -> list[dict]:
    """Return who to congratulate in the next 7 days, today included.

    Each user is {"name": str, "birthday": "YYYY.MM.DD"}. A birthday on
    Saturday or Sunday is congratulated on the following Monday.
    Result items: {"name": str, "congratulation_date": "YYYY.MM.DD"}.
    """
    today = today or datetime.today().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], DATE_FORMAT).date()

        birthday_this_year = _birthday_in_year(birthday, today.year)
        if birthday_this_year < today:
            birthday_this_year = _birthday_in_year(birthday, today.year + 1)

        if (birthday_this_year - today).days >= DAYS_AHEAD:
            continue

        congratulation_date = birthday_this_year
        if congratulation_date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            congratulation_date += timedelta(days=7 - congratulation_date.weekday())

        upcoming.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime(DATE_FORMAT),
        })

    return upcoming


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users, today=date(2024, 1, 22))
    print("Список привітань на цьому тижні:", upcoming_birthdays)
