import tkinter as tk
from tkinter import font
import time
from Adafruit_IO import Client


ApiKey = "fbdeb00ffbd747cea31dabfa326261ad"
UserId = "farhanf1"


aio = Client(UserId, ApiKey)
try:
	print("Initialising Feeds, please wait..!!")
	one = aio.feeds('one')
	print("Connected to One")
	two = aio.feeds('two')
	print("Connected to Two")
	three = aio.feeds('three')
	print("Connected to Three")
	four = aio.feeds('four')
	print("Connected to Four")
except:
	print("Error Occured..!!")
	exit()

def adafruit():
	try:
		alpha()
	except KeyboardInterrupt:
		print("exiting.........")
		exit()
	#time.sleep(.998)
	#adafruit()
	#root.after(1000,adafruit)

def alpha():
	data1 = aio.receive(one.key)
	button['text'] = "Connected"
	if str(data1.value) == "OFF":
		print("One is OFF")
		label1['text'] = "OFF"
		label1['image'] = bg1
	elif str(data1.value) == "ON":
		print("One is ON")
		label1['text'] = "ON"
		label1['image'] = bg2
	#beta()
	root.after(100,beta)



def beta():
	data2 = aio.receive(two.key)
	if str(data2.value) == "OFF":
		print("Two is OFF")
		label2['text'] = "OFF"
		label2['image'] = bg1
	elif str(data2.value) == "ON":
		print("Two is ON")
		label2['text'] = "ON"
		label2['image'] = bg2
	#charlie()
	root.after(100,charlie)




def charlie():
	data3 = aio.receive(three.key)
	if str(data3.value) == "OFF":
		print("Three is OFF")
		label3['text'] = "OFF"
		label3['image'] = bg1
	elif str(data3.value) == "ON":
		print("Three is ON")
		label3['text'] = "ON"
		label3['image'] = bg2
	#delta()
	root.after(100,delta)



def delta():
	data4 = aio.receive(four.key)
	if str(data4.value) == "OFF":
		print("Four is OFF")
		label4['text'] = "OFF"
		label4['image'] = bg1
	elif str(data4.value) == "ON":
		print("Four is ON")
		label4['text'] = "ON"
		label4['image'] = bg2
	root.after(100,alpha)



canvas_height = 600
canvas_width = 800

root = tk.Tk()

bg2 = tk.PhotoImage(file = '1.png')
bg1 = tk.PhotoImage(file = '2.png')


canvas = tk.Canvas(root, height = canvas_height, width = canvas_width)
canvas.pack()

frame_1 = tk.Frame(canvas, bg = "red")
frame_1.place(relx = .01, rely = .01, relwidth = .48, relheight = .48)
#frame_1.pack()

frame_2 = tk.Frame(canvas, bg = "blue")
frame_2.place(relx = .51, rely = .01, relwidth = .48, relheight = .48)
#frame_2.pack()

frame_3 = tk.Frame(canvas, bg = "green")
frame_3.place(relx = .01, rely = .51, relwidth = .48, relheight = .48)
#frame_3.pack()

frame_4 = tk.Frame(canvas, bg = "yellow")
frame_4.place(relx = .51, rely = .51, relwidth = .48, relheight = .48)
#frame_4.pack()


label1 = tk.Label(frame_1, text = "Click Get Status", font = ('calibri', 20))
#label1.place(anchor = 'n', relx = .5, rely = .4)
label1.pack()

label2 = tk.Label(frame_2, text = "Click Get Status", font = ('calibri', 20))
#label2.place(anchor = 'n', relx = .5, rely = .4)
label2.pack()

label3 = tk.Label(frame_3, text = "Click Get Status", font = ('calibri', 20))
#label3.place(anchor = 'n', relx = .5, rely = .4)
label3.pack()

label4 = tk.Label(frame_4, text = "Click Get Status", font = ('calibri', 20))
#label4.place(anchor = 'n', relx = .5, rely = .4)
label4.pack()

button = tk.Button(canvas, command =lambda:alpha(), text = 'Get Status', font = ("TimesNewRoman",18))
button.place(anchor = 's', relx = .5, rely = 1)

root.mainloop()