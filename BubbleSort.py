import time
from tkinter import *
from tkinter import messagebox
import threading

def bubbleSort(array, drawBars, speed):
    
    # Color Array
    colorArray = []
    for _ in range(len(array)):
        colorArray.append("red")

    n = len(array)
    for i in range(n-1):
        for j in range(n-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

                # Change color affected bars to blue
                colorArray[j] = "blue"
                colorArray[j+1] = "blue"

                # Redraw Bars
                drawBars(array, colorArray)

                # Undo changes made to color of bars
                colorArray[j] = "red"
                colorArray[j+1] = "red"

                # Pause
                time.sleep(speed)
        colorArray[n-i-1] = "green"

    # Sorting completed

    # Color Array
    colorArray = []
    for _ in range(len(array)):
        colorArray.append("green")

    # Show sorted Array
    drawBars(array, colorArray)

def startBubbleSort(array, drawBars, speed):

    info = """
        Bubble Sort

        Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

        In each pass largest element bubbles up to its correct position

        Visualization

        Bars which are being swapped are colored BLUE
        Bars which are sorted are colored GREEN
    """

    messagebox.showinfo(title="Bubble Sort", message=info)

    threading.Thread(target=bubbleSort, args=(array, drawBars, speed)).start()
    # bubbleSort(array, drawBars, speed)
