#largest prime factor of 600851475143
def largest_prime_factor(n):
    largest_prime_fact = 2
    # Divide the number by 2 until it is no longer even
    while n % 2 == 0:
        n //= 2
    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            largest_prime_fact = i
            n //= i
    # If n is still greater than 2, it is the largest prime factor
    if n > 2:
        largest_prime_fact = n
    return largest_prime_fact

print(largest_prime_factor(600851475143))
