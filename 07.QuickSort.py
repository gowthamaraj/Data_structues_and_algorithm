def quicksort(array,l,h):
    if(l<h):
        pivot = sort(array,l,h)
        quicksort(array,l,pivot-1)
        quicksort(array,pivot+1,h)

def sort(array,l,h):
    pivot = h;
    i=0;
    while i+l<=pivot:
        if array[i+l] > array[pivot]:
            array[pivot-1],array[pivot] = array[pivot],array[pivot-1];
            if((pivot-(i+l)) != 1):
                array[i+l], array[pivot] = array[pivot], array[i+l];
            pivot -= 1; 
        else:
            i+=1;
    return pivot;


#test
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quicksort(test,0,len(test)-1)

