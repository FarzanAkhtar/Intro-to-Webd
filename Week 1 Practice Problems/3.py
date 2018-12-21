#Greatest Common Divisor of two Numbers
a,b = map(int,input("Input two integers:").split())
print(a,b)

def gcd(a,b):
    if (a == b):
        return a
    elif (a > b):
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)

print("GCD of",a,"&",b,"is",gcd(a,b))
