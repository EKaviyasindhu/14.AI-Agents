# filename: permutation_count.py
from collections import Counter

def count_permutations(word):
    """
    Calculates the number of permutations of a word, accounting for repeated characters.

    Args:
        word: The input string.

    Returns:
        The number of distinct permutations.
    """
    char_counts = Counter(word.lower())  # Ignore case, count character frequencies
    n = len(word)
    denominator = 1
    for count in char_counts.values():
        for i in range(1, count + 1):
            denominator *= i  # Calculate factorial of each character count
    return factorial(n) // denominator


def factorial(n):
    """
    Calculates factorial of n.

    Args:
        n: Non-negative integer.

    Returns:
        Factorial of n.
    """
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


word = "ALGEbRA"
permutation_count = count_permutations(word)
print(f"The number of permutations of '{word}' is: {permutation_count}")
