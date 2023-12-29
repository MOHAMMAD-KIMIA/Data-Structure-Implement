# Import the selectionSort function from the Selection_Sort module
from Selection_Sort import selectionSort

# Function to perform Bucket Sort on an array
def BucketSort(array):
    # Find the maximum and minimum values in the array
    maxVal = max(array)
    minVal = min(array)
    
    # Calculate the range of each bucket
    bucketRange = (maxVal - minVal) / len(array)
    
    # Create empty buckets (lists of lists)
    buckets = [[] for _ in range(len(array))]
    
    # Distribute elements into buckets
    for n in array:
        # Calculate the index of the bucket for the current element
        index = int((n - minVal) / bucketRange)
        # Append the element to the corresponding bucket
        buckets[index].append(n)
        
    # Sort each bucket using the selectionSort function
    for i in range(len(buckets)):
        selectionSort(buckets[i])
        
    # Concatenate the sorted buckets into the final sorted array
    sortedArray = [n for finalBucket in buckets for n in finalBucket]
    
    return sortedArray