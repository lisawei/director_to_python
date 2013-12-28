def a(n):
    if n==1:
        return 1
    return n*a(n-1)

def b(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

if __name__=='__main__':
    print b(4)
    print a(5)