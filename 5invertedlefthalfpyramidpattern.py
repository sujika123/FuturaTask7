n = 5
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n, i, -1):
        print("*", end=" ")
    print()



print()
#Method2
print("Method2 : ")


rows = 5
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1




