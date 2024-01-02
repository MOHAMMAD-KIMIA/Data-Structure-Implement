def countingSort(array):
    # Find the minimum and maximum values in the array
    minVal = min(array)
    maxVal = max(array)
    
    # Create a count array to store the count of each element
    count = [0] * (maxVal - minVal + 1)
    
    # Count the occurrences of each element in the input array
    for n in array:
        # Adjust the index to be within the range of the count array
        count[n - minVal] += 1
    
    # Modify the count array to store the cumulative sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    # Create an output array to store the sorted elements
    outArr = [0] * len(array)
    
    # Build the sorted array using the count array
    for n in array:
        # Find the correct position for the current element in the output array
        position = count[n - minVal] - 1
        outArr[position] = n
        
        # Update the count array to reflect the placement of the current element
        count[n - minVal] -= 1
    
    return outArr