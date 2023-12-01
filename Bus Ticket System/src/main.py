from tkinter import *
from tkinter.messagebox import *

class Bus_Booking():
    #Home page
    def home(self):
        root = Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        root.title('Seat Booking Page')
        bus=PhotoImage(file="../assets/bus.png")
        Label(root, image=bus).grid(row=0,column=0,columnspan=10,padx=w//2.5)
        Label(root, text="Online Bus Booking System",font=("Arial", 30,"bold"),bg= "sky blue", fg= "red2").grid(row=1,column=1,columnspan=10,padx=w//3)


        def gobbook(e=0):
            root.destroy()
            self.Bus_Booking()


        def checkbooking(e=0):
            root.destroy()
            self.Check_Your_Booking()


        def addbusdetail(e=0):
            root.destroy()
            self.Admins_Only()

        seat_booking = Button(root, text = 'Seat Booking',font=("Arial", 25,),bg= "pale green", fg= "gray5",command=gobbook).grid(row=3,column=3,pady=70)
        check  = Button(root, text = 'Checked Booked Seat',font=("Arial", 25),bg= "lime green", fg= "gray5",command=checkbooking).grid(row=3,column=5,pady=70)
        Add_detail = Button(root, text = 'Add Bus Detail',font=("Arial", 25), fg= "gray5",command=addbusdetail).grid(row=3,column=7,pady=70)
        admins_only = Label(root, text='For Admin Only',font=("Arial", 16), fg= "red2").grid(row=4,column=7)
        root.mainloop()

    def Bus_Booking(self):
        root = Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        frame_1 = Frame(root)
        frame_1.grid(row=6,column=0,columnspan=20)
        root.title('Booking of bus')
        bus=PhotoImage(file="../assets/bus.png")
        Label(root, image=bus).grid(row=0,column=0,columnspan=20,padx=w//2.5)
        home=PhotoImage(file="../assets/home.png")
        Label(root, text="Online Bus Booking System",font=("Arial", 30,"bold"),bg= "sky blue", fg= "red2").grid(row=1,column=0,columnspan=20,padx=w//3)
        Label(root,text = "Entry Journey Details",font=("Arial", 20,"bold"),bg= "SpringGreen2", fg= "green4").grid(row=2,column=0,columnspan=20,pady=20)
        to=Label(root,text="To",font=("Arial", 15,"bold"), fg= "gray5").grid(row=3,column=3,pady=20,sticky='E')
        From=Label(root,text="From",font=("Arial", 15,"bold"), fg= "gray5").grid(row=3,column=5,pady=20,sticky='E')
        Journey_Date=Label(root,text="Journey Date",font=("Arial", 15,"bold"), fg= "gray5").grid(row=3,column=7,pady=20,sticky='E')
        tof=Entry(root)
        fromf=Entry(root)
        datef=Entry(root)
        tof.grid(row=3,column=4,pady=20,sticky='W')
        fromf.grid(row=3,column=6,pady=20,sticky='W')
        datef.grid(row=3,column=8,pady=20,sticky='W')
        v = StringVar(root, "1")

        import sqlite3

        con = sqlite3.connect('pythonbus.db')
        cur = con.cursor()

        def call():
            res = mb.askquestion('Fare Confirm',
                                'Total amount to be paid Rs.3000.00')

            if res == 'yes':
                root.destroy()
            else:
                mb.showinfo('Return', 'Your Seat is Not Booked')

        # Details Of Passengers
        def proceed_1():
            fill_detail = Label(frame_1, text="Fill Passenger Detail To Book The Bus Ticket", font=("Arial", 30, "bold"),bg="sky blue", fg="red2")
            fill_detail.grid(row=6, column=0,columnspan=10,pady=20)
            Name_pas = Label(root, text="Name", font=("Arial", 15, "bold"), fg="gray5")
            Name_pas.grid(row=8, column=3, pady=20, sticky='E')
            a1 = Entry(root)
            a1.grid(row=8, column=4, pady=20, sticky='W')
            Gender_1 = Label(root, text="Gender", font=("Arial", 15, "bold"), fg="gray5")
            Gender_1.grid(row=8, column=5, pady=20, sticky='E')
            options = [
                "Male",
                "Female",
                "Transgender",
                "Prefer not to say"
            ]
            clicked = StringVar()
            clicked.set("Male")
            drop = OptionMenu(root, clicked, *options)
            drop.grid(row=8, column=6, pady=20, sticky='W')
            Num_seat = Label(root, text="No. of Seats", font=("Arial", 15, "bold"), fg="gray5")
            Num_seat.grid(row=8, column=6, pady=20, sticky='E')
            b1 = Entry(root)
            b1.grid(row=8, column=7, pady=20, sticky='W')
            Mob = Label(root, text="Mobile", font=("Arial", 15, "bold"), fg="gray5")
            Mob.grid(row=8, column=7, pady=20, sticky='E')
            c1 = Entry(root)
            c1.grid(row=8, column=8, pady=20, sticky='W')
            Age = Label(root, text="Age", font=("Arial", 15, "bold"), fg="gray5")
            Age.grid(row=8, column=8, pady=20, sticky='E')
            d1 = Entry(root)
            d1.grid(row=8, column=9, pady=20, sticky='W')
            Book_seat = Button(root, text="Book seat", font=("Arial", 15,), background="pale green", fg="gray5",command=call)
            Book_seat.grid(row=8, column=10, pady=20)

        #Date Correction
        def datecorrect():
            olddate = datef.get()
            newdate = olddate[6:] + '-' + olddate[3:5] + '-' + olddate[:2]
            return newdate

        #Journey Detail
        def detail():
            select_bus = Label(root, text="Select Bus", font=("Arial", 15), fg="green4")
            select_bus.grid(row=4, column=4, pady=20)
            operatoR = Label(root, text="Operator", font=("Arial", 15), fg="green4")
            operatoR.grid(row=4, column=5, pady=20)
            bus_type = Label(root, text="Bus Type", font=("Arial", 15), fg="green4")
            bus_type.grid(row=4, column=6, pady=20)
            avail = Label(root, text="Available/capacity", font=("Arial", 15), fg="green4")
            avail.grid(row=4, column=7, pady=20)
            fare = Label(root, text="Fare", font=("Arial", 15), fg="green4")
            fare.grid(row=4, column=8, pady=20)
            values = {"Bus 1": "0"}
            for (text, value) in values.items():
                Radiobutton(root, text=text, variable=v,
                            value=value, indicator=0,background="light blue").grid(row=5, column=4, pady=20, sticky='W')
                        
            dated = datecorrect()
            cur.execute(
                """select op.name,b.bus_type,r.seat_available,b.capacity,b.fare,b.bus_opid,st.stid as start_st,ed.stid as end_st from operator as op,bus as b,route as st,route as ed,runs as r where r.runs_date='{}' and st.station_name="{}" and ed.station_name="{}" and st.stid< ed.stid and st.rid=ed.rid and b.bus_rid=st.rid and b.bus_opid=op.opid and r.runs_busid=b.busid""".format(
                    dated, fromf.get(), tof.get()))
            res = cur.fetchall()
            buses_count = len(res)

            name_operator = Label(root, text="Palak", font=("Arial", 15, "italic"), fg="medium blue")
            name_operator.grid(row=5, column=5, pady=20)
            b_type = Label(root, text="AC 2x3", font=("Arial", 15), fg="medium blue")
            b_type.grid(row=5, column=6, pady=20)
            capacity = Label(root, text="23/40", font=("Arial", 15), fg="medium blue")
            capacity.grid(row=5, column=7, pady=20)
            fee = Label(root, text="1499", font=("Arial", 15), fg="medium blue")
            fee.grid(row=5, column=8, pady=20)
            proceed = Button(root, text="Proceed To Book", font=("Arial", 15,), bg="pale green", fg="gray5", command=proceed_1)
            proceed.grid(row=5, column=9, pady=20)

        show_bus = Button(root,text="Show Bus",font=("Arial", 15,),bg= "pale green", fg= "gray5",command=detail)
        show_bus.grid(row=3,column=9,pady=20)

        def go_home():
            root.destroy()
            self.home
        home_button = Button(root,timage=home, command=go_home)
        home_button.grid(row=3,column=11,pady=20,sticky='W')

        root.mainloop()
    
    def checkbooking(self):
        root = Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        frame1 = Frame(root,relief='groove',bd=5)
        frame1.grid(row=4, column=4, columnspan=12,pady=20)

        import sqlite3

        con = sqlite3.connect('PYthonBusProj.db')
        cur = con.cursor()

        def getvals():
            if len(mobf.get())==10:
                cur.execute("SELECT * FROM bookinghistory where mobile={}".format(int(mobf.get())))
                f = cur.fetchall()
                print(f)
                passe = 'Passenger Name:' + str(f[0][0])
                gender = 'gender:' + str(f[0][8])
                nofs = 'No. of Seats:' + str(f[0][3])
                mob = 'Phone:' + str(f[0][1])
                age = 'Age:' + str(f[0][2])
                Fare = 'Fare:' + str(f[0][10])
                refno = 'Booking No.:' + str(f[0][8])
                oper = 'Bus Detail:' + str(f[0][11])
                travd = 'Travel Date:' + str(f[0][9])
                bookd = 'Booking Date:' + str(f[0][6])
                desti = 'Destination:' + str(f[0][5])
                bp = 'Boarding Point:' + str(f[0][4])
                Label(frame1, text=passe, fg='grey5', font='Arial 15 bold').grid(row=4, column=0)
                Label(frame1, text=nofs, fg='grey5', font='Arial 15 bold').grid(row=5, column=0)
                Label(frame1, text=age, fg='grey5', font='Arial 15 bold').grid(row=6, column=0)
                Label(frame1, text=refno, fg='grey5', font='Arial 15 bold').grid(row=7, column=0)
                Label(frame1, text=travd, fg='grey5', font='Arial 15 bold').grid(row=8, column=0)
                Label(frame1, text=bp, fg='grey5', font='Arial 15 bold').grid(row=9, column=0)
                Label(frame1, text=gender, fg='grey5', font='Arial 15 bold').grid(row=4, column=2)
                Label(frame1, text=mob, fg='grey5', font='Arial 15 bold').grid(row=5, column=2)
                Label(frame1, text=Fare, fg='grey5', font='Arial 15 bold').grid(row=6, column=2)
                Label(frame1, text=oper, fg='grey5', font='Arial 15 bold').grid(row=7, column=2)
                Label(frame1, text=bookd, fg='grey5', font='Arial 15 bold').grid(row=8, column=2)
                Label(frame1, text=desti, fg='grey5', font='Arial 15 bold').grid(row=9, column=2)

                Label(frame1, text='* Total amount Rs to be paid at the time of boarding the bus', fg='grey5',
                    font='Arial 15').grid(row=11, columnspan=20, column=0)

            else:

                showerror('phoneno', 'mobile number not valid')

        img = PhotoImage(file="bus.png")
        img1 = PhotoImage(file="home.png")
        bus = Label(root, image=img)
        bus.grid(row=0, column=0, columnspan=20, padx=w // 3)
        t1 = Label(root, text='Online Bus Booking System', bg='light blue', fg='Red', font='Arial 32 bold')
        t1.grid(row=1, column=0, columnspan=20, padx=w // 3)
        t2 = Label(root, text='Check Your Booking', bg='SpringGreen2', fg='green4', font='Arial 22 bold')
        t2.grid(row=2, column=0, columnspan=20, padx=w // 3, pady=20)

        mob = Label(root, text='Enter Your mobile number :', font='Arial 12')
        mobf = Entry(root)

        # Tkinter variable for storing entries
        #mobf = StringVar()

        #Entries for our form
        def checkbook():
            op1 = Label(root, text='Ticket Here', font='Arial 12')
            op1.grid(row=4, columnspan=20, padx=w // 3, )


        checkb = Button(root, text='Check Booking', font='Arial 14', command=getvals)

        #, command=checkbook

        mob.grid(row=3, column=8, sticky=E)  # sticky=W or E
        mobf.grid(row=3, column=9, sticky=EW, padx=5)
        checkb.grid(row=3, column=10, sticky=W)

        def go_Back():
            root.destroy()
            self.Bus_Booking()
        back_button = Button(root,text="Back", command=go_Back)
        back_button.grid(row=3,column=11,pady=20,sticky='W')

        def go_home():
            root.destroy()
            self.home()
        home=PhotoImage(file="../assets/home.png")
        home_button = Button(root,image=home, command=go_home)
        home_button.grid(row=3,column=12,pady=20,sticky='W')

        root.mainloop()

obj  = Bus_Booking()
obj.home()