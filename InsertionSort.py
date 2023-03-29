#삽입 정렬
def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -=1
    return arr 

"""
x = [20,40,10,50,30]
i = 0, 1, 2, 3, 4
j = 0, 1, 2, 3, 4

i = 0 , j = 0 (동작 없음)
i = 1 , j = 1         1 > 0  >> True   and  arr[0] > arr[1] >> False  :: 20 > 40  
i = 2 , j = 2         2 > 0  >> True   and  arr[1] > arr[2] >> True   :: 40 > 10
                        swap : x = [20,10,40,50,30] , j = 1
                      1 > 0  >> True   and  arr[0] > arr[1] >> True   :: 20 > 10
                        swap : x = [10,20,40,50,30] , j = 0

큰 값이 나오는 순간, 다시 회귀하여 0번째 index로 돌아간다.
즉, 최소값을 우선 탐색하여 0번째 index부터 채워 나가며 스왑한다.

"""



x = [20,40,10,50,30]
print(insertion_sort(x))