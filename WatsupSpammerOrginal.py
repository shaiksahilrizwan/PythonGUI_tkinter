from tkinter import *
#import pywhatkit
import pyautogui as spam
import time
root=Tk()
def wast():
    Label(text="Sending Message!").pack()
    number=ph.get()
    msg=ms.get()
    hrs=int(h.get())
    mins=int(m.get())+1
    limit=int(no.get())
    pywhatkit.sendwhatmsg(number,msg,hrs,mins)
    i=0

    time.sleep(1)
    while i<int(limit):
        spam.typewrite(msg)
        spam.press('enter')
        i+=1

    
root.title("Whatsapp Spam Automater")
root.geometry("900x550")
root.minsize(900,550)
root.maxsize(900,550)
texty=Label(text="WhatsApp Spam Bot!",font=("OnePlus Sans","14"),bg="Green",fg="White").pack(fill="x")
phone=Label(text="Enter Phone Number:",font=("OnePlus Sans","14"),fg="White",bg="Black").pack()
ph=StringVar()
phone1=Entry(textvariable=ph).pack()
msg=Label(text="Message You want to Send:",font=("OnePlus Sans","14")).pack(fill="x")
ms=StringVar()
msg1=Entry(textvariable=ms).pack()
hrs=Label(text="When You want to send (Time in Hrs) should type the current time:",font=("OnePlus Sans","14")).pack(fill="x")
h=StringVar()
hrs1=Entry(textvariable=h).pack()
mins=Label(text="(Time in Mins should type the current time):",font=("OnePlus Sans","14")).pack(fill="x")
m=StringVar()
mins1=Entry(textvariable=m).pack()
n=Label(text="Enter the number of messages you want to Spam:").pack()
no=StringVar()
n1=Entry(textvariable=no).pack()
Checkbutton(text="Ready to send message").pack(fill="x")
Button(text="Send Message>",command=wast,bg="blue",fg="White").pack()
Label(text='   ').pack()
Label(text='   ').pack()
Label(text="Before Use Note :",font=("OnePlus Sans","14"),fg='white',bg='red').pack()
Label(text="Enter the Phone Number with country Code Like +91 323XXXXXXX",font=("OnePlus Sans","14")).pack()
Label(text="Login to whatsapp for web because the message will be sent by whatsapp for web only",font=("OnePlus Sans","14")).pack()
Label(text="The Time should be entered only in 24Hrs format",font=("OnePlus Sans","14")).pack()
Label(text="You should enter only present time and the message will be spamed in next 2-3 mins depending of time").pack()
Label(text='   ').pack()
Label(text='This GUI Application is designed by VIT-AP student').pack()
root.mainloop
