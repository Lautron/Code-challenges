# https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def anagrams(word, word_list):
    is_anagram = lambda word, anagram: sorted(word) == sorted(anagram)
    return [i for i in word_list if is_anagram(word, i)]

if __name__ == "__main__":
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
    