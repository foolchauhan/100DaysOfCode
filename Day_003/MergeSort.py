# arr = [22, 11, 45, 65, 23, 4, 8, 31]

# L = arr[0:4]
# print(L)

def merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m

    L = arr[l:m+1]
    R = arr[m+1:r+1]

    i, j, k = 0, 0, l

    while i<n1 and j<n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    
    while i<n1 and k<len(arr):
        arr[k] = L[i]
        k+=1
        i+=1
    
    while j<n2 and k<len(arr):
        arr[k] = R[j]
        k+=1
        j+=1

def mergeSort(arr, l, r):
    if l<r:
        m=int((l+r)/2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
mergeSort(arr,0,n-1)
print(arr)

