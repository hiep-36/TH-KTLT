print("Le Hoa Hiep")
print("235752021610073")
def generate_primes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p,limit + 1,p):
                is_prime[i] = False
        p += 1
    return tuple(p for p in range(2, limit) if is_prime[p])

p=generate_primes(1000)
print("Tuple p gồm các nguyên to nho hon 1 trieu:",p)
