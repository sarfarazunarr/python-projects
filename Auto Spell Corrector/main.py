from tkinter import *
from textblob import TextBlob

def checkspelling():
    text = spell.get()
    checker = TextBlob(text)
    validspell = checker.correct()
    clearfield = correctspell.delete(0, END)
    correctspell.insert(0, validspell)

def start():
    global spell, correctspell
    win = Tk()
    win.title = 'Spelling Checker'
    win.config(bg='black')
    win.geometry('480x380')

    label1 = Label(win, text='Spelling Checker', font=('Bahnschrift', 30, 'bold'), bg='black', fg='white')
    label1.place(x=100, y=20, height=50, width=300)

    label1 = Label(win, text='Type any spell here 🔻🔻', font=('Bahnschrift', 15), bg='black', fg='white')
    label1.place(x=20, y=100, height=50, width=300)

    spell = Entry(win, font=('Bahnschrift', 12))
    spell.place(x=60, y=150, height=30, width=350)

    checkbtn = Button(win, text='Check Spell', font=('Bahnschrift', 12), bg='white', fg='black', command=checkspelling)
    checkbtn.place(x=290, y=190, height=40, width=120)

    label2 = Label(win, text='Corrected Spell', font=('Bahnschrift', 15), bg='black', fg='white')
    label2.place(x=60, y=230, height=50, width=150)

    correctspell = Entry(win, font=('Bahnschrift', 12))
    correctspell.place(x=60, y=280, height=30, width=350)


    win.mainloop()

start()
