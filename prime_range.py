"""
Write a Python program that takes two numbers, start and end, and prints all prime numbers in that range.

Example:
  For start = 10, end = 30:
  11, 13, 17, 19, 23, 29
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    print("Prime numbers in the range:", ", ".join(map(str, primes)))


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print_primes(start, end)
