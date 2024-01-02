def mergeSort(array):
    # Check if the array has more than one element
    if len(array) > 1:
        # Calculate the middle index
        mid = len(array) // 2

        # Divide the array into two halves
        left = array[:mid]
        right = array[mid:]

        # Recursively apply mergeSort to both halves
        mergeSort(left)
        mergeSort(right)

        # Merge the two sorted halves
        l = r = k = 0
        while l < len(left) and r < len(right):
            # Compare elements from both halves and merge them into the original array
            if left[l] < right[r]:
                array[k] = left[l]
                l += 1
            else:
                array[k] = right[r]
                r += 1
            k += 1

        # Check if there are any remaining elements in the left half
        while l < len(left):
            array[k] = left[l]
            l += 1
            k += 1

        # Check if there are any remaining elements in the right half
        while r < len(right):
            array[k] = right[r]
            r += 1
            k += 1