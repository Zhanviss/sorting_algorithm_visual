import time
from colors import *

def partition(data, low, high):
	pivot = data[high]

	i = low-1
	for j in range(low, high):
		if data[j] <= pivot:
			i += 1
			data[i], data[j] = data[j], data[i]

	data[i+1], data[high] = data[high], data[i+1]

	return i+1

def quick_sort(data, low, high, drawData, timeTick):
	if low<high:
		pi = partition(data, low, high)
		quick_sort(data, low, pi-1, drawData, timeTick)
		quick_sort(data, pi+1, high, drawData, timeTick)

		drawData(data, [BLACK if x>= low and x<pi else RED if x == pi else 
			DARK_BLUE if x>pi and x<=high else BLUE for x in range(len(data))])

		time.sleep(timeTick)
	drawData(data, [BLUE for x in range(len(data))])