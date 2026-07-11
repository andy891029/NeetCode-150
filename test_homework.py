data = [4,5,66,5,34,85,12,27]

def bubble(array):
    for i in range(len(array)-1):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array
#print(bubble(data))

def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick(left) + mid + quick(right)
print(quick(data))
