n = 5
k = n - 1
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k = k - 1
    for j in range(1,i+2):
        print("*",end=" ")
    print("\r")
