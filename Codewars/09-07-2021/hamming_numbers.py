#A Hamming number is a positive integer of the form 2^i * 3^j * 5^k, for some non-negative integers i, j, and k.
#
#Write a function that computes the nth smallest Hamming number.


exponents = [ (i, j, k) for k in range(50)
                        for j in range(50)
                        for i in range(50) ]

nums = sorted([2**i * 3**j * 5**k for i, j, k in exponents])

def hamming(n):
    return nums[n-1]
