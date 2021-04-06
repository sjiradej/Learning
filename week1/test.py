def isPalindrome(password):
    word=password.lower()
    if word==word[::-1] and word.isalpha():
        return True
    return False

def integer(number):
    if len(number)>=4 and number.isdigit():
        return True
    return False
def special(three):
    if len(three)==5 and three[0] in specials and three[4] in punct and three[1:3].isalpha():
        return True
    return False
    
specials = ['@', '$', '%', '^', '&']
punct = [",", ".", "?", "!"]
password, number, three = input().split()
if(isPalindrome(password) and integer(number) and special(three)):
    print('valid')
else:
    print('invalid')
