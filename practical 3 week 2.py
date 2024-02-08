def buggy_bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(n - i):

     print(arr, "i= ", i, "j =", j)

     if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

my_list = [90, 64, 34, 25, 22, 12, 11]
buggy_bubble_sort(my_list)
print("Sorted array:", my_list)


#T