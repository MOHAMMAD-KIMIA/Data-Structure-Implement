def selectionSort(array):
    #traverse the array
    for i in range(len(array)):
        minValue = i #min value should places in the first index
        for j in range(i+1, len(array)): #compare the first elemnts with other elements
            if array[minValue] > array[j]: #compare the elements with each other and find min value
                minValue = j
                
        array[i] , array[minValue] =  array[minValue] , array[i] #swap the min value and the element's with the min available index