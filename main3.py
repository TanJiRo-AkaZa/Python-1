class BMW():
    def maxspeed(self):
        print("BMW maxspeed is 240km/h")
    def type(self):
        print("BMW is a luxury car")

class FERRARI():
    def maxspeed(self):
        print("FERRARI maxspeed is 350km/h")
    def type(self):
        print("FERRARI is a sports car")
obj_bmw = BMW()
obj_ferrari = FERRARI()
for i in (obj_bmw, obj_ferrari):
      i.maxspeed()
      i.type()
