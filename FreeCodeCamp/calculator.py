import tkinter as tk
import tkinter.ttk as ttk


win = tk.Tk()

win.title("Calculator")


Entry = ttk.Entry(win,justify='right')
Entry.grid(row=0,columnspan=4,sticky='nsew')

button_7 = ttk.Button(win,text='7')
button_7.grid(row=1,column=0)

button_8 = ttk.Button(win,text='8')
button_8.grid(row=1,column=1)

button_9 = ttk.Button(win,text='9')
button_9.grid(row=1,column=2)

button_d = ttk.Button(win,text='/')
button_d.grid(row=1,column=3)



button_6 = ttk.Button(win,text='6')
button_6.grid(row=2,column=2)

button_5 = ttk.Button(win,text='5')
button_5.grid(row=2,column=1)

button_4 = ttk.Button(win,text='4')
button_4.grid(row=2,column=0)

button_m = ttk.Button(win,text='*')
button_m.grid(row=2,column=3)


button_3 = ttk.Button(win,text='3')
button_3.grid(row=3,column=2)

button_2 = ttk.Button(win,text='2')
button_2.grid(row=3,column=1)

button_1 = ttk.Button(win,text='1')
button_1.grid(row=3,column=0)

button_s = ttk.Button(win,text='-')
button_s.grid(row=3,column=3)



button_0 = ttk.Button(win,text='0')
button_0.grid(row=4,column=0)

button_dot = ttk.Button(win,text='.')
button_dot.grid(row=4,column=1)

button_c = ttk.Button(win,text='c')
button_c.grid(row=4,column=2)

button_a = ttk.Button(win,text='+')
button_a.grid(row=4,column=3)

button_e = ttk.Button(win,text='=')
button_e.grid(row=5,columnspan=4,sticky='nsew')


win.mainloop()