from collections import OrderedDict
units = OrderedDict([
    (' year', 31536000), (' day', 86400), (' hour', 3600), (' minute', 60), (' second', 1)
])
def format_duration(seconds):
    if not seconds:
        return 'now'
    result = []
    for unit, value in units.items():
        quantity = int(seconds // value)
        seconds = seconds % value
        if quantity:
            res = str(quantity) + (unit + ',' if quantity == 1 else unit + 's,')
        else:
            res = ''
        result.append(res)
    return '{} {} {} {} {}'.format(*result).strip(', ').replace(',  ', ', ')[::-1].replace(' ,', ' dna ', 1)[::-1]

print(format_duration(0))
print(format_duration(3600))
print(format_duration(36001))
print(format_duration(56001))
