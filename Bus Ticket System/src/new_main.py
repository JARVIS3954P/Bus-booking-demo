from tkinter import *
from sqlite import *
import sqlite3
from datetime import datetime
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

db_path = 'project.db'



class demo():


    def process_arguments(*args):
    # Check if any argument is null or an empty string
        for arg in args:
            if arg is None or (isinstance(arg, str) and arg.strip() == ''):
                return 0  # Return 0 if an error occurs

        # Return arguments in a tuple
        return tuple(args)


    def main_window(self):
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
        def open_seat_booking(e=0):
            root.destroy()
            self.seat_booking()
        button1 = Button(fr3, text="Seat Booking", font='arial 14 bold', bg="pale green", fg="black", command=open_seat_booking)
        button1.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        def open_check_booked_seat(e=0):
            root.destroy()
            self.check_bus_details()
        button2 = Button(fr3, text="Check Booked Seat", font='arial 14 bold', bg="medium sea green", fg="black", command=open_check_booked_seat)
        button2.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        def open_add_bus_details(e=0):
            root.destroy()
            self.admin_only()
        button3 = Button(fr3, text="Add Bus Details", font='arial 14 bold', bg="forest green", fg="black", command=open_add_bus_details)
        button3.grid(row=0, column=2, padx=10, pady=10, sticky='ew')
        Label(fr3, text="For Admin Only", fg="red", font='arial 10').grid(row=3, column=2, pady=5)
        root.mainloop()


    def ticket_window(self,ph_no):
            root=Tk()
            h,w=root.winfo_screenheight(),root.winfo_screenwidth()
            root.geometry('%dx%d+0+0'%(w,h))
            messagebox.showinfo('info','Seat Booked.......')
            bus = PhotoImage(file='../assets/bus.png')
            fr1 = Frame(root)
            fr1.grid(row=0, column=0, columnspan=10)
            fr2 = Frame(root)
            fr2.grid(row=1, column=0, columnspan=10)
            Label(fr1, image=bus).grid(row=0, column=0, padx=w//2.4)
            Label(fr2, text="Online Bus Booking System", font='arial 30 bold', fg="Red", bg="Light Blue").grid(row=1, column=2, pady=20)
            Label(fr2,text='Bus Ticket',font='arial 15 bold').grid(row=2,column=2,padx=10)

            fr3=Frame(root,relief='groove',bd=3)
            fr3.grid(row=2,column=0,columnspan=50,padx=(w/15,0))
            fr4=Frame(root,relief='groove',bd=3)
            fr4.grid(row=3,column=0,columnspan=50,padx=(w/15,0))
            Label(fr3,text='Passenger Name :',font='Arial 10 bold').grid(row=0,column=0, padx=20)
            Label(fr3,text='Gender :',font='Arial 10 bold').grid(row=1,column=0, padx=20)
            Label(fr3,text='Age :',font='Arial 10 bold').grid(row=2,column=0, padx=20)
            Label(fr3,text='Phone:',font='Arial 10 bold').grid(row=3,column=0, padx=20)
            Label(fr3,text='Seats Booked :',font='Arial 10 bold').grid(row=4,column=0, padx=20)
            Label(fr3,text='Fare ₹ :',font='Arial 10 bold').grid(row=5,column=0, padx=20)
            Label(fr3,text='Bus Detail :',font='Arial 10 bold').grid(row=0,column=1)
            Label(fr3,text='Operator Contact :',font='Arial 10 bold').grid(row=1,column=1)
            Label(fr3,text='Booking Ref :',font='Arial 10 bold').grid(row=2,column=1)
            Label(fr3,text='Travel on :',font='Arial 10 bold').grid(row=3,column=1)
            Label(fr3,text='Booked On :',font='Arial 10 bold').grid(row=4,column=1)
            Label(fr3,text='Boarding Point',font='Arial 10 bold').grid(row=5,column=1)
            Label(fr3,text='* Total amount of ₹ 1000.00/- to be paid at the time of boarding',font='Arial 8').grid(row=6,columnspan=100,pady=10)

            def go_home():
                root.destroy()
                self.main_window()
            home=PhotoImage(file="../assets/home.png")
            home_button = Button(fr4,image=home, command=go_home)
            home_button.grid(row=0,column=0,sticky='W')

            root.mainloop()    


    def seat_booking(self):
        root = Tk()
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))
        bus = PhotoImage(file='../assets/bus.png')
        fr1 = Frame(root)
        fr1.grid(row=0, column=0, columnspan=10)
        fr2 = Frame(root)
        fr2.grid(row=1, column=0, columnspan=10)
        fr3 = Frame(root)
        fr3.grid(row=2, column=0, columnspan=10)
        fr4=Frame(root)
        fr4.grid(row=3, column=0, columnspan=10)
        fr5=Frame(root)
        fr5.grid(row=4,column=0,columnspan=10)
        fr6=Frame(root)
        fr6.grid(row=5,column=0,columnspan=10)
        Label(fr1, image=bus).grid(row=0, column=0, padx=root.winfo_screenwidth()// 2.4)
        Label(fr2, text="Online Bus Booking System", font='arial 30 bold', fg="Red", bg="Light Blue").grid(row=1, column=2, pady=20)
        Label(fr3, text="Enter Journey Details", font='arial 16 bold', fg="green4", bg="green2").grid(row=0, column=2)
       
        to = StringVar()
        frm = StringVar()
        date = StringVar()

        # Input boxes
        to_label = Label(fr3, text="To")
        to_label.grid(row=1, column=1, sticky='e')
        to_entry = Entry(fr3,textvariable=to)
        to_entry.grid(row=1, column=2)
        from_label = Label(fr3, text="From")
        from_label.grid(row=2, column=1, sticky='e')
        from_entry = Entry(fr3,textvariable=frm)
        from_entry.grid(row=2, column=2)
        journey_date_label = Label(fr3, text="Journey Date")
        journey_date_label.grid(row=3, column=1, sticky='e')
        journey_date_entry = Entry(fr3,textvariable=date)
        journey_date_entry.grid(row=3, column=2)
        placeholder_label = Label(fr3, text="yyyy-mm-dd", fg="red")
        placeholder_label.grid(row=4, column=2)
        



        def show_bus(tpl):
            
            #tpl = check_journey_details_with_seats(to.get(),frm.get(),date.get())
            Label(fr4, text="Select Bus",font='arial 16 bold', fg='dark slate gray').grid(row=0,column=0,padx=10)
            Label(fr4, text="Operator",font='arial 16 bold', fg='dark slate gray').grid(row=0,column=1,padx=10)
            Label(fr4, text="Bus Type",font='arial 16 bold', fg='dark slate gray').grid(row=0,column=2,padx=10)
            Label(fr4, text="Seat Available",font='arial 16 bold', fg='dark slate gray',).grid(row=0,column=3,padx=10)
            Label(fr4, text="Fare",font='arial 16 bold', fg='dark slate gray').grid(row=0,column=4,padx=25)
            global selected_bus_id
            global busfare
            selected_bus_id = None
            busfare = None
            def button_click(id,fare):
                global selected_bus_id
                selected_bus_id = id
                global busfare
                busfare = fare 
            def show_tuple():
                for row, (bus_id, operator,bus_type,a,t,fare) in enumerate(tpl):
                    Button(fr4, text = "Bus_"+str(bus_id), font = 'arial 12 bold', fg='black', command=lambda id=bus_id, fare=fare: button_click(id, fare)).grid(row=row+1,column=0,padx=10)
                    Label(fr4, text=operator,font='arial 12 bold', fg='black').grid(row=row+1,column=1,padx=10)
                    Label(fr4, text=operator,font='arial 12 bold', fg='black').grid(row=row+1,column=2,padx=10)
                    Label(fr4, text=str(a)+"/"+str(t),font='arial 12 bold', fg='black').grid(row=row+1,column=3,padx=10)
                    Label(fr4, text=str(fare),font='arial 12 bold', fg='black').grid(row=row+1,column=4,padx=25)
            show_tuple()
            def cred():
                global busfare
                f = busfare
                global selected_bus_id
                bus_id = selected_bus_id
                if(selected_bus_id != None or busfare != None):

            
                    passenger_name = StringVar()
                    sex = StringVar()
                    seats = IntVar()
                    mobile_number = StringVar() 
                    age = IntVar()
                    Label(fr5,text="FILL PASSENGER DETAILS TO BOOK THIS TICKET", font='arial 16 bold', fg='red',bg='light blue').grid(row=0,column=2,pady=20)
                    Label(fr6,text="Name",font = 'arial 12 bold').grid(row=1,column=0,padx=10)
                    Entry(fr6,textvariable= passenger_name).grid(row=1,column=1,padx=15)
                    Label(fr6,text="Gender",font = 'arial 12 bold').grid(row=1,column=2,padx=10)
                    gender_options=['M','F']
                    dropdown = OptionMenu(fr6, sex, *gender_options)
                    dropdown.grid(row=1,column=3,padx=15)
                    Label(fr6,text="No of sets",font = 'arial 12 bold').grid(row=1,column=4,padx=10)
                    Entry(fr6,textvariable=seats).grid(row=1,column=5,padx=15)
                    Label(fr6,text="mob no",font = 'arial 12 bold').grid(row=1,column=6,padx=10)
                    Entry(fr6,textvariable= mobile_number).grid(row=1,column=7,padx=15)
                    Label(fr6,text="age ",font = 'arial 12 bold').grid(row=1,column=8,padx=10)
                    Entry(fr6,textvariable = age).grid(row=1,column=9,padx=15)

                    def insert():
                        if(age.get()>90 or seats.get() > 8):
                            messagebox.showinfo("Error", "Please insert correct fields!")
                        else:  
                            result = messagebox.askquestion("Confirm?", "You'll be paying ₹1000")
                            if(result == 'yes'):
                                val = add_new_booking_with_seat_update(db_path,date.get(),bus_id,passenger_name.get(),sex.get(),seats.get(),mobile_number.get(),age.get(),f*seats.get())
                                if val == 1:
                                    messagebox.showinfo("Sorry", "Not Enough Seats Avalable")
                                elif val == 2:
                                    root.destroy()
                                    self.ticket_window(mobile_number)
                                else:
                                    messagebox.showinfo("Error","Enter all the Details")

                    Button(fr6,text ="Book Seat",command = insert).grid(row=1,column=10)
                else:
                    messagebox.showinfo("Error", "Please Select a Bus")
            


            proceed_button=Button(fr4,text="Proceed to Book", font='arial 14 bold', bg="green4", fg="black",command = cred).grid(row=0,column=5)

        


        def insert():
            def is_valid_date_format(date_str):
                try:
                    # Attempt to parse the date string using the specified format
                    datetime.strptime(date_str, '%Y-%m-%d')
                    return 1
                except ValueError:
                    # If an exception is raised, the format is not valid
                    return 0
            if is_valid_date_format(date.get()) == 0:
                messagebox.showinfo("Info", "Enter correct date format")
            else:
                tpl = check_journey_details_with_seats(db_path,frm.get(),to.get(),date.get())
                if(len(tpl) == 0):
                    messagebox.showinfo("info", "NO avalable buses")
                else:
                    show_bus(tpl)                       
        show_bus_button = Button(fr3, text="Show Bus",font='arial 12 bold', bg="green2", fg="green4", command=insert)
        show_bus_button.grid(row=5, column=2, pady=10)
        
        def go_back():
            root.destroy()
            self.main_window()
        back_button = Button(fr3, text="Back", command=go_back)
        back_button.grid(row=5, column=4)
        root.mainloop()


    def check_bus_details(self):
        root = Tk()
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))
        bus = PhotoImage(file='../assets/bus.png')
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
        Label(fr2, text="Check Your Booking", font='arial 16 bold', fg="green4", bg="green2").grid(row=2, column=2,pady=20)
        # Input boxes
        ph_no = StringVar()
        to_label = Label(fr3, text="Enter Your Number :", font='arial 12')
        to_label.grid(row=1, column=1, padx=10,sticky='e')
        to_entry = Entry(fr3,textvariable = ph_no)
        to_entry.grid(row=1, column=2, padx=10)
        
        def check_booking():
            root.destroy()
            self.ticket_window(ph_no.get())#here to_entry is mobile number            
        check_button = Button(fr3, text="Check",font='arial 12 bold', bg="gray", fg="black", command=check_booking)
        check_button.grid(row=1, column=3, padx=10)
        def go_back():
            root.destroy()
            self.main_window()
        back_button = Button(fr3, text="Back", command=go_back)
        back_button.grid(row=1, column=4)
        root.mainloop()



    def admin_only(self):
        root = Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        root.title('Add New Details')
        bus=PhotoImage(file="../assets/bus.png")
        Label(root, image=bus).grid(row=0,column=0,columnspan=20,padx=w//2.5)
        Label(root, text="Online Bus Booking System",font=("Arial", 30,"bold"),bg= "sky blue", fg= "red2").grid(row=1,column=0,columnspan=20,padx=w//3)
        Label(root,text = "Add New Detail to Database",font=("Arial", 20,"bold"), fg= "green4").grid(row=2,column=0,columnspan=20,pady=20)
        def newop():
            root.destroy()
            self.add_bus_operator()
        def newbus():
            root.destroy()
            self.add_bus_details()
        def newroute():
            root.destroy()
            self.add_bus_route()
        def newrun():
            root.destroy()
            self.bus_running_detail()
        def newstation():
            root.destroy()
            self.add_station()
        New_operator = Button(root,text="New Operator",font=("Arial", 15,),bg= "pale green", fg= "gray5",command=newop)
        New_operator.grid(row=3,column=10,pady=20)
        New_Bus = Button(root,text="New Bus",font=("Arial", 15,),bg= "coral", fg= "gray5",command=newbus)
        New_Bus.grid(row=3,column=11,pady=20)
        New_Route = Button(root,text="New Route",font=("Arial", 15,),bg= "steel blue", fg= "gray5",command=newroute)
        New_Route.grid(row=3,column=9,pady=20)
        New_Run = Button(root,text="New Run",font=("Arial", 15,),bg= "RosyBrown3", fg= "gray5",command=newrun)
        New_Run.grid(row=3,column=12,pady=20)
        New_Station = Button(root,text="New Station",font=("Arial", 15,),bg= "yellow", fg= "gray5",command=newstation)
        New_Station.grid(row=3,column=8,pady=20)
        def go_home():
            root.destroy()
            self.main_window()
        home_button = Button(root,text="Back",command=go_home)
        home_button.grid(row=4,column=10,pady=20,sticky='W')
        root.mainloop()        
    
    def add_station(self):
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
        t2 = Label(fr2, text='Add Station Details', bg='gray20', fg='green3', font='Arial 22 bold').grid(row=2, column=2, padx=w // 3, pady=20)
        fr3=Frame(root)
        fr3.grid(row=2, column=0, columnspan=10)
        station_id = IntVar()
        station_name = StringVar()
        Label(fr3,text="Sation ID", font='arial 12 ').grid(row=0,column=0,padx=10)
        sId_entry=Entry(fr3,textvariable = station_id)
        sId_entry.grid(row=0,column=1,padx=10)
        Label(fr3,text="Sation Name", font='arial 12 ').grid(row=0,column=2,padx=10)
        sName_entry=Entry(fr3,textvariable = station_name)
        sName_entry.grid(row=0,column=3,padx=10)
        def insert():
            if insert_station_data(db_path,station_id.get(),station_name.get()):
                messagebox.showinfo("Info", "Sucess!")
            else:
                messagebox.showinfo("Info","Error!")

        add_button=Button(fr3,text="Add", bg="green2",command = insert)
        add_button.grid(row=0,column=4,padx=10)
        
        def go_home():
            root.destroy()
            self.main_window()
        home=PhotoImage(file="../assets/home.png")
        home_button = Button(fr3,image=home, command=go_home)
        home_button.grid(row=0,column=5,pady=20,padx=5,sticky='W')

        def go_back():
            root.destroy()
            self.admin_only()
        back_button = Button(fr3,text="Back", command=go_back)
        back_button.grid(row=0,column=6,pady=20,padx=5,sticky='W')
        
        root.mainloop()

    def add_bus_route(self):
        root = Tk()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry('%dx%d+0+0' % (w, h))
        img = PhotoImage(file="../assets/bus.png")
        img1 = PhotoImage(file="../assets/home.png")
        bus = Label(root, image=img)
        bus.grid(row=0, column=0, columnspan=20, padx=w // 3)
        t1 = Label(root, text='Online Bus Booking System', bg='light blue', fg='Red', font='Arial 32 bold')
        t1.grid(row=1, column=0, columnspan=20, padx=w // 3)
        t2 = Label(root, text='Add Bus Route Details', bg='gray20', fg='green3', font='Arial 22 bold')
        t2.grid(row=2, column=0, columnspan=20, padx=w // 3, pady=20)
        routeid = IntVar()
        d_sname = StringVar()
        o_sname = StringVar()

        Routeid = Label(root, text='Route ID', font='Arial 14')
        origin_sation = Label(root, text='Origin Station', font='Arial 14')
        destination_satation = Label(root, text='destination satation', font='Arial 14')

        routef = Entry(root,textvariable= routeid)
        o_sname = Entry(root,textvariable = o_sname)
        d_sname = Entry(root,textvariable = d_sname)

        def insert():
            if add_new_route(db_path,routeid.get(),o_sname.get(),d_sname.get()):
                messagebox.showinfo("Info", "Sucess!")
            else:
                messagebox.showinfo("Info","Error!")

        def update():
            if delete_route_by_id(db_path,routeid.get()):
                messagebox.showinfo("Info", "Sucess!")
            else:
                messagebox.showinfo("Info","Error!")
                




        addb = Button(root, text='Add Route', bg='SpringGreen2', font='Arial 14', command=insert)
        eb = Button(root, text='Delete Route', bg='SpringGreen2',fg='Red', font='Arial 14', command= update)


        Routeid.grid(row=5, column=3)
        routef.grid(row=5, column=4)
        origin_sation.grid(row=5, column=5)
        o_sname.grid(row=5, column=6)
        destination_satation.grid(row=5, column=7)
        d_sname.grid(row=5, column=8)
        addb.grid(row=5, column=9)
        eb.grid(row=5, column=10)

        def go_home():
            root.destroy()
            self.main_window()
        home=PhotoImage(file="../assets/home.png")
        home_button = Button(root,image=home, command=go_home)
        home_button.grid(row=5,column=12,pady=20,sticky='W')

        def go_back():
            root.destroy()
            self.admin_only()
        back_button = Button(root,text="Back", command=go_back)
        back_button.grid(row=5,column=11,pady=20,sticky='W')

        root.mainloop()

    def add_bus_operator(self):
        root = Tk()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry('%dx%d+0+0' % (w, h))
        img = PhotoImage(file="../assets/bus.png")
        img1 = PhotoImage(file="../assets/home.png")
        bus = Label(root, image=img)
        bus.grid(row=0, column=0, columnspan=20, padx=w // 3)
        t1 = Label(root, text='Online Bus Booking System', bg='light blue', fg='Red', font='Arial 32 bold')
        t1.grid(row=1, column=0, columnspan=20, padx=w // 3)
        t2 = Label(root, text='Add Bus Operator Details', bg='white smoke', fg='green3', font='Arial 22 bold')
        t2.grid(row=2, column=0, columnspan=20, padx=w // 3, pady=20)
        opid = Label(root, text='Operator ID', font='Arial 14')
        name = Label(root, text='Name', font='Arial 14')
        add = Label(root, text='Address', font='Arial 14')
        ph = Label(root, text='Phone', font='Arial 14')
        mail = Label(root, text='Email', font='Arial 14')
        # Tkinter variable for storing entries
        opf = IntVar()
        nf = StringVar()
        addf = StringVar()
        phf = StringVar()
        mf = StringVar()
        #Entries for our form
        opf = Entry(root, textvariable=opf)
        nf = Entry(root, textvariable=nf)
        addf = Entry(root, textvariable=addf)
        phf = Entry(root, textvariable=phf)
        mf = Entry(root, textvariable=mf)

        def insert():
            if add_new_operator(db_path,opf.get(),nf.get(),addf.get(),phf.get(),mf.get()):
                 messagebox.showinfo("Sucess")
            else:
                 messagebox.showinfo("Error")                 
        def update():
            if update_operator(db_path,opf.get(),nf.get(),addf.get(),phf.get(),mf.get()):
                 messagebox.showinfo("Sucess")
            else:
                 messagebox.showinfo("Error")
        addb = Button(root, text='Add', bg='SpringGreen2', font='Arial 14', command=insert)
        eb = Button(root, text='Edit', bg='SpringGreen2', font='Arial 14',command=update)
        opid.grid(row=3, column=1) 
        opf.grid(row=3, column=2)
        name.grid(row=3, column=3)
        nf.grid(row=3, column=4)
        add.grid(row=3, column=5)
        addf.grid(row=3, column=6)
        ph.grid(row=3, column=7)
        phf.grid(row=3, column=8)
        mail.grid(row=3, column=9)
        mf.grid(row=3, column=10)
        addb.grid(row=3, column=11)
        eb.grid(row=3, column=12)
        def go_home():
            root.destroy()
            self.main_window()
        home=PhotoImage(file="../assets/home.png")
        home_button = Button(root,image=home, command=go_home)
        home_button.grid(row=5,column=9,pady=20,sticky='W')
        def go_back():
            root.destroy()
            self.admin_only()
        back_button = Button(root,text="Back", command=go_back)
        back_button.grid(row=5,column=10,pady=20,sticky='W')
        root.mainloop()

    def add_bus_details(self):
        root = Tk()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry('%dx%d+0+0' % (w, h))
        img = PhotoImage(file="../assets/bus.png")
        img1 = PhotoImage(file="../assets/home.png")
        bus = Label(root, image=img)
        bus.grid(row=0, column=0, columnspan=20, padx=w // 3)
        t1 = Label(root, text='Online Bus Booking System', bg='light blue', fg='Red', font='Arial 32 bold')
        t1.grid(row=1, column=0, columnspan=20, padx=w // 3)
        t2 = Label(root, text='Add Bus Details', bg='gray20', fg='green3', font='Arial 22 bold')
        t2.grid(row=2, column=0, columnspan=20, padx=w // 3, pady=20)
        busid = Label(root, text='Bus ID', font='Arial 14')
        bustype = Label(root, text='Bus type', font='Arial 14')
        CapacitY = Label(root, text='Capacity', font='Arial 14')
        farE = Label(root, text='Fare Rs', font='Arial 14')
        opid = Label(root, text='Operator ID', font='Arial 14')
        Routeid = Label(root, text='Route ID', font='Arial 14')
        options = [
                "AC 2x2",
                "AC 3x2",
                "Non AC 2x2",
                "Non AC 3x2",
                "AC-Sleeper 2x1",
                "Non AC-Sleeper 2x1"
            ]
        clicked = StringVar()
        clicked.set("Bus Type")
        drop = OptionMenu(root, clicked, *options)
        # Tkinter variable for storing entries
        busid_f = IntVar()
        Routeid_f = IntVar()
        CapacitY_f = IntVar()
        farE_f = IntVar()
        opid_f = IntVar()
        #Entries for our form
        busid_f = Entry(root, textvariable=busid_f)
        Routeid_f = Entry(root, textvariable=Routeid_f)
        CapacitY_f = Entry(root, textvariable=CapacitY_f)
        farE_f = Entry(root, textvariable=farE_f)
        opid_f = Entry(root, textvariable=opid_f)        
        def insert():
            if add_new_bus(db_path,busid_f.get(),clicked.get(),CapacitY_f.get(),farE_f.get(),opid_f.get(),Routeid_f.get()):
                messagebox.showinfo("Info", "Sucess")
            else:
                messagebox.showinfo("Info", "Error")

        def update():
            if update_bus(db_path,busid_f.get(),clicked.get(),CapacitY_f.get(),farE_f.get(),opid_f.get(),Routeid_f.get()):
                messagebox.showinfo("Info", "Sucess")
            else:
                messagebox.showinfo("Info", "Error")

        addb = Button(root, text='Add Bus', bg='SpringGreen2', font='Arial 14', command=insert)
        eb = Button(root, text='Edit Bus', bg='SpringGreen2', font='Arial 14',command =update)
        busid.grid(row=3, column=1)
        busid_f.grid(row=3, column=2)
        bustype.grid(row=3, column=3)
        drop.grid(row=3, column=4)
        CapacitY.grid(row=3, column=5)
        CapacitY_f.grid(row=3, column=6)
        farE.grid(row=3, column=7)
        farE_f.grid(row=3, column=8)
        opid.grid(row=3, column=9)
        opid_f.grid(row=3, column=10)
        Routeid.grid(row=3, column=11)
        Routeid_f.grid(row=3, column=12)
        addb.grid(row=5, column=7)
        eb.grid(row=5, column=8)
        def go_home():
            root.destroy()
            self.main_window()
        home=PhotoImage(file="../assets/home.png")
        home_button = Button(root,image=home, command=go_home)
        home_button.grid(row=5,column=9,pady=20,sticky='W')
        def go_back():
            root.destroy()
            self.admin_only()
        back_button = Button(root,text="Back", command=go_back)
        back_button.grid(row=5,column=10,pady=20,sticky='W')
        root.mainloop()        
        
    def bus_running_detail(self):
        root = Tk()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry('%dx%d+0+0' % (w, h))
        img = PhotoImage(file="../assets/bus.png")
        img1 = PhotoImage(file="../assets/home.png")
        bus = Label(root, image=img)
        bus.grid(row=0, column=0, columnspan=20, padx=w // 3)
        t1 = Label(root, text='Online Bus Booking System', bg='light blue', fg='Red', font='Arial 32 bold')
        t1.grid(row=1, column=0, columnspan=20, padx=w // 3)
        t2 = Label(root, text='Add Bus Running Details', bg='gray20', fg='green3', font='Arial 22 bold')
        t2.grid(row=2, column=0, columnspan=20, padx=w // 3, pady=20)
        Busid = Label(root, text='Bus ID', font='Arial 14')
        date = Label(root, text='Running Date', font='Arial 14')
        jdate = StringVar()
        jbusid = StringVar()
        bidf = Entry(root,textvariable = jbusid)
        datef = Entry(root,textvariable = jdate)
        def insert():
            def is_valid_date_format(date_str):
                try:
                    # Attempt to parse the date string using the specified format
                    datetime.strptime(date_str, '%Y-%m-%d')
                    return 1
                except ValueError:
                    # If an exception is raised, the format is not valid
                    return 0
            a = add_new_journey(db_path,jdate.get(),jbusid.get())
            if a  == 1:
                messagebox.showinfo("Info", "Sucess")
            else:                
                messagebox.showinfo("Info", "Error")

        addb = Button(root, text='Add Run', bg='SpringGreen2', font='Arial 14', command=insert)
        Busid.grid(row=5, column=3)
        bidf.grid(row=5, column=4)
        date.grid(row=5, column=5)
        datef.grid(row=5, column=6)
        addb.grid(row=5, column=9)



        def go_home():
            root.destroy()
            self.main_window()
        home=PhotoImage(file="../assets/home.png")
        home_button = Button(root,image=home, command=go_home)
        home_button.grid(row=5,column=11,pady=20,sticky='W')

        def go_back():
            root.destroy()
            self.admin_only()
        back_button = Button(root,text="Back", command=go_back)
        back_button.grid(row=5,column=12,pady=20,sticky='W')


        root.mainloop()


    

        
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
Label(fr3,text="Name : Vaibhav Anand", font='arial 16', fg='blue').grid(row=0,column=0,pady=10)
Label(fr3,text="Enrollment : 221B426", font='arial 16', fg='blue').grid(row=1,column=0,pady=10)
Label(fr3,text="Mobile : 8423859380", font='arial 16', fg='blue').grid(row=2,column=0,pady=20)
fr4 = Frame(root)
fr4.grid(row=3, column=0, columnspan=10)
Label(fr4, text="Submitted To : Dr. Mahesh Kumar", font='arial 25 bold', fg="Red", bg="Light Blue").grid(row=0, column=0, pady=10)
Label(fr4, text="Project Based Learning", font='arial 20 bold', fg="Red", ).grid(row=1, column=0, pady=10)
def fun(e=0):
    root.destroy()
root.bind("<KeyPress>",fun)
root.mainloop()


d=demo()
d.main_window()


