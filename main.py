class IOSstring:
    def __init__(self):
        self.str1 = ""
    def get__string(self):
        self.str1 = input("Enter a string: ")
    def print__string(self):
        print("The result is:", self.str1.upper())
str1 = IOSstring()
str1.get__string()
str1.print__string()
