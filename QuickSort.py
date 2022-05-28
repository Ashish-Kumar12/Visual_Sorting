import time
from tkinter import *
from tkinter import messagebox
import threading

def partition(array, head, tail, drawBars, speed):

    # This function takes last element as pivot, places 
    # the pivot element at its correct position in sorted 
    # array, and places all smaller (smaller than pivot) 
    # to left of pivot and all greater elements to right 
    # of pivot 
    
    border = head             # Index of smaller element
    pivot = array[tail]       # Pivot element
    arrayLen = len(array)     # Len of array

    # Show current Pivot, Head, Tail, Border and Current Element
    drawBars(array, getColorArray(arrayLen, head, tail, border, border, False))
    time.sleep(speed)

    for i in range(head, tail):
        # If current element is smaller than pivot 
        if array[i] < pivot:

            # Show Swapping of Border element and Current element
            drawBars(array, getColorArray(arrayLen, head, tail, border, i, True))
            time.sleep(speed)

            # Swap elements and increment index of smaller element 
            array[border], array[i] = array[i], array[border]
            border += 1

        # Show current element as yellow
        drawBars(array, getColorArray(arrayLen, head, tail, border, i, False))
        time.sleep(speed)

    # Swap pivot with border value
    array[border], array[tail] = array[tail], array[border]

    # Show swapping of pivot and border element
    drawBars(array, getColorArray(arrayLen, head, tail, border, tail, True))
    time.sleep(speed)

    # Return border index and pivot is now at correct position
    return border


def quickSort(array, head, tail, drawBars, speed):

    if head < tail:
        # partitionIndex is partitioning index, array[partitionIndex] is now 
        # at right place 

        partitionIndex = partition(array, head, tail, drawBars, speed)

        # Separately sort elements before partition and after partition 

        # Left partition 
        quickSort(array, head, partitionIndex-1, drawBars, speed)

        # Right partition
        quickSort(array, partitionIndex+1, tail, drawBars, speed)
    else :

        # Sorting Done
        drawBars(array, ["green" for _ in range(len(array))])

def getColorArray(arrayLen, head, tail, border, currentIndex, isSwapping):

    colorArray = []

    for i in range(arrayLen):

        # Base coloring 
        # Part of array under consideration is gray else is white
        if i >= head and i <= tail:
            colorArray.append("gray")
        else:
            colorArray.append("white")

        # Tail is blue
        if i == tail:
            colorArray[i] = "blue"
        # Border element is red
        elif i == border:
            colorArray[i] = "red"
        # Current element is yellow
        elif i == currentIndex:
            colorArray[i] = "yellow"

        # Elements to be swapped are green
        if isSwapping == True:
            if i == border or i == currentIndex:
                colorArray[i] = "green"

    return colorArray

def startQuickSort(array, head, tail, drawBars, speed):

    info = """
        Quick Sort

        QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.

        The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

        Visualization

        Part of array under consideration is GRAY else is WHITE
        Tail is colored BLUE
        Border bar is colored RED
        Current bar is YELLOW
        Bars to be swapped are GREEN
    """

    messagebox.showinfo(title="Quick Sort", message=info)

    threading.Thread(target=quickSort, args=(array, head, tail, drawBars, speed)).start()
    # quickSort(array, head, tail, drawBars, speed)
