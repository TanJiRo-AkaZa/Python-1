class veichle:
    def __init__(self,name,maxspeed,mileage):
       self.name=name
       self.maxspeed=maxspeed
       self.mileage=mileage
class bus(veichle):
     pass
school_bus=bus("School Volvo",180,12)
print("veichle name:",school_bus.name,"speed:",school_bus.maxspeed,"mileage:",school_bus.mileage    )