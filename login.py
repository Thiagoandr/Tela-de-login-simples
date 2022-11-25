from tkinter import *

login = Tk()
login.title("")
login.geometry("460x560")
login.resizable(False,False)

proteja_senha= StringVar()

img_fundo = PhotoImage(file="desktop\\fundo1.png")


lab_fundo = Label(login,image=img_fundo)
lab_fundo.pack()


login_email = Entry(login, bd=2, font=("arial",10))
login_email.place(width=390, height=45, x=39, y=210)
login_email = Entry(login, bd=2, font=("arial",10))
login_senha = Entry(login, textvariable=proteja_senha, show="x", bd=2, font=("arial",10))
login_senha.place(width=390, height=45, x=39, y=320)

botao_entrar= Button(login, text="Entrar", bg='blue',)
botao_entrar.place(width=160, height=60, x=149, y=460)


login.mainloop()
