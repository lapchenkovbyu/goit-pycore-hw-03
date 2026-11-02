"""Task 3: normalize phone numbers for SMS sending."""

import re


def normalize_phone(phone_number: str) -> str:
    """Return the phone number as '+' and digits only, with code +38 if missing.

    - Removes every character except digits and '+'.
    - Number starting with '380' gets '+' in front.
    - Number without an international code gets '+38' in front.
    """
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    if cleaned.startswith("+"):
        return cleaned
    if cleaned.startswith("380"):
        return "+" + cleaned
    return "+38" + cleaned


if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
