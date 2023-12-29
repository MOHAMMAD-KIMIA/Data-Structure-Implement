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
            
if __name__ == "__main__":
    unsorted_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", unsorted_array)

    mergeSort(unsorted_array)

    print("Sorted array:", unsorted_array)