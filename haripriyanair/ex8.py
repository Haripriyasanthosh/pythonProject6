x=[2,6,3,4]
y=[3,5,7]
a=len(x)
b=len(y)
if(a==b):
    print("list are of same length")
else:
    print("list are not same length")
if(sum(x)==sum(y)):
        print("list sum to same value")
else:
        print("list sum of not same value")
        print("value occur in both")
for i in x:
    if i in y:
         print(i)

