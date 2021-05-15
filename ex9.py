import random
a = random.randint(0,9)
i = 0

while (i < 5):
    j = input("Plaese guess the number between 0-9: ")
    if(j.lower() == "exit"):
        break
    else:
        b = int(j)

    if (a == b):
        print("You guessed the number exactly right, number was", a)

    elif (a > b):
        print("You guessed the number a bit low, number was", a)

    elif (a < b):
        print("You guessed the number a bit high, number was", a)

    i += 1