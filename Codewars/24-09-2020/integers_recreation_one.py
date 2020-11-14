# https://www.codewars.com/kata/55aa075506463dac6600010d/python

import math
def list_squared(m, n):
    result = []
    #print(f"m: {m}, n: {n}", flush=True)
    for num in range(m, n + 1):
        #Get divisors, square divisors, add divisors
        list = []
        res = []
        # List to store half of the divisors 
        for i in range(1, int(math.sqrt(num) + 1)) : 
              
            if (num % i == 0) : 
                  
                # Check if divisors are equal 
                if (num / i == i) : 
                    res.append(i) 
                else : 
                    # Otherwise print both 
                    res.append(i) 
                    list.append(int(num / i)) 
                      
        # The list will be printed in reverse     
        for i in list[::-1] : 
            res.append(i) 
        #Check if its square
        suma = sum([i * i for i in res])
        if suma ** 0.5 % 1 == 0:
            result.append([num, suma])
    print(result)
    return result
    