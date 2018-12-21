#Frequency of each element of list
list=input("Enter the space separated elements of the list:").split()
frequency={}
for element in list:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print("Frequency Chart:")
for i,j in frequency.items():
    print(i,":",j)
