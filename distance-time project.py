from tkinter import ttk,StringVar,messagebox
from tkinter import *


root=Tk()
root.title("distance speed and time")
root.geometry('670x400+0+0')
root.configure(background='grey')


#frames

Tops=Frame(root,width=1000,height=50,bd=16,relief="raise")
Tops.pack(side=TOP)
Tops1=Frame(root,width=1000,height=50,bd=16,relief="raise")
Tops1.pack(side=BOTTOM)
LeftInFrame=Frame(root,width=150,height=300,bd=8,relief="raise")
LeftInFrame.pack(side=LEFT)
LeftMainFrame=Frame(root,width=150,height=300,bd=8,relief="raise")
LeftMainFrame.pack(side=LEFT)

RightMainFrame=Frame(root,width=300,height=300,bd=8,relief="raise")
RightMainFrame.pack(side=RIGHT)

#variables 
value0=StringVar()
check1=StringVar()
check2=StringVar()
check3=StringVar()
Distance=StringVar()
speed=StringVar()
time=StringVar()

#calculation

def ConDistance():
    if value0.get()=="Distance":
        convert1=float(speed.get())
        convert2=float(time.get())
        convert3=str('%.2f'%(convert1*convert2)),'km'
        Distance.set(convert3)
        check1.set('Speed')
        check2.set('Time')
        check3.set('Distance')
    elif (value0.get()=="Speed"):
        convert1=float(speed.get())
        convert2=float(time.get())
        convert3=str('%.2f'%(convert1/convert2)),'km/h'
        Distance.set(convert3)
        check1.set('Distance')
        check2.set('Time')
        check3.set('Speed') 
    elif (value0.get()=="Time"):
        convert1=float(speed.get())
        convert2=float(time.get())
        convert3=str('%.2f'%(convert1/convert2)),'hrs'
        Distance.set(convert3)
        check1.set('Distance')
        check2.set('Speed')
        check3.set('Time')
    elif (value0.get()==" "):
        messagebox.showinfo("Convert?","Make a selection?")


def Reset():
    value0.set("")
    Distance.set("")
    check1.set("")
    check2.set("")
    check3.set("")
    speed.set("")
    time.set("")
    
def qExit():
    qExit=messagebox.askyesno("Exit System","Do you want to quit")
    if qExit>0:
        root.destroy()
        return 



lblMiles=Label(Tops,font=('arial',40,'bold'),text='Distance Speed and Time',padx=2,pady=2,bd=2,fg="black",)
lblMiles.grid(row=0,column=2)




box=ttk.Combobox(LeftMainFrame,textvariable=value0,state="readonly",font=('arial',20,'bold'),width=13)
box['values']=(' ','Distance','Speed','Time')
box.current(0)
box.grid(row=0,column=0)

Entspeed=Entry(LeftMainFrame,font=('arial',20,'bold'),textvariable=speed,bd=2,width=15,justify='center')
Entspeed.grid(row=1,column=0)
Enttime=Entry(LeftMainFrame,font=('arial',20,'bold'),textvariable=time,bd=2,width=15,justify='center')
Enttime.grid(row=2,column=0)

lblConvert=Label(LeftMainFrame,font=('arial',20,'bold'),textvariable=Distance,bd=2,width=13,bg='white',pady=2,padx=2,relief='sunken')
lblConvert.grid(row=3,column=0)
lbldown=Label(Tops1,font=('arial',10,'bold'),text="NOTE : "+'\n'+"1) If you want distance then first enter speed and then time. "+'\n'+"2) If you want speed then first enter distance and then time. "+'\n'+"3) If you want time then first enter distance and then speed.",padx=2,pady=2,bd=2,fg="red",)
lbldown.grid(row=0,column=2)



lblSpace=Label(LeftInFrame,font=('arial veranda',20,'bold'),bd=2,width=13,pady=2,padx=2,fg="red",bg="yellow",text="Search")
lblSpace.grid(row=0,column=0)
lblConvert=Label(LeftInFrame,font=('arial',20,'bold'),textvariable=check1,bd=2,width=13,pady=2,padx=2,relief='sunken')
lblConvert.grid(row=1,column=0)
lblConvert=Label(LeftInFrame,font=('arial',20,'bold'),textvariable=check2,bd=2,width=13,pady=2,padx=2,relief='sunken')
lblConvert.grid(row=2,column=0)
lblConvert=Label(LeftInFrame,font=('arial',20,'bold'),textvariable=check3,bd=2,width=13,pady=2,padx=2,relief='sunken')
lblConvert.grid(row=3,column=0)


#buttons

btnConvert=Button(RightMainFrame,text='Convert',padx=2,pady=2,bd=2,fg="red",bg="yellow",font=('arial',18,'bold'),width=10,height=0,command=ConDistance).grid(row=1,column=0)
btnReset=Button(RightMainFrame,text='Reset',padx=2,pady=2,bd=2,fg="red",bg="yellow",font=('arial',18,'bold'),width=10,height=0,command=Reset).grid(row=2,column=0)
btnExit=Button(RightMainFrame,text='Exit',padx=2,pady=2,bd=2,fg="red",bg="yellow",font=('arial',18,'bold'),width=10,height=0,command=qExit).grid(row=3,column=0)


root.mainloop()
