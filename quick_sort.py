def partition(list, low, high):
    i = (low-1)         
    pivot = list[high]     
  
    for j in range(low, high):
        if list[j] <= pivot:
            i = i+1
            list[i], list[j] = list[j], list[i]
  
    list[i+1], list[high] = list[high], list[i+1]
    return (i+1)
  
def quickSort(arr, low, high):
    if len(list) == 1:
        return list
    if low < high:
  
        index = partition(arr, low, high)

        quicksort(arr, low, index -1)
        quicksort(arr, index +1, high)
n=int(input("Enter Total Number of Students: "))
student=[]
for i in range (n):
    roll=int(input("Enter Roll No: "))
    student.append(roll)
print(quicksort(student , 0, n-1)