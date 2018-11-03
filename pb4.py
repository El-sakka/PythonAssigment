def toDecimal(n,b):
    res = int(0) 
    mul = int (1)
    while(n > 0):
        t = int(n % 10) 
        #print(t)
        res += (t * mul)
        mul *= b
        n = int(n/10)
    return res

def fromDecimalToAny(n,b):
    res = 0 
    mul = 1 
    while(n > 0):
        res += int(n%b) * mul
        mul *= 10
        n = int(n/b)
    return res

x = int(input("Enter Number : "))
y = int(input("Enter Number base : "))
todicmal = toDecimal(x,y)
z = int(input("Convert it to Base : "))
print(fromDecimalToAny(todicmal,z))