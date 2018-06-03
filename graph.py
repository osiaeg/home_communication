from tkinter import *
import math 

root = Tk()
root.title('Построение графика функции y = sin(x)')
root.geometry("1320x640")

canvas = Canvas(root, width = 1040, height = 640, bg = '#002')
canvas.pack(side='right')

# линии сетки для вертикали 
for y in range(21):
	k = 50 * y 
	canvas.create_line(20+k, 620, 20+k, 20, width = 1, fill = '#191938')

# линии сетки по горизонтали
for x in range(13):
	k = 50 * x 
	canvas.create_line(20, 20+k, 1020, k+20, width = 1, fill = '#191938')

# линии координат X и Y
canvas.create_line(20, 20, 20, 620, width =  1, arrow = FIRST, fill = '#FFF') # ось Y
canvas.create_line(1020, 320, 20, 320, width = 1, arrow = FIRST, fill = '#FFF') # ось X

canvas.create_text(20, 10, text='300', fill= 'white')
canvas.create_text(20, 630, text='-300', fill= 'white')
canvas.create_text(10, 310, text='0', fill= 'white')
canvas.create_text(1015, 310, text='1000', fill= 'white')

label_w = Label(root, text = 'Циклическая частота: ')
label_w.place(x = 0, y = 10)
label_phi = Label(root, text = 'Смещение графика по X: ')
label_phi.place(x = 0, y = 35)
label_A = Label(root, text = 'Амплитуда: ')
label_A.place(x = 0, y = 60)
label_dy = Label(root, text = 'Смещение графика по Y: ')
label_dy.place(x = 0, y = 85)

entry_w = Entry(root)
entry_w.place(x =  160, y = 10, width = 115)
entry_phi = Entry(root)
entry_phi.place(x =  160, y = 35, width = 115)
entry_A = Entry(root)
entry_A.place(x =  160, y = 60, width = 115)
entry_dy = Entry(root)
entry_dy.place(x =  160, y = 85, width = 115)

# w = 0.0209 # циклическая частота 
# phi = 10 # смещение графика по X
# A = 100 #  Амплитуда
# dy = 310 # смещение графика по Y

def sinus(w, phi, A, dy):
	global sin 
	sin = 0
	xy = []
	for x in range(1000):
		y = math.sin(x * w)
		xy.append(x + phi)
		xy.append(y * A + dy)
	sin = canvas.create_line(xy, fill = 'blue')

def clean():
	canvas.delete(sin)	

btn_calc = Button(root, text = 'Рассчитать')
btn_calc.bind('<Button-1>', lambda event: sinus(float(entry_w.get()), float(entry_phi.get()), float(entry_A.get()), float(entry_dy.get())))
btn_calc.place(x = 10, y = 115)

btn_clean = Button(root, text = 'Отчистить график')
btn_clean.bind('<Button-1>', lambda event: clean())
btn_clean.place(x = 130, y = 115)


root.mainloop()

