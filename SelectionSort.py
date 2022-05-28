import time
from tkinter import *
from tkinter import messagebox
import threading

def selectionSort(array, drawBars, speed):
	n = len(array)

	# Color Array (Unsorted Array)
	colorArray = []
	for _ in range(n):
		colorArray.append("red")

	# Traverse through all array elements 
	for i in range(n): 
		
		# Find the minimum element in remaining 
		# unsorted array 
		min_idx = i 

		# Min bar is Blue Bar
		colorArray[min_idx] = "blue"

		for j in range(i+1, n): 
			# Current bar is yellow
			colorArray[j] = "yellow"

			if array[min_idx] > array[j]: 
				# Update previous min bar to red
				colorArray[min_idx] = "red"
				min_idx = j 

			# Update new min bar to blue
			colorArray[min_idx] = "blue"
			drawBars(array, colorArray)
			time.sleep(speed)

			# Change current bar back to red
			colorArray[j] = "red"
				
		# Swap the found minimum element with 
		# the first element		 
		array[i], array[min_idx] = array[min_idx], array[i] 

		colorArray[min_idx] = "red"
		colorArray[i] = "green"
		drawBars(array, colorArray)
		time.sleep(speed)


	# Sorting completed
	# Color Array (Sorted Array)
	colorArray = []
	for _ in range(len(array)):
		colorArray.append("green")

	# Show sorted Array
	drawBars(array, colorArray)


def startSelectionSort(array, drawBars, speed):

	info = """
		Selection Sort

		The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

		1) The subarray which is already sorted.
		2) Remaining subarray which is unsorted.

		In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

		Visualization

		Bars which are being swapped are colored BLUE
		Bars which are sorted are colored GREEN
	"""

	messagebox.showinfo(title="Selection Sort", message=info)

	threading.Thread(target=selectionSort, args=(array, drawBars, speed)).start()
	# selectionSort(array, drawBars, speed)
