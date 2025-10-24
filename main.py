class myclass:
    __privatvar = 27
    def __privatmet(self):
        print("Iam inside class of myclass")
    def hello(self):
        print("private variable value is:",myclass.__privatvar)
foo =myclass()
foo.hello()
foo.__privatmet()  # This will raise an AttributeError