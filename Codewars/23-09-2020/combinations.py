# https://www.codewars.com/kata/5263c6999e0f40dee200059d

from itertools import product
def get_pins(observed):
    posibilities = {
        '1': ['1', '2', '4'],
        '2': ['2', '1', '5', '3'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '4', '8', '6', '2'],
        '6': ['6', '9', '5', '3'],
        '7': ['7', '8', '4'],
        '8': ['8', '9', '5', '7'],
        '9': ['9', '8', '6'],
        '0': ['0', '8'],
    }
    combinations = product(*[posibilities[num] for num in observed])
    result = [''.join(tup) for tup in combinations]
    return result

if __name__ == "__main__":
    get_pins('123')
    

