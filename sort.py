from tkinter import *
from tkinter import ttk, messagebox
import random
from BubbleSort import startBubbleSort
from InsertionSort import startInsertionSort
from SelectionSort import startSelectionSort
from QuickSort import startQuickSort
from MergeSort import startMergeSort
from HeapSort import startHeapSort

root = Tk()
root.title("Visual Sort")
root.maxsize(900, 600)
root.config(bg="black")

# Variables
canvasHeight = 380
canvasWidth = 600
minValueOfBars = 1
avgValueOfBars = 50
maxValueOfBars = 100
maxNoOfBars = 20
minNoOfBars = 3

# Array of numbers
array = []

# Sorting Algos List
sorts = [
    "Bubble Sort",
    "Insertion Sort",
    "Selection Sort",
    "Quick Sort",
    "Merge Sort",
    "Heap Sort"
    ]

# Tkinter Variables
selectedSort = StringVar()
selectedSort.set(sorts[0])

# Command Functions

def drawBars(array, colorArray):
    global canvasHeight
    global canvasWidth

    barWidth = canvasWidth / (len(array) + 1)
    XoffSet = barWidth/2
    barsSpacing = 10

    # Modify bars height to be relative to canvas height
    normalizedData = [ i/max(array) for i in array]

    # Clear previous bars
    canvas.delete("all")

    for i, height in enumerate(normalizedData):
        # Top Left Corner
        x0 = i * barWidth + XoffSet + barsSpacing
        y0 = canvasHeight - height*(canvasHeight-40)

        # Bottom right Corner
        x1 = (i+1) * barWidth + XoffSet
        y1 = canvasHeight

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+5, y0, text=str(array[i]), anchor=SW)

    root.update_idletasks()

def generateArray():
    global array

    # Input Data
    minVal = minValueScale.get()
    maxVal = maxValueScale.get()
    noOfBars = barsScale.get()

    # Generate Random Array
    array = []
    colorArray = []
    for _ in range(noOfBars):
        array.append(random.randrange(minVal, maxVal+1))
        colorArray.append("red")

    drawBars(array, colorArray)

def startSort():
    global array

    # No array to sort
    if not array:
        return

    # Call Sorting Algos
    print("Sorting Algo Selected : " + selectedSort.get())
    
    if selectedSort.get() == "Bubble Sort":
        startBubbleSort(array, drawBars, speedScale.get())
    elif selectedSort.get() == "Insertion Sort":
        startInsertionSort(array, drawBars, speedScale.get())
    elif selectedSort.get() == "Selection Sort":
        startSelectionSort(array, drawBars, speedScale.get())
    elif selectedSort.get() == "Quick Sort":
        startQuickSort(array, 0, len(array)-1, drawBars, speedScale.get())
    elif selectedSort.get() == "Merge Sort":
        startMergeSort(array, 0, len(array)-1, drawBars, speedScale.get())
    elif selectedSort.get() == "Heap Sort":
        startHeapSort(array, drawBars, speedScale.get())

    # Sorting Done
    drawBars(array, ["green" for _ in range(len(array))])

    # messagebox.showinfo(title="Completion message", message="Done Sorting!!!")

# User UI Frame
UIframe = Frame(root, width=600, height=200, bg="gray")
UIframe.grid(row=0, column=0, padx=10, pady=5)

# Canvas Frame for bars
canvas = Canvas(root, width=canvasWidth, height=canvasHeight, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# Options for User / UI Frame Options
# Row 0
algoLabel = Label(UIframe, text="Algorithms ", bg="gray")
algoLabel.grid(row=0, column=0, padx=5, pady=5, sticky=W)

algoMenu = ttk.Combobox(UIframe, textvariable=selectedSort, values = sorts)
algoMenu.grid(row=0, column=1, padx=5, pady=5)

speedScale = Scale(UIframe, label="Speed (in seconds)", from_=0.1, to=2.0, orient=HORIZONTAL, length=200, resolution=0.2) # digits = 2
speedScale.grid(row=0, column=2, padx=5, pady=5)

startBtn = Button(UIframe, text="Start Sorting", command=startSort)
startBtn.grid(row=0, column=3, padx=5, pady=5)

# Row 1
barsScale = Scale(UIframe, label="No of Bars", from_=minNoOfBars, to=maxNoOfBars, resolution=1, orient=HORIZONTAL)
barsScale.grid(row=1, column=0, padx=5, pady=5)

minValueScale = Scale(UIframe, label="Min Value", from_=minValueOfBars, to=avgValueOfBars, resolution=1, orient=HORIZONTAL)
minValueScale.grid(row=1, column=1, padx=5, pady=5)

maxValueScale = Scale(UIframe, label="Max Value", from_=avgValueOfBars, to=maxValueOfBars, resolution=1, orient=HORIZONTAL)
maxValueScale.grid(row=1, column=2, padx=5, pady=5)

generateBtn = Button(UIframe, text="Array Generate", command=generateArray)
generateBtn.grid(row=1, column=3, padx=5, pady=5)

generateArray()

root.mainloop()
