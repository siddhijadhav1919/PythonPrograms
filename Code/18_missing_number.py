def missing_number(numbers):
    # The list should contain 1..n with exactly one number missing.
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(numbers)


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Missing number:", missing_number(numbers))