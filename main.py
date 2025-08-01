medical_cause = input("does the student have any medical issues?(Y or N)").upper()
atten =int(input("what is the percentage of attendence ofthe student"))
if medical_cause=="Y":
  print("he can take the exam")
else:
   if atten>75:
      print("he can write the exam")
   else:
      print("Sorry you are not eligible for the exam")