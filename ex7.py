a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
j = 0

while (j < len(a)):
    if (a[j] % 2 == 0):
        b.append(a[j])
    j += 1

print(b)