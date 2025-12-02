from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")


def BMI():
    h=float(Height.get())
    w=float(Weight.get())
    
    #convert height into metr
    m=h/100
    bmi=round(float(w/m**2),1)
    Label1.config(text=bmi)
    
    #you can change value , because different countries have 
    
    if bmi<=18.5:
        Label2.config(text="UnderWeight!")
        Label3.config(text="You have lower weight then normal body!")
        
    elif bmi>18.5 and bmi<=25:
        Label2.config(text="Normal!")
        Label3.config(text="It indicates that you are healthy!")
     
    elif bmi>25 and bmi<=30:
        Label2.config(text="OverWeight!")
        Label3.config(text="It indicates that a person is \n slightly overWeight \n A doctor may advise to lose some \n weight for health reason!")
        
    else:  
        Label2.config(text="Obes")
        Label3.config(text="Health may be at risk, if they do not  \n lose we!")
                  
#icon

image_icon=PhotoImage(file="images/icon.png")
root.iconphoto(False,image_icon)

#top

top=PhotoImage(file="images/top.png")
top_image=Label(root,image=top, background="#f0f1f5")
top_image.place(x=-10,y=-10)


#bottom box

Label(root,width=72,height=35,bg="lightblue").pack(side=BOTTOM)

#two boxes

box=PhotoImage(file="images/box.png")
Label(root,image=box).place(x=20,y=100)
Label(root,image=box).place(x=240,y=100)

#scale

Scale=PhotoImage(file="images/scale12.png")
Label(root,image=Scale, bg="lightblue").place(x=20,y=310)

###########Slider1#############
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    
    
    size=int(float(get_current_value()))
    img=(Image.open("images/man.jpg"))
    resized_image=img.resize((70,40+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70,y=530-size)
    secondimage.image=photo2

#command to change bg color of scale
style = ttk.Style()
style.configure("TScale",background="white")
slider= ttk.Scale(root,from_=0, to=220,orient='horizontal',style="TScale",
                  command=slider_changed, variable=current_value)
slider.place(x=80,y=250)


##@@@@@@@Slider2@@@@
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

#command to change bg color of scale
style2 = ttk.Style()
style2.configure("TScale",background="white")
slider2= ttk.Scale(root,from_=0, to=200,orient='horizontal',style="TScale",
                  command=slider_changed2, variable=current_value2)
slider2.place(x=300,y=250)

#Entry box

Height=StringVar()
Weight=StringVar()
height=Entry(root,textvariable=Height,width=10,font='arial 21 bold',bg="#fff",fg="blue",bd=10,justify=CENTER)
height.place(x=35,y=160)
Height.set(get_current_value())

weight=Entry(root,textvariable=Weight,width=10,font='arial 21 bold',bg="white",fg="blue",bd=10,justify=CENTER)
weight.place(x=255,y=160)

Weight.set(current_value2.get())


#man image
secondimage=Label(root,bg="lightblue")
secondimage.place(x=70,y=530)



Button(root,text="Natija",width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=BMI).place(x=280,y=310)

Label1=Label(root,font="arial 60 bold", bg="lightblue",fg="#fff")
Label1.place(x=240,y=360)


Label2=Label(root,font="arial 20 bold ",bg="lightblue",fg="#3b3a3a")
Label2.place(x=300,y=450)


Label3=Label(root,font="arial 10 ",bg="lightblue",)
Label3.place(x=200,y=500)

Label4=Label(root,text="Uzunlik",font="arial 20 bold ",bg="lightblue",fg="#3b3a3a")
Label4.place(x=70,y=55)

Label5=Label(root,text="Og'irlik",font="arial 20 bold ",bg="lightblue",fg="#3b3a3a")
Label5.place(x=300,y=55)

root.mainloop()