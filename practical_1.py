import array as arr 
list=arr.array('i', [])
n=int(input("enter the number of students : "))
sum=0

for i in range (n):
  num=int (input("enter the marks : "))
  if num>0:
    sum=num+sum
    avg=sum/n
  list.append(num)

count=0  
for i in range(n):
  if list[i]==-9:
    count=count+1
    
    

i=0
Max=0
count=0
for j in list :
  if list.index(j)==[i]:
    list.count(j)
    if list.count(j)>Max:
      Max=j
  i+=1


  
  

print (list)
print("sum=", sum)
print("avg=", avg)
print("absent students= ", count)
print("highest marks is",j, "with frequency ",count )
