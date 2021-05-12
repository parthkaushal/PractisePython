wrd=input("Please enter a word: ")
rev = ""
j = len(wrd)

while (j > 0):
    j -= 1
    rev += wrd[j]

if (wrd == rev):
    print("This word is a palindrome")

else:
    print("This word is not a palindrome")

print("hello world")