try:
    num1,num2=eval(input("enter two numbers seperated by a comma"))
    result=num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("division by zero is error!!!")
except SyntaxError:
    print("comma is missing enter numbers in comma just like this 1,2")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will execute")