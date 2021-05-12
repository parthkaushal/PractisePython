j = 0

while (j < 5):
    p1 = input(" Player1, please enter r for rock, p for paper and s for scissors: ")
    p2 = input(" Player2, please enter r for rock, p for paper and s for scissors: ")
    
    if (p1 == p2):
        print("Tie!!")

    elif (p1 == "r" and p2 == "s"):
        print(" Player1 Won!!")

    elif (p1 == "r" and p2 == "p"):
        print(" Player2 Won!!")

    elif (p1 == "s" and p2 == "r"):
        print(" Player2 Won!!")

    elif (p1 == "s" and p2 == "p"):
        print(" Player1 Won!!")

    elif (p1 == "p" and p2 == "s"):
        print(" Player2 Won!!")

    elif (p1 == "p" and p2 == "r"):
        print(" Player1 Won!!")

    j += 1