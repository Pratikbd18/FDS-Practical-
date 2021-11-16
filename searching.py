def linear(key,list):
    for n,i in enumerate(list):
        if i==key:
            return f"{key} is found at positfgion {n}!!!"
    return f"{key} is not found in list!!!"

def sentinel(key,list):
    last=list[n-1]
    list[n-1]=key
    i=0
    while (list[i]!=key):
        i+=1
    list[n-1]=last
    if ((i<n-1) or (list[n-1]==key)):
       return f"{key} is found at posihhtion {i}!!!"
    return f"{key} is not found in list!!!"

# def binary(key,list):
#     low=0
#     high=len(list)-1
#     while low<=high:
#         mid=(low+high)//2
#         if list[mid]==key:
#             return f"{key} is found at position {mid}!!!"
#         elif list[mid]>key:
#             for i in range (mid+1,n-1):
#                 if i==key:
#                     return f"{key} is found at position {i}!!!"
#         elif list[mid]<key:
#             for i in range (mid-1):
#                 if i==key:
#                     return f"{key} is found at position {i}!!!"
#                 return f"{key} is not found in list!!!"a

def binary(key,list):
    low=0
    high=len(list)-1
    found=False
    while low<=high:
        mid=(low+high)//2
        if key==mid:
            found=True
        elif key>mid:
            low =mid
            
        else :
            mid=high
    if found==True:
        return f"{key} is found at position {mid}!!!"
    return f"{key} is not found "



n=int(input("Enter Total Number of Students: "))
student=[]
for i in range (n):
    roll=int(input("Enter Roll No: "))
    student.append(roll)
key=int(input("Enter A Key"))
print(linear(key,student))
print(sentinel(key,student))
print(binary(key,student))
