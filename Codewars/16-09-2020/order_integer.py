# https://www.codewars.com/kata/5467e4d82edf8bbf40000155
def descending_order(num):
    # Separate integer
    #     Convert to string, and then put it into a list
    num_str = str(num)
    num_list = [int(i) for i in num_str]
    # Order integer
    #     reverse sort list
    num_sorted = sorted(num_list, reverse=True)
    # Return integer
    result = int(''.join(map(str, num_sorted)))
    return result

print(descending_order(12456))