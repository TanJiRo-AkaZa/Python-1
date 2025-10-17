class employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("detructor called, employee deleted.")
def Create__obj():
    print("making object")
    obj = employee()
    print("function end")
    return obj
print("calling Create__obj function....")
obj = Create__obj()
print("program end")