#math.gcdを...使おう！w
def gcd(m,n):
    x,y=max(m,n),min(m,n)
    if x%y==0:
        return y
    else:
        while x%y!=0:
            z=x%y
            x=y
            y=z
        else:
            return z
def lcm(m,n):
    return m*n//gcd(m,n)