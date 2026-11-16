def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(check_even_odd(number))