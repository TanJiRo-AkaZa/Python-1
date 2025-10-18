class person(object):
    def __init__(self,name,idnumber):
       self.name=name
       self.idnumber=idnumber
    def display(self):
        print("name:",self.name)
        print("ID number:",self.idnumber)   
class employee(person):
        def __init__(   self,name,idnumber,salary,post):
            
            self.salary=salary
            self.post=post
            person.__init__(self,name,idnumber)
a=employee("rahul",886012,2000000,"manager")
a.display()
    