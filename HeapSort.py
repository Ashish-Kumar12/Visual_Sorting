import time
from tkinter import *
from tkinter import messagebox
import threading

# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(array, n, i, drawBars, speed, stopIndex): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1	 # left = 2*i + 1 
    r = 2 * i + 2	 # right = 2*i + 2 

    # See if left child of root exists and is 
    # greater than root 
    if l < n and array[i] < array[l]: 
        largest = l 

    # See if right child of root exists and is 
    # greater than root 
    if r < n and array[largest] < array[r]: 
        largest = r 

    # Change root, if needed 
    if largest != i: 
        array[i],array[largest] = array[largest],array[i] # swap 

        # Heapify rest
        drawBars(array, getColorArray(array, stopIndex, largest, i))
        time.sleep(speed)

        # Heapify the root. 
        heapify(array, n, largest, drawBars, speed, stopIndex) 

# The main function to sort an arrayay of given size 
def heapSort(array, drawBars, speed): 
    n = len(array) 

    # Build a maxheap. 
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    # range (start, stop, step)
    for i in range(n // 2 - 1, -1, -1): 
        heapify(array, n, i, drawBars, speed, stopIndex=n) 

    # One by one extract elements 
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i] # swap 

        # Last element is largest and sorted
        drawBars(array, getColorArray(array, i, 0, i))
        time.sleep(speed)

        heapify(array, i, 0, drawBars, speed, stopIndex=i) 

    drawBars(array, ["green" for _ in range(len(array))])

def getColorArray(array, stopIndex, swapIndex1, swapIndex2):
    colorArray = []

    for i in range(stopIndex):
        # Child node is yellow
        if i == swapIndex1:
            colorArray.append("yellow")
        # Parent node is pink
        elif i == swapIndex2:
            colorArray.append("pink")
        # Elements not into consideration are white
        else:
            colorArray.append("white")

    # Already sorted elements are green
    for i in range(stopIndex, len(array)):
        colorArray.append("green")

    return colorArray

def startHeapSort(array, drawBars, speed): 

    info = """
        Heap Sort

        Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining elements.

        Heap Sort Algorithm for sorting in increasing order:

        1. Build a max heap from the input data.
        2. At this point, the largest item is stored at the root of the heap. 
            Replace it with the last item of the heap followed by 
            reducing the size of heap by 1. Finally, heapify the root of the 
            tree.
        3. Repeat step 2 while size of heap is greater than 1.

        Visualization

        Child node is YELLOW
        Parent node is PINK
        Nodes not into consideration are WHITE
        Already sorted nodes are GREEN
    """

    messagebox.showinfo(title="Heap Sort", message=info)

    threading.Thread(target=heapSort, args=(array, drawBars, speed)).start()
    # heapSort(array, drawBars, speed)
