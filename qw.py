g=int(input())
rev=0
while(g>0):
    dig=g%10
    rev=rev*10+dig
    g=g//10
print(rev)
