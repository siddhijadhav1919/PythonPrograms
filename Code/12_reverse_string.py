def reverse_string(text):
    result = ""
    for char in text:
        result = char + result
    return result


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Reversed:", reverse_string(text))