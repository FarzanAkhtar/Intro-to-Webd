#Commas in number
def addcommas(a):
    for element in a:
        b=insertCommas(element)
        print(b)

def insertCommas(a):
    a=a[::-1]
    b=[]
    for i in range(len(a)):
        b.insert(0,a[i])
        if (i+1)%3 == 0:
            b.insert(0,",")

    if b[0] == ",":
        b.pop(0)

    return ("".join(b))


a=[]
n=int(input("No of numbers:"))
for i in range(n):
    a.append((input()))

print("Numbers with commas inserted:")
addcommas(a)
