def lgc(x,n,c,a,m):
    if (n>=0):
        x=(a*x+c)%m
        print(x)
        lgc(x,n-1,c,a,m)
        
c=101390422
a=1664525
m=2**32
lgc(99999,32,c,a,m)
