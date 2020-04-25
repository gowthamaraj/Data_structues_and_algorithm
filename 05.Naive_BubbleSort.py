def bubbleSort(arr):
    l = len(arr)-1;

    for i in range(l-1):
        for j in range(l-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j];


#test
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)