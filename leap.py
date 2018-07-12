x=int(input())
if(x%400==0):
    print ("leapyear")
elif(x%4==0):
    print ("leapyear")
elif(x%100!=0):
    print ("leapyear")
else:
    print ("not leapyear")
