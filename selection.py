#선택 정렬
def selection_sort(arr):
    a=10
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr),1):
            if arr[min_index] > arr[j] :
                min_index=j
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp 
    return arr
"""
x = [20,40,10,50,30]
i = 0,1,2,3
j= i+1,5
i=0, j = 1, max(4)
i=1, j = 2, max(4)
i=2, j = 3, max(4)
i=3, j = 4, max(4) (실행 없음)

i=0, j = 1, max(4)
arr[0] > arr[1] : False (20>40)
arr[0] > arr[2] : True (20>10) >> swap >> x = [10,40,20,50,30]
arr[0] > arr[3] : False (10>50)
arr[0] > arr[4] : False (10>30)

index 0번부터, 0번을 제외한 모든 index를 탐색하며
index 0보다 큰 수가 있다면, 스왑
작은 수 부터 0번 index를 채워가는 알고리즘

"""


x = [20,40,10,50,30]
print(selection_sort(x))
