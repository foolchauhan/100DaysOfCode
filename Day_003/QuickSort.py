def quickSort(arr, low, high):
    if(low<high):
        pi = partition(arr, high, low)      # pi is partition index, arr[pi] is in place
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def partition(arr, high, low):
    pivot = arr[high]       # taken last element as pivot
    i=low-1

    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print(arr)

