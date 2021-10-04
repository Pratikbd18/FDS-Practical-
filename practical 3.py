s=input("please enter name of person: ")
d=int(input("please choose the Designation of person \n1. Manager  \n2. Team Leader \n3. Employee: ")) 
m=(input("please enter the name of month"))
p=int(input("number of days he/she is present: "))
o=int(input("please enter no of days he/she did Overtime: ")) 
if (m=="Jan" or "mar" or "may" or "jul" or "aug" or "oct" or "dec") :
  d=31
elif m=="apr" or "jun" or "sep" or "nov":
  d=30
elif m=="feb":
  d=29
else:
  print("INVALID!! ")
  #break
  
if (d==1):
    d=2000
    sal=(p*d)+((o/2)*d)
    print("Total Salary Of", s, "is", sal)
    
elif(d==2):
    d=1800
    sal=(p*d)+((o/2)*d)
    print("Total Salary Of", s, "is", sal)
else:
    d=1500
    sal=(p*d)+((o/2)*d)
    print("Total Salary Of", s, "is", sal) 
#else:
  #print("INVALID!! ")
     

