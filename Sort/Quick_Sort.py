def quicksort(arr):
    # Base case: if the array has 1 or fewer elements, it is already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose the first element as the firstOf
        firstOf = arr[0]
        
        # Partition the array into two subarrays: elements <= firstOf and elements > firstOf
        less = [x for x in arr[1:] if x <= firstOf]
        greater = [x for x in arr[1:] if x > firstOf]
        
        # Recursively apply quicksort to the subarrays and concatenate the results
        return quicksort(less) + [firstOf] + quicksort(greater)