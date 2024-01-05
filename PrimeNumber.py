def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(n):
    prime_list = [num for num in range(2, n+1) if is_prime(num)]
    return prime_list

limit = 20
prime_numbers = generate_prime(limit)

print(f"Prime numbers up to {limit}: {prime_numbers}")
