n, x = map(int, input().split())
array = list(map(int,input().split()))

def left_indexs(array, target, start, end, left_index):
    mid = ( start+end ) // 2
    if start > end:
        return left_index
    if array[mid] >= x:
        if left_index > mid:
            left_index = mid
        return left_indexs(array,target,start,mid-1,left_index)
    else:
        return left_indexs(array,target,mid+1,end,left_index) 

def right_indexs(array, target, start, end, right_index):

    mid = ( start+end ) // 2
    if start > end:
        return right_index
    if array[mid] <= x:
        if right_index < mid:
            right_index = mid
        return right_indexs(array,target,mid+1,end, right_index)
    else:
        return right_indexs(array,target,start,mid-1, right_index)
     
print(right_indexs(array,x,0,n-1,-1) - left_indexs(array,x,0,n-1,n) + 1)

