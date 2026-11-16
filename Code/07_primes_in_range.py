def primes_in_range(start, end):
    primes = []
    for number in range(start, end + 1):
        if number < 2:
            continue
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes


if __name__ == "__main__":
    start, end = map(int, input("Enter start and end: ").split())
    print(primes_in_range(start, end))