#  create all permutations of an input string and remove duplicates, if present.
# There is a more elegant way to accomplish this using python built in libraries, but I decided to create my own algorithm to solve this problem.
def permutations(string):
    res = set()
    if len(string) == 1:
        return string
    if len(string) == 2:
        return list({string, string[::-1]})
    for letter in string:
        remainding = string.replace(letter,"", 1)
        for permut in permutations(remainding):
            res.add(letter + permut)
            
    return list(res)

print(permutations("ab"))
print(permutations("abc"))
print(permutations("abca"))
