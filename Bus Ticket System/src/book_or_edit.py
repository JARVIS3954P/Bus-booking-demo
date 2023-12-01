from tkinter import *

def open_seat_booking():
    root.destroy()
    import seat_booking

def open_check_booked_seat():
    root.destroy()
    import check_booked_seat

def open_add_bus_details():
    root.destroy()
    import add_bus_details

root = Tk()
h, w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0' % (w, h))

bus = PhotoImage(file='../assets/bus.png')

fr1 = Frame(root)
fr1.grid(row=0, column=0, columnspan=10)

fr2 = Frame(root)
fr2.grid(row=1, column=0, columnspan=10)

Label(fr1, image=bus).grid(row=0, column=0, padx=w//2.4)
Label(fr2, text="Online Bus Booking System", font='arial 30 bold', fg="Red", bg="Light Blue").grid(row=1, column=2, pady=20)

fr3=Frame(root)
fr3.grid(row=2, column=0, columnspan=10)

button1 = Button(fr3, text="Seat Booking", font='arial 14 bold', bg="pale green", fg="black", command=open_seat_booking)
button1.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
button2 = Button(fr3, text="Check Booked Seat", font='arial 14 bold', bg="medium sea green", fg="black", command=open_check_booked_seat)
button2.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
button3 = Button(fr3, text="Add Bus Details", font='arial 14 bold', bg="forest green", fg="black", command=open_add_bus_details)
button3.grid(row=0, column=2, padx=10, pady=10, sticky='ew')
Label(fr3, text="For Admin Only", fg="red", font='arial 10').grid(row=3, column=2, pady=5)

root.mainloop()
