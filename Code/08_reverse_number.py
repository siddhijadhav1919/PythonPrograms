def reverse_number(num):
    sign = -1 if num < 0 else 1
    num = abs(num)
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return sign * reversed_num


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Reversed:", reverse_number(num))