# import all the packages needed

import ttkbootstrap as ttk
import tkinter as Tk
import customtkinter as Ctk
#from tkinter import ttk



#convert commmand 

def convert():
    mile_input = entry_int.get()
    km_output= mile_input * 1.61
    output_string.set(str(km_output) + "Km")

#window
window = ttk.Window(themename= 'journal')

#Window Title 
window.title('Miles To Kilometers - Made By tahaes')

#window geometry
window.geometry('350x250')

#text/labels

title_label = ttk.Label(master = window, text = 'Miles To Kilometers', font = 'FiraCode, 22 bold' )
footer_label = ttk.Label(master = window,text = 'the easiest way to convert miles into kilometers', font = 'Calibri, 8 ' )
title_label.pack()
footer_label.pack()

# input field 

input_field = ttk.Frame(master = window )
entry_int= Tk.IntVar()
entry = ttk.Entry(master = input_field , textvariable= entry_int)
button = ttk.Button(master = input_field, text = 'Convert' ,command= convert)
input_field.pack()
entry.pack(side = 'left' , padx = 10)
button.pack(side = 'left', pady= 10)



#output label

output_string = Tk.StringVar()
output_label = ttk.Label(master = window , text = 'Output', font = 'Calibri, 22 bold', textvariable=output_string )
output_label.pack(pady = 12)

# credits field
credits_field= ttk.Label(master = window, text = 'Made By  @Tahaes', font = 'FiraCode, 6 bold' )
credits_field.pack(pady= 18)

#run
window.mainloop()