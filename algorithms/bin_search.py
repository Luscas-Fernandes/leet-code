ar1 = [14, 3, 89, 27, 65]

ar2 = [42, 7, 91, 18, 33, 56]

ar3 = [5, 72, 11, 94, 38, 60, 2]

ar4 = [99, 24, 17, 8, 73, 41, 6, 52]

ar5 = [30, 4, 88, 12, 57]


def binSearchRecursive(ordered_array: list[int], search_element: int) -> bool:
    arraySize = len(ordered_array)

    array_half = arraySize // 2

    if not arraySize:
        return False

    if search_element == ordered_array[array_half]: 
        return True

    elif search_element > ordered_array[array_half]:
        return binSearchRecursive(ordered_array[(array_half + 1)::], search_element)
    else:
        return binSearchRecursive(ordered_array[0:array_half:], search_element)
    

def binSearch(ordered_array: list[int], search_element: int) -> bool:
    pass

    
sortedArray = ar4.sort()
print(ar4)
finding = binSearchRecursive(ar4, 24)
print(finding)