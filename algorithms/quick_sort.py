def partition(arr, left, right):
    pivot = arr[right]

    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]
    
    return i + 1


def quick_sort(arr, left, right):
    print(arr)
    
    if left < right:
        pi = partition(arr,left,right)
        quick_sort(arr, left, pi-1)
        quick_sort(arr,pi+1, right)


array = [2,4,3,7,9,12,5,1]

quick_sort(array, 0, len(array) - 1)

print(array)