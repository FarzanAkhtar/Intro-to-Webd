#Print the abbreviation
a=[]
while True:
    element=input()
    if element:
        a.append(element)
    else:
        break

for i in range(len(a)):
    if i>0:
        print("")
    letters=list(a[i])
    print(letters[0],end="")
    for j in range(len(letters)):
        if letters[j]==" ":
            print(letters[j+1],end="")
