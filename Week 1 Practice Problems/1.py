#Fibonacci numbers
n=int(input("Enter an Integer:"))
a=0
b=1
print("First",n,"fibonacci numbers are:")
print(a)
print(b)
for i in range(2,n):
    c = a + b
    print(c)
    a=b
    b=c
