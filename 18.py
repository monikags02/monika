print("enter the starting no:")
x=int(input())
print("enter the ending no:")
y=int(input())
for m in range(x+1,y):
    n=str(m)
    l=len(n)
    sum=0
    for i in range(0,l):
        u=n[i]
        v=(int(u))**3
        sum +=v
    if sum==int(n):
        print(n)
