#!/usr/bin/env python3
"""
The 'Bubble Sort' algorithm starts at the beginning of a list and compares
pairs of items as it moves towards the end. If the pairs are out of order it 
performs a swap. Gradually the largest items 'bubble' to the end while the
smallest move to the beginning.

Bubble sort has a time complexity of O(n^2) because of the double while loops.
"""


def bubble_sort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i-1]:
                lyst[i], lyst[i-1] = lyst[i-1], lyst[i]
            i += 1
        n -= 1
    return lyst

def better_bubble_sort(lyst):
    """Improves on bubble sort by returning the list if there are no swaps 
    during one outer loop. Improves best case time complexity to O(n)"""
    n = len(lyst)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            if lyst[i] < lyst[i-1]:
                lyst[i], lyst[i-1] = lyst[i-1], lyst[i]
                swapped = True
            i += 1
        if swapped == False:
            return lyst
        n -= 1
    return lyst


if __name__ == '__main__':
    import random
    #print(bubble_sort([8,5,9,2,7,1,3,15,22]))
    # print(better_bubble_sort([1,3,2,5,7,9,15,22]))
    print(bubble_sort(random.sample(range(100_000), 2000)))