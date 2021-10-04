a=[]
b=[]
c=[]
k=int(input("How many want to play cricket: "))
for i in range(k):
  l=int(input("Roll numbers: ")) 
  a.append(l)
p=int(input("How many want to play badminton: "))
for i in range(p):
  q=int(input("Roll numbers: "))
  b.append(q)
d=int(input("How many want to play football: "))
for i in range(d):
  e=int(input("Roll numbers: "))
  c.append(e)

print("\nRoll no who want play cricket :" , a)
print("Roll no who want play badminton : ", b)
print("Roll no who want play football : ", c)
  
def union(a, b):
    res = list(a)  
    for i in b:
        if i not in a:
            res.append(i)
    return res
    
def intersect(a,b):
    res = []
    for i in a:
        if i in b:
            res.append(i) 
    return res 
    
def eiter_or(a, b):
    u = union(a, b)
    i = intersect(a, b)
    for value in i:
        u.remove(value)
    return u
    
    
def minus(a, b):
    res = list(a)
    for i in b:
        if i in res:
            res.remove(i)
    return res
    


print(f"\nBoth Cricket and Badminton: {union(a, b)}")
print(f"Cricket or batminton but not both: {eiter_or(a, b)}")
print(f"Neitner cricket not football: {minus(minus(b, a), c)}")
print(f"Cricket and football but not batminton: {minus(intersect(a, c), b)}")
  
