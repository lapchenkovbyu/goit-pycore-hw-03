"""Task 2: unique random lottery numbers."""

import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Return `quantity` unique random numbers from [min, max], sorted.

    Constraints: 1 <= min <= max <= 1000 and 1 <= quantity <= max - min + 1.
    Returns an empty list if any constraint is violated.
    """
    params_are_ints = all(isinstance(value, int) for value in (min, max, quantity))
    if not params_are_ints:
        return []
    if not (1 <= min <= max <= 1000):
        return []
    if not (1 <= quantity <= max - min + 1):
        return []

    # random.sample picks without repetition, so all numbers are unique.
    return sorted(random.sample(range(min, max + 1), quantity))


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
    print(get_numbers_ticket(0, 49, 6))   # min < 1 -> []
    print(get_numbers_ticket(1, 36, 40))  # too many numbers -> []
