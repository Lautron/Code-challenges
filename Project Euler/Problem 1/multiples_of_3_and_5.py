#TODO Find multiples below a limit
def find_multiples(num, limit):
    return {n for n in range(1, limit) if n % num == 0}

def main(limit):
    res = set()
    mult_3 = find_multiples(3, limit)
    mult_5 = find_multiples(5, limit)
    res.update(mult_5, mult_3)
    print(sum(res))

if __name__ == "__main__":
    main(1000)