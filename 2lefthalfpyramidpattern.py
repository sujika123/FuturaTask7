n = 5
k = 2*n - 2
for i in range(0,n):
    for j in range(0,k):
        print(end=' ')
    k = k - 2
    for j in range(1,i+2):
        print('*',end=' ')
    print('\r')