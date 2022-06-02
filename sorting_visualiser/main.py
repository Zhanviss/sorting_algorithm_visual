from tkinter import *
from tkinter import ttk
import random 
from colors import *
from algorithms.bubbleSort import bubble_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
#Creating window

window = Tk()
window.title("Sorting Algorithm")
window.maxsize(1000, 700)
window.config(bg=WHITE)

algorithm_name = StringVar()
#Selecting Algorithm to Use
algo_list = ['Bubble Sort', 'Merge Sort', 'Quick Sort']

speed_name = StringVar()
#Selecting Speed
speed_list = ['Fast', 'Normal', 'Slow']

data = []

#Drawing Graph according on Data 
def drawData(data, colorArray):
	canvas.delete("all")
	canvas_width = 800
	canvas_height = 400
	x_width = canvas_width/(len(data)+1)
	offset = 4
	spacing = 2
	normalizedData = [i/max(data) for i in data]

	for i,height in enumerate(normalizedData):
		x0 = i*x_width + offset +spacing
		x1 = (i+1) * x_width + offset
		y0 = canvas_height - height * 390
		y1 = canvas_height
		canvas.create_rectangle(x0,y0,x1,y1, fill=colorArray[i])

	window.update_idletasks()

#Generating List of random values of Data
def generate():
	global data 
	data = []

	for i in range(0, 100):
		random_value = random.randint(1, 200)
		data.append(random_value)

	drawData(data, [BLUE for x in range(len(data))])


#Setting Speed Function
def set_speed():
	if menu_speed.get()=='Slow':
		return 0.3
	elif menu_speed.get()=='Normal':
		return 0.1
	else:
		return 0.001

#Sorting Function
def sort():
	global data 
	timeTick = set_speed()
	if menu_algo.get()=='Bubble Sort':
		bubble_sort(data, drawData, timeTick)
	elif menu_algo.get()=='Merge Sort':
		merge_sort(data, 0, len(data)-1, drawData, timeTick)
	elif menu_algo.get()=='Quick Sort':
		quick_sort(data, 0, len(data)-1, drawData, timeTick)

#Setting Up UI
UI_Frame = Frame(window, width=900, height=300, bg= WHITE)
UI_Frame.grid(row=0, column=0, padx=10, pady=5)

#Choices for Sorting Algorithm
label1 = Label(UI_Frame, text= "Algorithm to Sort:", bg=WHITE)
label1.grid(row=0, column=0, padx=5, pady=5)
menu_algo = ttk.Combobox(UI_Frame, textvariable=algorithm_name, values=algo_list)
menu_algo.grid(row=0, column=1, padx=5, pady=5)
menu_algo.current(0)

#Choices for Speed of Sorting Algorithm
label2 = Label(UI_Frame, text= "Speed for Sorting:", bg=WHITE)
label2.grid(row=1, column=0, padx=5, pady=5)
menu_speed = ttk.Combobox(UI_Frame, textvariable=speed_name, values=speed_list)
menu_speed.grid(row=1, column=1, padx=5, pady=5)
menu_speed.current(0)

#Button for Sorting
button_1 = Button(UI_Frame, text="Sort", command = sort, bg= LIGHT_GRAY)
button_1.grid(row=2, column=1, padx=5, pady=5)

#Button for Generating List of Values
button_2 = Button(UI_Frame, text="Generate List", command = generate, bg= LIGHT_GRAY)
button_2.grid(row=2, column=0, padx=5, pady=5)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()