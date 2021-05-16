def check(l, n):
    i = 0
    while (i < len(l)):
        if (l[i] == n):
            return True
        i += 1
    return False

i = 0
a = []

while (i < 10):
    a.append(int(input("PLease enter a number: ")))
    i += 1

b = set()
i = 0

while (i < len(a)):
    # if not (check(b, a[i])):
    #     b.append(a[i])
    b.add(a[i])
    i += 1

print(a)
print(b)