def num_factory(num):
    return lambda arg=num: arg if arg == num else eval(num + arg)

def op_factory(operator):
    return lambda num: f' {operator} ' + num

zero, one, two, three, four, five, six, seven, eight, nine = [num_factory(str(num)) for num in range(10)]
plus, minus, times, divided_by = [op_factory(op) for op in ['+', '-', '*', '//']]

