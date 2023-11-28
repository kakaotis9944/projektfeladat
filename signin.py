from tkinter import *
from tkinter import messagebox
import random

timeleft=60
def timer():
    global timeleft, i
    if timeleft>0:
        timeleft-=1
        timerLabel.config(text=timeleft)
        timerLabel.after(1000,timer)
    else:
        wordEntry.config(state=DISABLED)
        result=score-miss
        instructionLabel.config(text=f"Sikeres {score}\n Sikertelen {miss}\n Pont {result}")
        if result<15:
            emoji1Label.config(image=sad)
        if result>15:
            emoji1Label.config(image=happy)
        if result>20:
            emoji1Label.config(image=pro)
        res=messagebox.askyesno("Megerősítés", "Szeretnél még játszani?")
        if res:
            i=0
            timeleft=60
            countLabel.config(text="0")
            timerLabel.config(text="60")
            wordEntry.config(state=NORMAL)
            instructionLabel.config(text="Írd be a szót és nyomd meg az Entert")
            emoji1Label.place_forget()
        else:
            root.destroy()



i=0
score=0
miss=0
def start_game(event):
    if wordEntry.get()!="":
        global i, score, miss
        i+=1
        countLabel.config(text=i)
        instructionLabel.config(text="")
        if timeleft==60:
            timer()
        if wordEntry.get()==word_list_Label["text"]:
            score+=1
        else:
            miss+=1
        random.shuffle(word_list)
        word_list_Label.config(text=word_list[0])
        wordEntry.delete(0, END)



#Szavak
word_list=["keyboard", "mouse", "ant"]

#Függvények
sliderwords = ""
count = 0
def slider():
    global sliderwords, count
    text = "Figyelj a gyorsaságra és a helyességre!"
    if count>=len(text):
        count=0
        sliderwords=""
    sliderwords = sliderwords+text[count]
    movingLabel.config(text=sliderwords)
    count+=1
    movingLabel.after(250, slider)

#GUI rész
root = Tk()
root.title("Gyorsasági játék")
root.iconbitmap("icon.ico")
root.geometry("700x600+550+150")
root.config(bg="lightgray")
root.resizable(0,0)
logoImage = PhotoImage(file="logo.png")
logoLabel = Label(root, image=logoImage, bg="lightgray")
logoLabel.place(x=200, y=50)

movingLabel = Label(root, text="", bg="lightgray", font=("Arial", 25, "bold italic"), width=35, fg="red")
movingLabel.place(x=10, y=10)
slider()

random.shuffle(word_list)
word_list_Label=Label(root,text=word_list[0], font=("cooper black", 38, "italic bold"), bg="lightgray")
word_list_Label.place(x=350,y=350, anchor=CENTER)

wordLabel=Label(root,text="Szavak",font=("Castellar",28,"bold"), bg="lightgray")
wordLabel.place(x=500,y=150)

countLabel=Label(root,text=i,font=("Castellar",28,"bold"), bg="lightgray")
countLabel.place(x=570,y=220)

timeLabel=Label(root,text="Idő",font=("Castellar",28,"bold"), bg="lightgray")
timeLabel.place(x=70,y=150)

timerLabel=Label(root,text="60",font=("Castellar",28,"bold"), bg="lightgray")
timerLabel.place(x=80,y=220)

wordEntry=Entry(root, font=("arial", 25), bd=5, justify=CENTER)
wordEntry.place(x=170, y=390)
wordEntry.focus_set()

instructionLabel=Label(root,text="Írd be a szót és nyomd meg az Entert", font=("Chiller",28,"bold"),bg="lightgray", fg="red")
instructionLabel.place(x=125, y=460)

sad=PhotoImage(file="sad.png")
happy=PhotoImage(file="happy.png")
pro=PhotoImage(file="pro.png")

emoji1Label=Label(root,bg="lightgray")
emoji1Label.place(x=500, y=500)


root.bind("<Return>", start_game)
root.mainloop()
