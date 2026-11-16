def common_elements(list_one, list_two):
    result = []
    for item in list_one:
        if item in list_two and item not in result:
            result.append(item)
    return result


if __name__ == "__main__":
    list_one = input("Enter first list separated by space: ").split()
    list_two = input("Enter second list separated by space: ").split()
    print(common_elements(list_one, list_two))