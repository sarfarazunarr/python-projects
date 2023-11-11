from tkinter import *
from tkinter.messagebox import showerror
import pybase64   #Download it

# Function will encrypt data when user click on enc_btn.
def Encrypt_date():
  # Declare message and password as global variable in mainfunction.
    message = entry1.get(1.0, END)
    password = str(entry2.get()) #Don't add index value

    if password == "PASSWORD": #ADD YOUR OWN PASSWORD
        en_msg = message.encode('ascii')
        data_row = pybase64.b64encode(en_msg)
        sec = data_row.decode('ascii')

        win1 = Toplevel()
        win1.geometry('300x300')
        win1.resizable(False, False)
        win1.config(bg='black')
        win1.title('Encrypted Message')
        secured_msg = Text(win1, font=('Verdana', 10))
        secured_msg.insert(1.0, sec)
        secured_msg.place(x=20, y=20, height=260, width=260)
        win1.mainloop()
    else:
        showerror('Wrong Password', 'Please Enter Valid Password')

def Decrypt_data():
    message = entry1.get(1.0, END)
    password = str(entry2.get())

    if password == "123":
        en_msg = message.encode('ascii')
        data_row = pybase64.b64decode(en_msg)
        sec = data_row.decode('ascii')

        win1 = Toplevel()
        win1.geometry('300x300')
        win1.resizable(False, False)
        win1.config(bg='black')
        win1.title('Decrypted Message')
        secured_msg = Text(win1, font=('Verdana', 10))
        secured_msg.insert(1.0, sec)
        secured_msg.place(x=20, y=20, height=260, width=260)
        win1.mainloop()
    else:
        showerror('Wrong Password', 'Please Enter Valid Password')

def reset():
    entry1.delete(1.0, END)
    entry2.delete(0, END)


def main_win():
    global entry1, entry2

    win = Tk()
    win.title('Secure it')
    win.config(bg='black')
    win.geometry('500x600')

    Label1 = Label(win, text='ENTER YOUR MESSAGE', font=('Verdana', 15), bg='black', fg='white')
    Label1.place(x=15, y=20, height=40, width=250)

    entry1 = Text(win,  font=('Times New Roman', 20))
    entry1.place(x=20, y=70, height=200, width=460)

    Label2 = Label(win, text='ENTER PASSWORD', font=('Verdana', 15), bg='black', fg='white')
    Label2.place(x=20, y=280, height=40, width=200)

    entry2 = Entry(win,  font=('Times New Roman', 20), show='*')
    entry2.place(x=20, y=320, height=50, width=460)

    enc_btn = Button(win, text='Encrypt', font=('Calibri', 13), bg='green', fg='white', command=Encrypt_date)
    enc_btn.place(x=140, y=390, height=30, width=100)

    dec_btn = Button(win, text='Decrypt', font=('Calibri', 13), bg='red', fg='white', command=Decrypt_data)
    dec_btn.place(x=260, y=390, height=30, width=100)

    res_btn = Button(win, text='Reset', font=('Calibri', 13), bg='yellow', fg='black', command=reset)
    res_btn.place(x=120, y=430, height=30, width=280)


    name = Label(win, text='SecureIt', font=('Bahnschrift Condensed', 35, 'bold'), bg='black', fg='red')
    name.place(x=150, y=470, height=40, width=200)
    author = Label(win, text='Designed By Sarfaraz', font=('Agency FB', 15), bg='black', fg='white')
    author.place(x=150, y=510, height=40, width=200)
    win.mainloop()
main_win()
