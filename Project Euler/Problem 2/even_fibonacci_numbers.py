
def fib_seq(limit):
    res = [1, 2]
    while True:
        res.append(res[-1] + res[-2])
        if res[-1] >= limit:
            del res[-1]
            break
    return res

def sum_even(fib_list):
    return sum([num for num in fib_list if num % 2 == 0])

def main():
    print(sum_even(fib_seq(4000000)))

if __name__ == '__main__':
    main()



