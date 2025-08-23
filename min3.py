def sum( P ,Q):
    return P+Q
def sub(P,Q):
    return P-Q
def mul(P,Q):
    return P*Q
def div(P,Q):
    return P/Q
print(i("please enter the choice of calculation you want"))
print("a.add")
print("b.sub")
print("c.mul")
print("d.div")
choice=input("please enter your option")
num1=int(input("please enter the number of your choice"))
num2=int(input("please enter the number of your choice"))

if choice =="=a":
 print(num1,"+",num2=sum(num1,num2))
elif  choice =="b":
 print(num1,"-",num2=sub(num1,num2))
elif choice =="c":
 print(num1,"*",num2=mul(num1,num2))
elif choice =="d":
 print(num1,"/",num2=div(num1,num2))
else:
 print("input is invalid")
