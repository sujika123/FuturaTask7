# n = 5
n = int(input("Enter the number of rows : "))
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print('*',end=" ") # printing * and staying in same line
    print("\r") # ending line after each row
