primes = [2,3,5,7,11,13,17,19,23]
def getAllPrimeFactors(n):
    if n == 1: return [1]
    if not isinstance(n, int): return []
    if n < 0: return []

    result = []
    number = n
    for prime in primes:
        if number < prime: break
        while number % prime == 0:
            number = number / prime
            result.append(prime)
    if not result:
        result = [num for num in range(2, n) if n % num == 0]
    return result

            
            
def getUniquePrimeFactorsWithCount(n):
    prime_decomp = getAllPrimeFactors(n)
    factors = sorted(list(set(prime_decomp)))
    count = [prime_decomp.count(factor) for factor in factors]
    return [factors, count]
    
def getUniquePrimeFactorsWithProducts(n):
    prime_decomp = getAllPrimeFactors(n)
    factors = sorted(list(set(prime_decomp)))
    result = [factor ** prime_decomp.count(factor) for factor in factors]
    return result
