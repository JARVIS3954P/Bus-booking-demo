from tkinter import *

root = Tk()
h, w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0' % (w, h))

bus = PhotoImage(file='.//Bus_for_project.png')

fr1 = Frame(root)
fr1.grid(row=0, column=0, columnspan=10)

fr2 = Frame(root)
fr2.grid(row=1, column=0, columnspan=10)

fr3 = Frame(root)
fr3.grid(row=2, column=0, columnspan=10)

fr4=Frame(root)
fr4.grid(row=3, column=0, columnspan=10)

Label(fr1, image=bus).grid(row=0, column=0, padx=w // 2.4)

Label(fr2, text="Online Bus Booking System", font='arial 30 bold', fg="Red", bg="Light Blue").grid(row=1, column=2, pady=20)

Label(fr3, text="Enter Journey Details", font='arial 16 bold', fg="green4", bg="green2").grid(row=0, column=2)

# Input boxes
to_label = Label(fr3, text="To")
to_label.grid(row=1, column=1, sticky='e')
to_entry = Entry(fr3)
to_entry.grid(row=1, column=2)

from_label = Label(fr3, text="From")
from_label.grid(row=2, column=1, sticky='e')
from_entry = Entry(fr3)
from_entry.grid(row=2, column=2)

journey_date_label = Label(fr3, text="Journey Date")
journey_date_label.grid(row=3, column=1, sticky='e')
journey_date_entry = Entry(fr3)
journey_date_entry.grid(row=3, column=2)
placeholder_label = Label(fr3, text="dd-mm-yyyy", fg="red")
placeholder_label.grid(row=4, column=2)

# Show Bus button
def show_bus():
    Label(fr4, text="Select Bus",font='arial 16 bold').grid(row=0,column=0)
    Label(fr4, text="Operator",font='arial 16 bold').grid(row=0,column=1)
    Label(fr4, text="Bus Type",font='arial 16 bold').grid(row=0,column=2)
    Label(fr4, text="Seat Available",font='arial 16 bold').grid(row=0,column=3)
    Label(fr4, text="Fare",font='arial 16 bold').grid(row=0,column=4)
    
    
show_bus_button = Button(fr3, text="Show Bus",font='arial 12 bold', bg="green2", fg="green4", command=show_bus)
show_bus_button.grid(row=5, column=2, pady=10)

# Home button
def go_home():
    root.destroy()
    import main
home_image = PhotoImage(file=r"C:\Users\ASUS\Desktop\CODES\Python\Bus Ticket System\home.png")
home_button = Button(fr3, image=home_image, command=go_home)
home_button.grid(row=5, column=3)

# Back button
def go_back():
    root.destroy()
    import book_or_edit
back_button = Button(fr3, text="Back", command=go_back)
back_button.grid(row=5, column=4)

root.mainloop()
