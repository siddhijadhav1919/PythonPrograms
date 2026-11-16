def second_largest(numbers):
    unique = sorted(set(numbers))
    if len(unique) < 2:
        return None
    return unique[-2]


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Second largest:", second_largest(numbers))