import tkinter as tk
from tkinter import *
class Page:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)

    def show(self):
        self.frame.grid()

    def hide(self):
        self.frame.grid_forget()

class MainPage(Page):
    def __init__(self, master):
        super().__init__(master)
        bus = PhotoImage(file='assets/bus.png')

        fr1 = tk.Frame()
        fr1.grid(row=0, column=0, columnspan=10)

        fr2 = tk.Frame(root)
        fr2.grid(row=1, column=0, columnspan=10)

        Label(fr1, image=bus).grid(row=0, column=0, padx=w//2.4)
        Label(fr2, text="Online Bus Booking System", font='arial 30 bold', fg="Red", bg="Light Blue").grid(row=1, column=2, pady=20)

        fr3=tk.Frame(root)
        fr3.grid(row=2, column=0, columnspan=10)

        button1 = Button(fr3, text="Seat Booking", font='arial 14 bold', bg="pale green", fg="black", command=self.open_seat_booking)
        button1.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        button2 = Button(fr3, text="Check Booked Seat", font='arial 14 bold', bg="medium sea green", fg="black")
        button2.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        button3 = Button(fr3, text="Add Bus Details", font='arial 14 bold', bg="forest green", fg="black")
        button3.grid(row=0, column=2, padx=10, pady=10, sticky='ew')
        Label(fr3, text="For Admin Only", fg="red", font='arial 10').grid(row=3, column=2, pady=5)

    def open_seat_booking(self):
        self.hide()
        seat_booking_page.show()


class seat_booking(Page):
    def __init__(self, master):
        super().__init__(master)
        bus = PhotoImage(file='assets/bus.png')
        fr1 = tk.Frame()
        fr1.grid(row=0, column=0, columnspan=10)
        fr2 = tk.Frame()
        fr2.grid(row=1, column=0, columnspan=10)
        fr3 = tk.Frame()
        fr3.grid(row=2, column=0, columnspan=10)
        fr4 = tk.Frame()
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

        show_bus_button = Button(fr3, text="Show Bus",font='arial 12 bold', bg="green2", fg="green4")
        show_bus_button.grid(row=5, column=2, pady=10)

        back_button = Button(fr3, text="Back", command=self.back_to_main)
        back_button.grid(row=5, column=4)

    def show_bus(fr4):
        Label(fr4, text="Select Bus",font='arial 16 bold').grid(row=0,column=0)
        Label(fr4, text="Operator",font='arial 16 bold').grid(row=0,column=1)
        Label(fr4, text="Bus Type",font='arial 16 bold').grid(row=0,column=2)
        Label(fr4, text="Seat Available",font='arial 16 bold').grid(row=0,column=3)
        Label(fr4, text="Fare",font='arial 16 bold').grid(row=0,column=4)

    def back_to_main(self):
        self.hide()
        main_page.show()

class Page2(Page):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self.frame, text="Page 2").pack()
        tk.Button(self.frame, text="Back to Main", command=self.back_to_main).pack()

    def back_to_main(self):
        self.hide()
        main_page.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Multi-Page Tkinter App")
    h, w = root.winfo_screenheight(), root.winfo_screenwidth()
    root.geometry('%dx%d+0+0' % (w, h))

    main_page = MainPage(root)
    seat_booking_page = seat_booking(root)
    

    main_page.show()

    root.mainloop()





'''class Page:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()

class MainPage(Page):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self.frame, text="Main Page").pack()
        tk.Button(self.frame, text="Go to Page 1", command=self.open_page1).pack()
        tk.Button(self.frame, text="Go to Page 2", command=self.open_page2).pack()

    def open_page1(self):
        self.hide()
        page1.show()

    def open_page2(self):
        self.hide()
        page2.show()

class Page1(Page):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self.frame, text="Page 1").pack()
        tk.Button(self.frame, text="Back to Main", command=self.back_to_main).pack()

    def back_to_main(self):
        self.hide()
        main_page.show()

class Page2(Page):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self.frame, text="Page 2").pack()
        tk.Button(self.frame, text="Back to Main", command=self.back_to_main).pack()

    def back_to_main(self):
        self.hide()
        main_page.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Multi-Page Tkinter App")

    main_page = MainPage(root)
    page1 = Page1(root)
    page2 = Page2(root)

    main_page.show()

    root.mainloop()
'''