arr = []
n = int(input("Enter array Size "))
while(n>0):
    x = int(input("Enter number "))
    arr.append(x)
    n -= 1
arr.sort()
# print(arr)
k = int(input("enter k element : "))
print(arr[k-1])