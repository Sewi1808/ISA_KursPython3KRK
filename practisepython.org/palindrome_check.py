w = input("Give me a random word:\n")
if w.lower() == w[::-1].lower():
    print("{} is a palindrome!".format(w))
else:
    print("{} is not a palindrome!".format(w))