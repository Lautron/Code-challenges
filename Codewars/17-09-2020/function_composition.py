# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

def dry(arg, num): # Don't repeat yourself
    if arg == num:
        return arg
    else:
        return eval(num + arg)

def zero(arg='0'):
    return dry(arg, '0')
def one(arg='1'): 
    return dry(arg, '1')
def two(arg='2'): 
    return dry(arg, '2')
def three(arg='3'): 
    return dry(arg, '3')
def four(arg='4'): 
    return dry(arg, '4')
def five(arg='5'): 
    return dry(arg, '5')
def six(arg='6'): 
    return dry(arg, '6')
def seven(arg='7'): 
    return dry(arg, '7')
def eight(arg='8'): 
    return dry(arg, '8')
def nine(arg='9'): 
    return dry(arg, '9')


def plus(num): 
    return ' + ' + num
def minus(num): 
    return ' - ' + num
def times(num): 
    return ' * ' + num
def divided_by(num): 
    return ' // ' + num

if __name__ == "__main__":
    print(seven(times(five()))) # must return 35
    print(four(plus(nine()))) # must return 13
    print(eight(minus(three()))) # must return 5
    print(six(divided_by(two()))) # must return 3