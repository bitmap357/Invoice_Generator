from tkinter import *

window = Tk()
window.title("Invoice Generator")

medicine_label = Label(window, text="Medicine: ")
medicine_label.pack()

medicine_listbox = Listbox(window, selectmode=SINGLE)
medicine_listbox.pack()

quantity_entry = Entry(window)
quantity_entry.pack()

window.mainloop()
