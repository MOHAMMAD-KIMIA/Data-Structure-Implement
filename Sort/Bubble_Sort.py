def bubbleSort(array):
    #traversing array
    for i in range(len(array)):
        #compare array elements
        #why(len(array - i))? each element in array that placed and be sorted one i minus from length of second for (i=0 means the first want to be sorted, i=1 means the second want to be sorted)
        #why(len(array - 1))? because of the comparisom between array's elements if we have 5 elements we have to compare 4 times
        for j in range(0, len(array)-i-1): 
            #if true change the place
            if array[j] > array[j+1]:
                
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            