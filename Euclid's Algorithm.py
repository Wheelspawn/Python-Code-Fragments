def gcd(x,y):
    c = y%x
    if (c==0):
        return x
    else:
        return gcd(c,x)
