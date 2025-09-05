try:
  number=int(input("please enter your number"))
  print("the number you have given is",number)
except ValueError as ex:
     print("exception",ex)