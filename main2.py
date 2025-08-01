unit=int(input("please enter the number of units entered"))
amount=0
extra=0
if  unit< 50 :
 amount=unit*2.60
 extra=25
elif unit<=100:
 amount=130 +((unit-50)*3.25)
 extra = 35

elif unit<=200:
 amount=130+162.5+((unit-100)*5.26)
 extra=45

else :
  amount=130+162.5+526+((unit-200)*8.45)
  extra=75

total=amount+ extra
print("\nElectricity Bill =%.2f" %total)

