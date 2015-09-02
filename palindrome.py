import re


def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome

    word2= re.sub(r'[^A-Za-z]', "", sentence).lower()

    if len(word2) <= 1:
        return True

    elif word2[0] == word2[-1]:
        return is_palindrome(word2[1:-1])
    return False


def main():
     # TODO: put your input/output code here
    sentence = input("Please enter a word or sentence to test if it is palindromic: ")
    #word2 = re.sub(r'[^A-Za-z]', "", sentence).lower()
    if is_palindrome(sentence) == True:
        print("That is a palindrome!")
    else:
        print("Sorry, that is not a palindrome.")
    # word3 = word2[::-1]
    # if word2 == word3:
    #     print("y")
    # else:
    #     print("n")



if __name__ == '__main__':
    main()
