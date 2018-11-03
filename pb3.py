start = int(input("Enter your Start : "))
end = int(input("Enter your end : "))
for i in range(start,end+1):
    s = str(i)
    digits = len(s)
    x = 0
    for k in range(digits):
        x += ( int(s[k])**digits )
    if x == i :
        print(x)

