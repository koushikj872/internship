def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def run_fizzbuzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0
    number_count = 0

    i = 1
    while i <= 50:
        result = fizzbuzz(i)
        print(result)

        if result == "FizzBuzz":
            fizzbuzz_count += 1
        elif result == "Fizz":
            fizz_count += 1
        elif result == "Buzz":
            buzz_count += 1
        else:
            number_count += 1

        i += 1

    print("\nCounts:")
    print("Fizz:", fizz_count)
    print("Buzz:", buzz_count)
    print("FizzBuzz:", fizzbuzz_count)
    print("Numbers:", number_count)


run_fizzbuzz()
