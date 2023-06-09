import tkinter as tk

def f_to_c():
    text = entry.get()
    label.config(text=(float(text)-32)*.556)

    # formule (x - 32)/1,8


def c_to_f():
    text = entry.get()
    label.config(text=(float(text)*1.8)+32) #Nesugalvoju kaip prideti C/F
    #formule x * 1.8 + 32

langas = tk.Tk()


entry = tk.Entry(langas)
entry.pack()


button1 = tk.Button(langas, text="Fahrenheit to Celsius", command=f_to_c)
button2 = tk.Button(langas, text="Celsius to Fahrenheit", command=c_to_f)


button1.pack(side=tk.TOP)
button2.pack(side=tk.BOTTOM)


label = tk.Label(langas)
label.pack()

langas.mainloop()
