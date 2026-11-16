def check_number(num):
    if num > 0:
        return "Positive"
    if num < 0:
        return "Negative"
    return "Zero"


if __name__ == "__main__":
    num = float(input("Enter a number: "))
    print(check_number(num))