import webbrowser
from tkinter import *

root = Tk( )

root.title('Abrir Browser')
root.geometry('300x200')

def github():
	webbrowser.open('https://github.com/JoseAntonioIosephvsAnthonivs')

mygithub = Button(root, text='Abrir meu Github', command=github).pack(pady=20)
root.mainloop()