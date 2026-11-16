def is_palindrome_string(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == "".join(reversed(cleaned))


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Palindrome" if is_palindrome_string(text) else "Not Palindrome")