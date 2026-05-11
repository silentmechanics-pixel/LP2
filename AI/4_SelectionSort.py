num = int(input("Enter no of Inputs: "))
arr=[]
for i in range(num):
  value = int(input("Enter Value: "))
  arr.append(value)

print("Unsorted Array ",arr)

for i in range(num):
  min_index = i

  for j in range(i+1, num):
    if arr[j] < arr[min_index]:
      min_index = j

  arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array after selection sort: ",arr)

