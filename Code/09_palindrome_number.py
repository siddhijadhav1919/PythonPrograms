def is_palindrome_number(num):
    if num < 0:
        return False
    text = str(num)
    return text == "".join(reversed(text))


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Palindrome" if is_palindrome_number(num) else "Not Palindrome")