import time
from tkinter import *
from tkinter import messagebox
import threading

# Merges two subarrays of array[]. 
# First subarray (left part) is array[left..middle+1] 
# Second subarray (right part) is array[middle+1..right+1] 
def merge(array, left, middle, right, drawBars, speed):
    arrayLen = len(array)

    
    drawBars(array, getColorArray(arrayLen, left, middle, right))
    time.sleep(speed)

    # create temp arrays and copy data
    leftPart = array[left : middle+1]
    rightPart = array[middle+1 : right+1]

    leftIndex = 0
    rightIndex = 0

    for arrayIndex in range(left, right+1):

        # Merge temp arrays back into original array
        if leftIndex < len(leftPart) and rightIndex < len(rightPart):
            if leftPart[leftIndex] <= rightPart[rightIndex]:
                array[arrayIndex] = leftPart[leftIndex]
                leftIndex += 1
            else:
                array[arrayIndex] = rightPart[rightIndex]
                rightIndex += 1

        # Copy remaining elements of left part if there are any
        elif leftIndex < len(leftPart):
            array[arrayIndex] = leftPart[leftIndex]
            leftIndex += 1
        
        # Copy remaining elements of right part if there are any
        elif rightIndex < len(rightPart):
            array[arrayIndex] = rightPart[rightIndex]
            rightIndex += 1

    # Sorting of subpart done
    drawBars(array, ["green" if left <= x <= right else "white" for x in range(arrayLen)])
    time.sleep(speed)


def mergeSort(array, left, right, drawBars, speed):
    
    if left < right:
        arrayLen = len(array)
        middle = (left + right)//2

        # Left part
        mergeSort(array, left, middle, drawBars, speed)

        # Right part
        mergeSort(array, middle+1, right, drawBars, speed)

        # Merge back
        merge(array, left, middle, right, drawBars, speed)


def getColorArray(arrayLen, left, middle, right):
    colorArray = []

    for i in range(arrayLen):
        
        # Base Coloring
        # Part of array which is into consideration
        if i >= left and i <= right:
            # Left subarray is yellow
            if i <= middle:
                colorArray.append("yellow")
            
            # Right subarray is pink
            else:
                colorArray.append("pink")

        # Part of array which is not into consideration is white
        else:
            colorArray.append("white")

    return colorArray

def startMergeSort(array, left, right, drawBars, speed):

    info = """
        Merge Sort

        Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. 
        
        The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

        Visualization

        Part of array which is into consideration
            Left subarray is YELLOW
            Right subarray is PINK
        
        Part of array which is not into consideration is WHITE
    """

    messagebox.showinfo(title="Merge Sort", message=info)

    threading.Thread(target=mergeSort, args=(array, left, right, drawBars, speed)).start()
    # mergeSort(array, left, right, drawBars, speed)
