def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    items = input("Enter items separated by space: ").split()
    print(remove_duplicates(items))