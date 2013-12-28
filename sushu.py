import math
def prime(n):
    for i in range(2,math.sqrt(n)):
        if n%i==0:
            return False
        return True

if __name__=='__main__':
    for i in range(100,1000+1):
        if prime(i):
            print i