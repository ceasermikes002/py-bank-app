# utils/random_generator.py
import random

def generate_random_number(digits):
    """Generate a random number with the specified number of digits."""
    if digits <= 0:
        raise ValueError("Number of digits must be greater than 0")

    lower_bound = 10 ** (digits - 1)
    upper_bound = 10 ** digits - 1
    return random.randint(lower_bound, upper_bound)
