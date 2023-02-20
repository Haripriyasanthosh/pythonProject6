str=input("Enter the string:")
dict={}
a=str.split()
print(a)
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
print("Word frequency")
for x,y in dict.items():
        print(x,y)