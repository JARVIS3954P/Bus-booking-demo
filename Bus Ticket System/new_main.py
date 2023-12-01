from tkinter import *

class demo():




#for main window
    def main_window(self):
        root = Tk()
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))
        bus = PhotoImage(file='assets/bus.png')
        fr1 = Frame(root)
        fr1.grid(row=0, column=0, columnspan=10)
        fr2 = Frame(root)
        fr2.grid(row=1, column=0, columnspan=10)
        Label(fr1, image=bus).grid(row=0, column=0, padx=w//2.4)
        Label(fr2, text="Online Bus Booking System", font='arial 30 bold', fg="Red", bg="Light Blue").grid(row=1, column=2, pady=20)
        fr3=Frame(root)
        fr3.grid(row=2, column=0, columnspan=10)
        def open_seat_booking(e=0):
            root.destroy()
            self.seat_booking()
        button1 = Button(fr3, text="Seat Booking", font='arial 14 bold', bg="pale green", fg="black", command=open_seat_booking)
        button1.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        def open_check_booked_seat(e=0):
            root.destroy()
            self.check_booked_seat()
        button2 = Button(fr3, text="Check Booked Seat", font='arial 14 bold', bg="medium sea green", fg="black", command=open_check_booked_seat)
        button2.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        def open_add_bus_details(e=0):
            root.destroy()
            self.add_bus_details()
        button3 = Button(fr3, text="Add Bus Details", font='arial 14 bold', bg="forest green", fg="black", command=open_add_bus_details)
        button3.grid(row=0, column=2, padx=10, pady=10, sticky='ew')
        Label(fr3, text="For Admin Only", fg="red", font='arial 10').grid(row=3, column=2, pady=5)
        root.mainloop()






#for seat booking
    def seat_booking(self):
        root = Tk()
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))
        bus = PhotoImage(file='assets/bus.png')
        fr1 = Frame(root)
        fr1.grid(row=0, column=0, columnspan=10)
        fr2 = Frame(root)
        fr2.grid(row=1, column=0, columnspan=10)
        fr3 = Frame(root)
        fr3.grid(row=2, column=0, columnspan=10)
        fr4=Frame(root)
        fr4.grid(row=3, column=0, columnspan=10)
        Label(fr1, image=bus).grid(row=0, column=0, padx=root.winfo_screenwidth()// 2.4)
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
        def show_bus():
            Label(fr4, text="Select Bus",font='arial 16 bold').grid(row=0,column=0)
            Label(fr4, text="Operator",font='arial 16 bold').grid(row=0,column=1)
            Label(fr4, text="Bus Type",font='arial 16 bold').grid(row=0,column=2)
            Label(fr4, text="Seat Available",font='arial 16 bold').grid(row=0,column=3)
            Label(fr4, text="Fare",font='arial 16 bold').grid(row=0,column=4)            
        show_bus_button = Button(fr3, text="Show Bus",font='arial 12 bold', bg="green2", fg="green4", command=show_bus)
        show_bus_button.grid(row=5, column=2, pady=10)
        def go_back():
            root.destroy()
            self.main_window()
        back_button = Button(fr3, text="Back", command=go_back)
        back_button.grid(row=5, column=4)
        root.mainloop()






#for checking bus details
    def check_bus_details():
        print()






    def add_bus_details():
        print()


d=demo()
d.main_window()


''' 
from tkinter import*
class demo():
    def violet(self):
        root = Tk()
        root.geometry('1920x1200')
        root.configure(bg="dark violet")
        #Label(root,text="First Screen",font="Arial 30 bold",bg="light green",fg="green").pack(ipady=100)
        def fun(e=0):
            root.destroy()
            self.indigo()
        #Button(root,text="Next",command=fun).pack()
        root.after(200,fun)
        root.mainloop()

    def indigo(self):
        root = Tk()
        root.geometry('1920x1200')
        root.configure(bg="blue2")
        Label(root,text="Second Screen",font="Arial 30 bold",bg="yellow",fg="red").pack(ipady=100)
        def fun(e=0):
            root.destroy()
            self.blue()
        #Button(root,text="Prev",command=fun).pack()
        root.after(200,fun)
        root.mainloop()
    def blue(self):
        root = Tk()
        root.geometry('1920x1200')
        root.configure(bg="blue")
        Label(root,text="First Screen",font="Arial 30 bold",bg="light green",fg="green").pack(ipady=100)
        def fun(e=0):
            root.destroy()
            self.green()
        #Button(root,text="Next",command=fun).pack()
        root.after(200,fun)
        root.mainloop()
    def green(self):
        root = Tk()
        root.geometry('1920x1200')
        root.configure(bg="lime green")
        Label(root,text="First Screen",font="Arial 30 bold",bg="light green",fg="green").pack(ipady=100)
        def fun(e=0):
            root.destroy()
            self.yellow()
        #Button(root,text="Next",command=fun).pack()
        root.after(200,fun)
        root.mainloop()
    def yellow(self):
        root = Tk()
        root.geometry('1920x1200')
        root.configure(bg="yellow2")
        Label(root,text="First Screen",font="Arial 30 bold",bg="light green",fg="green").pack(ipady=100)
        def fun(e=0):
            root.destroy()
            self.orange()
        #Button(root,text="Next",command=fun).pack()
        root.after(200,fun)
        root.mainloop()
    def orange(self):
        root = Tk()
        root.geometry('1920x1200')
        root.configure(bg="orange2")
        Label(root,text="First Screen",font="Arial 30 bold",bg="light green",fg="green").pack(ipady=100)
        def fun(e=0):
            root.destroy()
            self.red()
        #Button(root,text="Next",command=fun).pack()
        root.after(200,fun)
        root.mainloop()
    def red(self):
        root = Tk()
        root.geometry('1920x1200')
        root.configure(bg="red2")
        #Label(root,text="First Screen",font="Arial 30 bold",bg="light green",fg="green").pack(ipady=100)
        def fun(e=0):
            root.destroy()
            self.violet()
        #Button(root,text="Next",command=fun).pack()
        root.after(200,fun)
        root.mainloop()

d=demo()'''