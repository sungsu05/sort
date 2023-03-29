def buble_sort(arr):
    for i in range(len(arr)-1):
        print()
        for j in range(len(arr)-1-i):
            #swap
            if arr[j]>arr[j+1] :
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
"""
x = [20,40,10,50,30]
i = 0 1 2 3
j == 5-1-i << j = len(x)-1-i
i = 0 , j = max(4)
i = 1 , j = max(3)
i = 2 , j = max(2)
i = 3 , j = max(1)

swap
i = 0, max(j) = 4
if arr[0] > arr[1] : False (20>40)
if arr[1] > arr[2] : True  (40>10) >> x = [20,10,40,50,30]
if arr[2] > arr[3] : False (40>50)
if arr[3] > arr[4] : True  (50>30) >> x = [20,10,40,30,50]

index 0번부터, 리스트의 마지막 index까지 순환하며
최대값을 가장 마지막 index에 삽입한다.
"""


x = [20,40,10,50,30]
print(buble_sort(x))