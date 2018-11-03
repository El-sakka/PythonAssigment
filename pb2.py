def get_factor(n):
    arr = []
    for i in range(1,n+1):
        if n % i == 0:
            arr.append(i)
    print(arr)
get_factor(20)