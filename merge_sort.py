def mergesort(student):
    if len(student) > 1:
        mid = len(student) // 2
        left = student[:mid]
        right = student[mid:]
        mergesort(left)
        mergesort(right)
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              student[k] = left[i]
              i += 1
            else:
                student[k] = right[j]
                j += 1 
            k += 1

        
        while i < len(left):
            student[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            student[k]=right[j]
            j += 1
            k += 1
n=int(input("Enter Total Number of Students: "))
student=[]
for i in range (n):
    roll=int(input("Enter Roll No: "))
    student.append(roll)
mergesort(student)
print(student)
