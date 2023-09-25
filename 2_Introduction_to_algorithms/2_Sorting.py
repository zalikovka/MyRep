def insertionSort(n):
    '''Insertion sort in ancending order'''
    for i in range(len(n)):
        #compare with a key element every element from right to left 
        for j in range(i, 0, -1):
            if n[j-1] > n[j]:
                #swap elements of array
                (n[j], n[j-1]) = (n[j-1], n[j])
    return n


def insertionSortReversed(n):
    '''Insertion sort in descending order'''
    for i in range(len(n)):
        for j in range(i, 0, -1):
            if n[j-1] < n[j]:
                (n[j], n[j-1]) = (n[j-1], n[j])
    return n


def selectionSort(n):
    '''Selection sort in ancending order'''
    length = len(n)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            # select the minimum element in every iteration
            if n[j] < n[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (n[i], n[min_index]) = (n[min_index], n[i])
    return n

def selectionSortReversed(n):
    '''Selection sort in descending order'''
    length = len(n)
    for i in range(length):
        max_index = i
        for j in range(i + 1, length):
            # select the minimum element in every iteration
            if n[j] > n[max_index]:
                max_index = j
         # swapping the elements to sort the array
        (n[i], n[max_index]) = (n[max_index], n[i])
    return n


def bubbleSort(n):
    length = len(n)
    swapped = False
    for i in range(length-1):
        for j in range(0, length-i-1):
             # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            if n[j] > n[j + 1]:
                swapped = True
                n[j], n[j + 1] = n[j + 1], n[j]
        if not swapped:
            return n
    return n


def bubbleSortReversed(array):
    length = len(array)
    swapped = False
    for i in range(length-1):
        for j in range(0, length-i-1):
            # traverse the array from 0 to n-i-1
            # swap if the element found is greater
            if array[j] < array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            return array
    return array


def mergeSort(array):
    if len(array) > 1:
        #  m is the point where the array is divided into two subarrays
        m = len(array)//2
        L = array[:m]
        R = array[m:]
        # Sort two halves
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    return array


def mergeSortReversed(array):
    if len(array) > 1:
        #  m is the point where the array is divided into two subarrays
        m = len(array)//2
        L = array[:m]
        R = array[m:]
        # Sort two halves
        mergeSortReversed(L)
        mergeSortReversed(R)
        i = j = k = 0
        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    return array

array = [9, 2, 4, 6, 1, 3, 6, 1]
print('insertionSort', insertionSort(array))
print('insertionSortReversed', insertionSortReversed(array))
print('selectionSort', selectionSort(array))
print('selectionSortReversed', selectionSortReversed(array))
print('bubbleSort', bubbleSort(array))
print('bubbleSortReversed', bubbleSortReversed(array))
print('mergeSort', mergeSort(array))
print('mergeSortReversed', mergeSortReversed(array))


