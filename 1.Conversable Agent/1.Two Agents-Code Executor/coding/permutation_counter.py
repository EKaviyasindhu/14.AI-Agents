# filename: permutation_counter.py
import math

def count_unique_permutations(word):
    """
    Calculates the number of unique permutations of a word.

    Args:
      word: The input word (case-insensitive).

    Returns:
      The number of unique permutations.  Returns 0 if the input is invalid.
    """
    word = word.lower()
    n = len(word)
    if n == 0:
        return 0

    char_counts = {}
    for char in word:
        char_counts[char] = char_counts.get(char, 0) + 1

    numerator = math.factorial(n)
    denominator = 1
    for count in char_counts.values():
        denominator *= math.factorial(count)

    return numerator // denominator


#Verification
word = "ALGEBRA"
unique_permutations = count_unique_permutations(word)
print(f"The number of unique permutations of '{word}' is: {unique_permutations}") # Output should be 2520

word = "ALGEbRA" #case-insensitive test
unique_permutations = count_unique_permutations(word)
print(f"The number of unique permutations of '{word}' is: {unique_permutations}") # Output should be 2520

word = "" #empty string test
unique_permutations = count_unique_permutations(word)
print(f"The number of unique permutations of '{word}' is: {unique_permutations}") # Output should be 0

word = "AAABBB" #test with repeated letters
unique_permutations = count_unique_permutations(word)
print(f"The number of unique permutations of '{word}' is: {unique_permutations}") # Output should be 20

