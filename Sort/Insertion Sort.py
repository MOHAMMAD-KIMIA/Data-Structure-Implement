def insertionSort(array):
    #traverse the array
    for i in range(1, len(array)):
        #start from the index = 1
        val = array[i]
        #declare the j to one index before i 
        j = i-1
        #if array[j] is not greater than val(array[i]) while does not run and we put val in array[i]
        #else if array[j] is greater than val(array[i]) we swap the elments
        while j>=0 and val<array[j]:
            array[j+1] = array[j]
            j-=1
        
        #val is the operator that we need to save the value of index i
        array[j+1] = val