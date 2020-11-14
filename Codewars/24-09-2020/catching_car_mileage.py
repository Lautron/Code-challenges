# https://www.codewars.com/kata/52c4dd683bfd3b434c000292

def is_num(num):
    if num % 100 == num:
        return False
    # Followed by zeros
    if num % 100 == 0:
        return True
    num = str(num)
    # Palindrome
    if len(set(num)) == 1:
        return True

    if num in '1234567890':
        return True
    if num in '9876543210':
        return True
    if num == num[::-1]:
        return True
    
def is_interesting(number, awesome_phrases):
    if number + 1 in awesome_phrases or number + 2 in awesome_phrases:
        return 1
    if number in awesome_phrases:
        return 2
    if is_num(number + 1) or is_num(number + 2):
        return 1
    if is_num(number):
        return 2
    return 0
    

