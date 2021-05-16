def fibonnaciGenerator(n):
    i = 0
    j = 1
    k = 1
    l = 0

    print(j)
    print(k)

    while (i < n - 2):
        l = k + j
        print(l)
        j = k
        k = l
        i += 1

n = int(input("Please enter how many fibonnaci numbers to generate: "))
fibonnaciGenerator(n)
