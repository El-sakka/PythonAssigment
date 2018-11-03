def toBcd(x):
    s = str(x)
    res = ''
    for char in s:
        if char == '1':
            res += '0001'
        elif char == '2':
            res += '0010'
        elif char == '3':
            res += '0011'
        elif char == '4':
            res += '0100'
        elif char == '5':
            res += '0101'
        elif char == '6':
            res += '0110'
        elif char == '7':
            res += '0111'
        elif char == '8':
            res += '1000'
        elif char == '9':
            res += '1001'
        elif char == '0':
            res += '0000'
    return res

def add_bin(x,y):
    maxlen = max(len(x), len(y))
    #made both same lengths 
    x = x.zfill(maxlen)
    y = y.zfill(maxlen)

    res = ''
    car = 0

    for i in range(maxlen-1,-1,-1):
        r = car
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0

        res = ('1' if r % 2 == 1 else '0') + res
        car = 0 if r < 2 else 1
    
    if car != 0:
        res = '1' + res
    return res.zfill(maxlen)


def checkSix(s):
    st = ''
    res =''
    for char in s :
        st += char
        if len(st) == 4:
            if(int(st) > int('1001')):
                res += '0110'
            st=''
    return res

def backToDecimal(s):
    st = ''
    res = ''
    for char in s:
        st += char
        if len(st) == 4:
            if st == '0001':
                res += '1'
            elif st == '0010':
                res += '2'
            elif st == '0011':
                res += '3'
            elif st == '0100':
                res += '4'
            elif st == '0101':
                res += '5'
            elif st == '0110':
                res += '6'
            elif st == '0111':
                res += '7'
            elif st == '1000':
                res += '8'
            elif st == '1001':
                res += '9'
            st = ''
    return res


# x = toBcd(124)
# y = toBcd(197)

# z = add_bin(x,y)
# adding = checkSix(z)
# # print(z)
# # print(adding)

# w= add_bin(z,adding)

# print(backToDecimal(w))

x = int(input("Enter first Number : "))
y = int(input("Enter second Number : "))

xBcd = toBcd(x)
yBcd = toBcd(y)

addXY = add_bin(xBcd,yBcd)
six = checkSix(addXY)

addSix = add_bin(addXY,six)
print(backToDecimal(addSix))