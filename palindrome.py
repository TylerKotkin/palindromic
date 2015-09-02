import re

def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    pass


def main():
    # TODO: put your input/output code here
    word = input("Please enter a word or sentence to test if it is palindromic: ")
    newword = re.sub(r'[^A-Za-z]', "", word).lower()
    newword == newword[::-1]
    print(newword)

if __name__ == '__main__':
    main()
