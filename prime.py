def prim(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
primes = [num for num in range(10,101) if prime(num)]
print(primes)