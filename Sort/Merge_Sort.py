def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        l=r=k=0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                array[k] = left[l]
                l += 1
            else:
                array[k] = right[r]
                r += 1
            k += 1
                
        while l < len(left):
            array[k] = left[l]
            l += 1
            k += 1
            
        while r < len(right):
            array[k] = right[r]
            r += 1
            k += 1