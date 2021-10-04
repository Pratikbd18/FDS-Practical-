print("---*---Welcome To Big Bank---*---")
a=int(input("\nPlease Enter Amount Of Deposit :  "))
b=int(input("Please Enter Amount Of Withdraw : "))
bal=0
bal+=a
if b>bal:
  print("\nINSUFFICIENT BALANCE!!!")
else:
  print("\n Your Account Balance is : ", bal-b)
print("\n---*---Thank You--*---")