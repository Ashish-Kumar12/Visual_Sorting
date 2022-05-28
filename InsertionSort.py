import time
from tkinter import *
from tkinter import messagebox
import threading

# Function to do insertion sort 
def insertionSort(array, drawBars, speed): 

    # Color Array
    colorArray = []
    for _ in range(len(array)):
        colorArray.append("red")

    n = len(array)
	# Traverse through 0 to len(array) 
    for i in range(0, n): 

        # Key / Current Bar
        key = array[i] 
        
        # Change color of key
        colorArray[i] = "yellow"
        drawBars(array, colorArray)
        time.sleep(speed)

        # Move elements of array[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < array[j] :             
            array[j+1] = array[j] 

            # Update array[j] to show key going downwards
            array[j] = key

            # Move Green Bar upwards and Yellow Bar downwards
            colorArray[j+1] = "green"
            colorArray[j] = "yellow"
            drawBars(array, colorArray)
            time.sleep(speed)

            j -= 1

        # Store Key to correct position
        array[j+1] = key

        # Key propagated to correct position
        colorArray[i] = "green"
        colorArray[j+1] = "green"
        drawBars(array, colorArray)
        time.sleep(speed)

    # Sorting completed

    # Color Array
    colorArray = []
    for _ in range(len(array)):
        colorArray.append("green")

    # Show sorted Array
    drawBars(array, colorArray)

def startInsertionSort(array, drawBars, speed):

    info = """
        Insertion Sort

        Algorithm

        To sort an array of size n in ascending order:
        1: Iterate from arr[1] to arr[n] over the array.
        2: Compare the current element (key) to its predecessor.
        3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

        Visualization
        
        Key is YELLOW
        Sorted Bars are GREEN
    """

    messagebox.showinfo(title="Insertion Sort", message=info)

    threading.Thread(target=insertionSort, args=(array, drawBars, speed)).start()
    # insertionSort(array, drawBars, speed)
