import sys



def sub(a,b):
    return a-b

def add(a,b):
    return a+b

n1=(input("enter first number"))
n2=(input("enter the second number"))

sum=add(n1,n2)
substr=sub(n1,n2)
print(f"sum of numbers{sum} and substr{substr}")
