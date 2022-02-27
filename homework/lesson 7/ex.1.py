
def palindrome(word):
    word = (input('Scrie cuvintul: '))
    reversed_str = word[::-1]
    return word == reversed_str

print(palindrome(' '))