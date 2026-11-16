def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


if __name__ == "__main__":
    n = int(input("Enter a non-negative integer: "))
    print("Factorial:", factorial(n))