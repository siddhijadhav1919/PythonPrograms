def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= c:
        return b
    return c


if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print(largest_of_three(a, b, c))