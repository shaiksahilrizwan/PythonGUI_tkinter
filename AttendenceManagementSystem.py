import cv2#Importing the moduel
import numpy as np
from pyzbar.pyzbar import decode
from tkinter import *
from tkinter import filedialog# File explorer is on
from tkinter import messagebox 
def creatfile():#if file not created the command reaches here
    with open('Attendence.csv','w')as f: #creates the file in current directory
        f.write('Attendence')
def ender():
    messagebox.showinfo("Weit...","Saving data and closing")
    Label(root,text="Closing Please weit!!",font=("OnePlus Sans",10,"")).pack()
    root.destroy()
def checker(x):#checkes whether id belongs to UNIV
    list_of_courses=['BCE','BCS','BCD','MIC','MIS','BSC','MSC','BBA','LLB','PHD']
    if str(x[3:6]) in list_of_courses:
       return True#if and only is the student is from UNIV
    else:
       return False
def camopener():#cam opened
    #address=
    cp=cv2.VideoCapture(0)#you can use an ip camera also
    cp.set(3,640)
    cp.set(4,480)
    while True:
        success, im=cp.read()
        for codes in decode(im):
            x=(str(codes.data))
            datas=(x.replace('b',''))# data to decode
            y=checker(datas)#sending data for recognition
            if y==True:
                y=(50, 205, 50)
                datareceiver(datas)
            else:
                y=(0,0,0)
            pts=np.array([codes.polygon],np.int32)
            pts=pts.reshape((-1,1,2))
            cv2.polylines(im,[pts],True,y,10)
        if cv2.waitKey(1) & 0xFF==ord('x'):#programe stooper for cam
            break
        cv2.imshow("Attendence Camera",im)
        cv2.waitKey(1)
        mainstep()
    cp.release()
    cv2.destroyAllWindows()
def mainstep():#only be acceseed when file choosen
    framemiddle=Frame(root,bg="LightSteelBlue1",borderwidth=4,relief=SUNKEN)
    framemiddle.pack(fill=X)
    Label(framemiddle,text='CLICK THE BELOW TO START THE SESSION:',bg='light grey',fg='black',padx=10,pady=20,font=("OnePlus Sans",28,""),borderwidth=3).pack(fill=X)
    b4=Button(framemiddle,text='End the Session',bg="White",fg="Red",font=("OnePlus Sans",18,""),borderwidth=5,command=ender,padx=30).pack(side=BOTTOM)
    b3=Button(framemiddle,text='Start the Camera',bg="White",fg='blue',pady=20,padx=20,font=("OnePlus Sans",28,""),borderwidth=5,relief=GROOVE,command=camopener).pack(pady=200)
    
def filepath(x):#file path receiver 
    v=x
    z=(v[-1:-4:-1])
    if v=='' or (z[::-1])!='csv':#returns True if and only is the file extension is csv and file choosen
        messagebox.showinfo("Warning!!","No file is selected please select a file or wrong file selected")
    else:
        global p
        p=v
        return True
    #datareceiver(p)
def datareceiver(d):
    print(d)
    with open(p,'r') as f:
        c=f.readlines()
        if d+'\n' in c:
            pass
        else:
            with open(p,'a') as f:
                f.write(d+'\n')
            
def filecreation():
        #Selection Takes place here
        root.filename=filedialog.askopenfilename(initialdir=r"C:\\Users\\User\\Desktop",title="Select a file",filetypes=(("csv files","*.csv"),("all files","*.*")))
        if filepath(root.filename):
            mainstep()
def infobox():
    top=Toplevel()#InfoBox Dude
    top.minsize(640,360)
    top.title("Info Corner")
    top.geometry("640x360")
    Label(top,text="To take Attendence first you should choose a file").pack()
    Label(top,text="").pack()
    Label(top,text="Then you will get the option to open camera").pack()
    Label(top,text="").pack()
    Label(top,text="While Recording the attendence Green detection shows the Attendence marked").pack()
    Label(top,text="").pack()
    Label(top,text="Only open .CSV Extension for excel don't open xls type ").pack()
    Label(top,text="").pack()
    Label(top,text="Don't open file while taking attendence ").pack()
    Label(top,text="").pack()
    Label(top,text="""To End the Camera just palce the mouse key on camera window and press " x " Key """ ).pack()
    Label(top,text="").pack()
    Label(top,text="We will Soon reslove this issue").pack()
    Label(top,text="").pack()
    b4=Button(top,text="Tap to creat a .csv file",command=creatfile).pack()
    Label(top,text="This csv file will be created in current directory where this app is running").pack()
    Label(top,text="This is a GUI Application designed 22BCE*%&(").pack(side=BOTTOM)
    Label(top,text="").pack()
root=Tk()
root.title("Attendence Management System")
#root.iconbitmap(r"C:\\Users\\User\\Downloads\\icon.ico")
root.geometry("1280x720")                       
frame=Frame(root,bg="LightSteelBlue1",borderwidth=4,relief=SUNKEN)
frame.pack(fill=X)
root.minsize(1100,690)
root.maxsize(1290,730)
Label(frame,text="ID-Attendence",bg='light grey',fg='black',padx=10,pady=20,font=("OnePlus Sans",28,""),borderwidth=3,relief=SUNKEN).pack(fill=X)
#img=PhotoImage(file="LOGOs.png")
#Label(image=img,height=300,width=300).pack(padx=10)
#Label(frame,text='Use the Options Given below:',font=("Lucida Console",18)).pack()
frameleft=Frame(root,bg="LightSteelBlue1",borderwidth=4,relief=SUNKEN)
frameleft.pack(side=LEFT,fill=Y)
#framemiddle=Frame(root,bg="LightSteelBlue1",borderwidth=4,relief=SUNKEN)
#framemiddle.pack(fill=X)
#Label(framemiddle,text='CLICK THE BELOW TO START THE SESSION:',bg='light grey',fg='black',padx=10,pady=20,font=("OnePlus Sans",28,""),borderwidth=3).pack(fill=X)
Label(frameleft,text="Choose the file:",bg="white",fg='black',font=("OnePlus Sans",18,""),borderwidth=3,relief=SUNKEN).pack()
b1=Button(frameleft,fg="Red",bg="cornsilk1",text="Choose File",font=("OnePlus Sans",18,""),borderwidth=4,relief=GROOVE,command=filecreation).pack(pady=100)
b2=Button(frameleft,fg="Red",bg="cornsilk1",text="Info/About",font=("OnePlus Sans",18,""),borderwidth=4,relief=GROOVE,command=infobox).pack(pady=100)
#b3=Button(framemiddle,text='Start the Camera',bg="White",fg='blue',pady=20,padx=20,font=("OnePlus Sans",28,""),borderwidth=5,relief=GROOVE,command=camopener).pack(pady=200)
root.mainloop()
