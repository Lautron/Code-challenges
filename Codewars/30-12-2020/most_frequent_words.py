res = {}

def pop_max_val():
    result = max(res, key=res.get)
    res.pop(result)
    return result

def replace(string, ignore={',', '.', '\n', '//', ':', ';', '_', '?', '!', '-', '/'}):
    for char in ignore:
        string = string.replace(char, ' ')
    return string

def get_string_list(string):
    string = replace(string.strip(" '-"))
    word_list = [word for word in string.split(' ') if word ]
    return [replace(word) for word in word_list]

def top_3_words(string): 
    string_list = get_string_list(string.lower())
    word_set = set(string_list)
    for word in word_set:
        count = string_list.count(word)
        res.update({word: count})
    result = [pop_max_val() for _ in range(3)] if len(res) >= 3 else [pop_max_val() for _ in range(len(res))]
    res.clear()
    return result
