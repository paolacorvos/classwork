from typing import List

def get_factors(num: int) -> List[int]:
    """
    Returns a list of factors for the provided num
    
    Args:
        num (int): The umber for which we want factors
    Return:
        List[int]: A list of factors for the num.
    """
    factors = []
    for i in range(1,num+1): # range return ints # between start (defaults and 0), end (exclusive)
        if num % i == 0:
            factors.append(i)
    return factors

def get_prime_factors(num: int) -> List[int]:
    primes = []
    for i in get_factors(num):
        factors = get_factors(i)
        if len(factors) == 2:
            primes.append(i)
    return primes