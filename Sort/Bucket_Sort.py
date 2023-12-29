from Selection_Sort import selectionSort
def BucketSort(array):
    maxVal = max(array)
    minVal = min(array)
    
    bucketRange = (maxVal - minVal) / len(array)
    
    bucket = [[]for i in range(len(array))]
    
    for n in array:
        index = int((n - minVal) / bucketRange)
        bucket[index].append(n)
        
    for i in range(len(bucket)):
        selectionSort(bucket[i])
        
    sortedArray = [n for finalBucket in bucket for n in finalBucket]
    
    return sortedArray

if __name__ == "__main__":
    unsortedArray = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", unsortedArray)

    sortedArray = BucketSort(unsortedArray)

    print("Sorted array:", sortedArray)