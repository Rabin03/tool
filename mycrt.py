import math

def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]


def mycrt(x,y,n1,n2):
    # x = X mod n1 && y = X mod n2
    
    a,b = extgcd(n1,n2)
    # a*n1 + b*n2 = 1

    ANS = b*x*n2 + a*y*n1
    ans = ANS % (n1*n2)
    
    return ans


x,y = (int(s) for s in input("x,y: ").split())
n1,n2 = (int(t) for t in input("n1,n2: ").split())

Ans = mycrt(x,y,n1,n2)

print("ans = ",end = "")
print(Ans)