from tkinter import *

window = Tk()
window.title("Invoice Generator")

medicine_label = Label(window, text="Medicine: ")
medicine_label.pack()

medicine_listbox = Listbox(window, selectmode=SINGLE)
medicine_listbox.pack()

quantity_label = Label(window, text="Quantity")
quantity_label.pack()
quantity_entry = Entry(window)
quantity_entry.pack()

window.mainloop()
