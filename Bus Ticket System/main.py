from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
#Adding Image
bus=PhotoImage(file='.//Bus_for_project.png')

#Adding Frames
fr1=Frame(root)
fr1.grid(row=0,column=0,columnspan=10)
fr2=Frame(root)
fr2.grid(row=1,column=0,columnspan=10)

#Adding Project Name
Label(fr1,image=bus).grid(row=0,column=0,padx=w//2.4)
Label(fr2,text="Online Bus Booking System",font='arial 30 bold',fg="Red",bg="Light Blue").grid(row=1,column=2,pady=50)

#Adding Details
Label(fr2,text="Name:Vaibhav Anand",fg="blue",font='arial 20 bold').grid(row=2,column=2)
Label(fr2,text="Er: 221B426",fg="blue",font='arial 20 bold').grid(row=3,column=2)
Label(fr2,text="Mobile:8423859380",fg="blue",font='arial 20 bold').grid(row=4,column=2)
Label(fr2,text="Submitted to: Dr. Mahesh Kumar",fg="Red",bg="Light Blue",font='arial 30 bold').grid(row=5,column=2,pady=40)
Label(fr2,text="Project Based Learning",fg="red",font='arial 20 bold').grid(row=6,column=2)

#Moving to next window with keypress
def changewindow(event):
    root.destroy()
    import book_or_edit
root.bind("<KeyPress>",changewindow)

root.mainloop()
