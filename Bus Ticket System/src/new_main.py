from tkinter import *

class demo():



#for main window
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


#for seat booking
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
            Label(fr4, text="Select Bus",font='arial 16 bold', fg='green2').grid(row=0,column=0,padx=10)
            Label(fr4, text="Operator",font='arial 16 bold', fg='green2').grid(row=0,column=1,padx=10)
            Label(fr4, text="Bus Type",font='arial 16 bold', fg='green2').grid(row=0,column=2,padx=10)
            Label(fr4, text="Seat Available",font='arial 16 bold', fg='green2').grid(row=0,column=3,padx=10)
            Label(fr4, text="Fare",font='arial 16 bold', fg='green2').grid(row=0,column=4,padx=10)            
        show_bus_button = Button(fr3, text="Show Bus",font='arial 12 bold', bg="green2", fg="green4", command=show_bus)
        show_bus_button.grid(row=5, column=2, pady=10)
        def go_back():
            root.destroy()
            self.main_window()
        back_button = Button(fr3, text="Back", command=go_back)
        back_button.grid(row=5, column=4)
        root.mainloop()


#for checking bus details
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
        to_label = Label(fr3, text="Enter Your Number :", font='arial 12')
        to_label.grid(row=1, column=1, padx=10,sticky='e')
        to_entry = Entry(fr3)
        to_entry.grid(row=1, column=2, padx=10)
        
        def check_booking():
            pass            
        check_button = Button(fr3, text="Check",font='arial 12 bold', bg="gray", fg="black", command=check_booking)
        check_button.grid(row=1, column=3, padx=10)
        def go_back():
            root.destroy()
            self.main_window()
        back_button = Button(fr3, text="Back", command=go_back)
        back_button.grid(row=1, column=4)
        root.mainloop()


#For admin to adding to database  
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
        New_operator.grid(row=3,column=8,pady=20)
        New_Bus = Button(root,text="New Bus",font=("Arial", 15,),bg= "coral", fg= "gray5",command=newbus)
        New_Bus.grid(row=3,column=9,pady=20)
        New_Route = Button(root,text="New Route",font=("Arial", 15,),bg= "steel blue", fg= "gray5",command=newroute)
        New_Route.grid(row=3,column=10,pady=20)
        New_Run = Button(root,text="New Run",font=("Arial", 15,),bg= "RosyBrown3", fg= "gray5",command=newrun)
        New_Run.grid(row=3,column=11,pady=20)
        New_Station = Button(root,text="New Station",font=("Arial", 15,),bg= "yellow", fg= "gray5",command=newstation)
        New_Station.grid(row=3,column=12,pady=20)
        def go_home():
            root.destroy()
            self.main_window()
        home_button = Button(root,text="Back",command=go_home)
        home_button.grid(row=4,column=10,pady=20,sticky='W')
        root.mainloop()        
    

#Options for admin  
    def add_bus_details(self):
        root = Tk()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry('%dx%d+0+0' % (w, h))

        import sqlite3
        con = sqlite3.connect('PYthonBusProj.db')
        cur = con.cursor()


        img = PhotoImage(file="../assets/bus.png")
        img1 = PhotoImage(file="../assets/home.png")
        bus = Label(root, image=img)
        bus.grid(row=0, column=0, columnspan=20, padx=w // 3)
        t1 = Label(root, text='Online Bus Booking System', bg='light blue', fg='Red', font='Arial 32 bold')
        t1.grid(row=1, column=0, columnspan=20, padx=w // 3)
        t2 = Label(root, text='Add Bus Details', bg='gray20', fg='green3', font='Arial 22 bold')
        t2.grid(row=2, column=0, columnspan=20, padx=w // 3, pady=20)



        def getvals():

            cur.execute("""insert into bus (busID,bus_type,bus_opid,capacity,fare,bus_rid)values({},'{}',{},{},{},{})""".format(busid_f.get(), clicked.get(), opid_f.get(), CapacitY_f.get(), farE_f.get(), opid_f.get(),Routeid_f.get()))
            con.commit()

            op1 = Label(root,text='{} {} {} {} {} {}'.format(busid_f.get(), clicked.get(), CapacitY_f.get(), farE_f.get(), opid_f.get(),Routeid_f.get()),font='Arial 12')


            op1.grid(row=4, columnspan=13)
            showinfo('Operator Entry Updated', 'Bus Details updated successfully')


            print(f"{busid_f.get(),clicked.get(),  CapacitY_f.get(), farE_f.get(), opid_f.get(),Routeid_f.get()} ")

            with open("add_busdetail.txt", "a") as f:
                f.write(f"{busid_f.get(), clicked.get(),  CapacitY_f.get(), farE_f.get(), opid_f.get(),Routeid_f.get()}\n ")



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
        busid_f = StringVar()
        Routeid_f = StringVar()
        CapacitY_f = StringVar()
        farE_f = StringVar()
        opid_f = StringVar()

        #Entries for our form
        busid_f = Entry(root, textvariable=busid_f)
        Routeid_f = Entry(root, textvariable=Routeid_f)
        CapacitY_f = Entry(root, textvariable=CapacitY_f)
        farE_f = Entry(root, textvariable=farE_f)
        opid_f = Entry(root, textvariable=opid_f)


        def checking():
            cur.execute("SELECT * FROM bus")
            f=cur.fetchall()
            print(f)


        def addnew():
            op1 = Label(root, text='{} {} {} {} {}'.format(busid_f.get(),clicked.get(), CapacitY_f.get(), farE_f.get(), opid_f.get(), Routeid_f.get()),
                        font='Arial 12')
            op1.grid(row=4, columnspan=13)
            showinfo('Operator Entry Updated', 'Bus Details updated successfully')

        addb = Button(root, text='Add Bus', bg='SpringGreen2', font='Arial 14', command=getvals)
        eb = Button(root, text='Edit Bus', bg='SpringGreen2', font='Arial 14')

        #check_db = Button(root, text='Check', bg='SpringGreen2', font='Arial 14', command=checking)
        #check_db.grid(row=10, column=11)

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

        import sqlite3

        con = sqlite3.connect('PYthonBusProj.db')
        cur = con.cursor()


        def getvals():

            cur.execute("""insert into operator (opid,name,phone,address,email)values({},'{}',{},'{}','{}')""".format(int(float(opf.get())), nf.get(), int(phf.get()), addf.get(), mf.get()))
            con.commit()

            op1 = Label(root, text='{} {} {} {} {}'.format(opf.get(), nf.get(), addf.get(), phf.get(), mf.get()),
                        font='Arial 12')
            op1.grid(row=4, columnspan=13)
            showinfo('Operator Entry Updated', 'Operator Record updated successfully')

            print(f"{opf.get(), nf.get(), addf.get(), phf.get(), mf.get()} ")

            with open("operator_detail.txt", "a") as f:
                f.write(f"{opf.get(), nf.get(), addf.get(), phf.get(), mf.get()}\n ")



        opid = Label(root, text='Operator ID', font='Arial 14')
        name = Label(root, text='Name', font='Arial 14')
        add = Label(root, text='Address', font='Arial 14')
        ph = Label(root, text='Phone', font='Arial 14')
        mail = Label(root, text='Email', font='Arial 14')



        # Tkinter variable for storing entries
        opf = StringVar()
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


        def checking():
            cur.execute("SELECT * FROM operator")
            f=cur.fetchall()
            print(f)


        def addnew():
            op1 = Label(root, text='{} {} {} {} {}'.format(opf.get(), nf.get(), addf.get(), phf.get(), mf.get()),
                        font='Arial 12')
            op1.grid(row=4, columnspan=13)
            showinfo('Operator Entry Updated', 'Operator Record updated successfully')


        addb = Button(root, text='Add', bg='SpringGreen2', font='Arial 14', command=getvals)
        eb = Button(root, text='Edit', bg='SpringGreen2', font='Arial 14')

        #check_db = Button(root, text='Check', bg='SpringGreen2', font='Arial 14', command=checking)
        #check_db.grid(row=10, column=11)

        opid.grid(row=3, column=1)  # stick=W or E
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


        import sqlite3

        con = sqlite3.connect('PYthonBusProj.db')
        cur = con.cursor()



        def addnew():
            '''routef.delete(0, END)
            snf.delete(0, END)
            staion_id_f.delete(0, END)'''


            #cur.execute("""select rid from route""".format(c.get))

            cur.execute("""insert into route(rid,stid,station_name)values({},{},"{}")""".format(routef.get(),snf.get(),staion_id_f.get()))
            con.commit()

            op1 = Label(root, text='{} {} {} '.format(routef.get(), snf.get(), staion_id_f.get()),font='Arial 12')
            op1.grid(row=6, columnspan=13)
            showinfo('Operator Entry Updated', 'Bus Route Added successfully')


        def checking():
            cur.execute("SELECT * FROM route")
            f=cur.fetchall()
            print(f)

        Routeid = Label(root, text='Route ID', font='Arial 14')
        station_name = Label(root, text='Origin Station', font='Arial 14')
        Station_id = Label(root, text='Destination Station', font='Arial 14')

        routef = Entry(root)
        snf = Entry(root)
        staion_id_f = Entry(root)



        addb = Button(root, text='Add Route', bg='SpringGreen2', font='Arial 14', command=addnew)
        eb = Button(root, text='Delete Route', bg='SpringGreen2',fg='Red', font='Arial 14')


        #check_db = Button(root, text='Check', bg='SpringGreen2', font='Arial 14', command=checking)
        #check_db.grid(row=10, column=11)

        Routeid.grid(row=5, column=3)
        routef.grid(row=5, column=4)
        station_name.grid(row=5, column=5)
        snf.grid(row=5, column=6)
        Station_id.grid(row=5, column=7)
        staion_id_f.grid(row=5, column=8)
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


        def datecorrect():
            olddate = datef.get()
            newdate = olddate[6:] + '-' + olddate[3:5] + '-' + olddate[:2]
            return newdate

        import sqlite3

        con = sqlite3.connect('PYthonBusProj.db')
        cur = con.cursor()


        Busid = Label(root, text='Bus ID', font='Arial 14')
        date = Label(root, text='Running Date', font='Arial 14')
        avail = Label(root, text='Seat Available', font='Arial 14')

        bidf = Entry(root)
        datef = Entry(root)
        availf = Entry(root)


        def addnew():
            date = 0
            date = cur.fetchall()
            date = datecorrect()
            cur.execute("""insert into runs(runs_busID,runs_date,seat_available)values({},'{}',{})""".format(bidf.get(), date,
                                                                                                availf.get()))
            con.commit()


            op1 = Label(root, text='{} {} {} '.format(bidf.get(), datef.get(), availf.get()),
                        font='Arial 12')
            op1.grid(row=6, columnspan=13)
            showinfo('Operator Entry Updated', 'Bus Running Record updated successfully')


        def checking():
            cur.execute("SELECT * FROM runs")
            f=cur.fetchall()
            print(f)

        addb = Button(root, text='Add Run', bg='SpringGreen2', font='Arial 14', command=addnew)
        eb = Button(root, text='Delete Run', bg='SpringGreen2',fg='Red', font='Arial 14')

        #check_db = Button(root, text='Check', bg='SpringGreen2', font='Arial 14', command=checking)
        #check_db.grid(row=10, column=11)

        Busid.grid(row=5, column=3)
        bidf.grid(row=5, column=4)
        date.grid(row=5, column=5)
        datef.grid(row=5, column=6)
        avail.grid(row=5, column=7)
        availf.grid(row=5, column=8)
        addb.grid(row=5, column=9)
        eb.grid(row=5, column=10)

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
        
        Label(fr3,text="Sation ID", font='arial 12 ').grid(row=0,column=0,padx=10)
        sId_entry=Entry(fr3)
        sId_entry.grid(row=0,column=1,padx=10)
        
        Label(fr3,text="Sation Name", font='arial 12 ').grid(row=0,column=2,padx=10)
        sName_entry=Entry(fr3)
        sName_entry.grid(row=0,column=3,padx=10)
        
        add_button=Button(fr3,text="Add", bg="green2")
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



d=demo()
d.main_window()


