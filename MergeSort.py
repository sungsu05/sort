#병합 정렬
#분할 정복

def merge()

def merge_sort(arr,left,right):
    if left<right:
        middle = int((left+right)/2)
        
        merge_sort(arr,left,middle) # 재귀 분할의 왼쪽

        merge_sort(arr,middle+1,right) # 재귀 분할의 오른쪽

        merge(arr,left,middle,right) # 분할된 값을 정렬
    else : return


x = [20,40,10,50,30]
merge_sort(x,0,len(x))
#리스트,시작인덱스,마지막 인덱스