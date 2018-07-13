def power(b,e):
    if(e==1):
        return(b)
    if(e!=1):
        return(b*power(b,e-1))
base=int(input("Enter b: "))
exp=int(input("Enter e value: "))
print("Result:",power(b,e))
