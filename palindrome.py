import re

def is_palindrome(word):
    # TODO: return True or False if the sentence is or isn't a palindrome
    # word = input("Please enter a word or sentence to test if it is palindromic: ")
    # word = main()
    word2 = re.sub(r'[^A-Za-z]', "", word).lower()
    word3 = word2[::-1]
    if word2 == word3:
    #     return True
    # else:
    #     return False
        print("yes")
    else:
        print("No")


def main():
#     # TODO: put your input/output code here
#     word = input("Please enter a word or sentence to test if it is palindromic: ")
#     return word

    # if is_palindrome() True:
    #     print("yes")
    # else:
    #     print("no")
    # word2 = re.sub(r'[^A-Za-z]', "", word).lower()
    # word3 = word2[::-1]
    # if word2 == word3:
    #     return True
    # else:
    #     return False

if __name__ == '__main__':
    main()
