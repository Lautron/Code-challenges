# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
words = {w: n for n, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split(' '))}
words.update({w: n * 10 for n, w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(' '), 2)})
thousands = {w: 1000 ** n for n, w in enumerate('thousand million'.split(' '), 1)}

def parse_int(string):
    res = []
    print(string)
    for word in string.replace(' and ', ' ').replace('-', ' ').split(' '):
        if word == 'hundred':
            res[-1] *= 100
            continue
        if word == 'thousand':
            res[-1] = sum(res[0:]) * 1000
            continue
        if word == 'million':
            res[-1] *= 1000000
            continue
        if word in words:
            res.append(words[word])
    print(res)
    return sum(res)

print(parse_int('one thousand three hundred and thirty-seven'))