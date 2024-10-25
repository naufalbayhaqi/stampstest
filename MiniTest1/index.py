def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(1, 101))

result = []
for num in reversed(numbers):
    if is_prime(num):
        continue
    elif num % 3 == 0 and num % 5 == 0:
        result.append("FooBar")
    elif num % 3 == 0:
        result.append("Foo")
    elif num % 5 == 0:
        result.append("Bar")
    else:
        result.append(str(num))

print(", ".join(result))