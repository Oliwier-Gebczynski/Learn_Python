from tkinter import *


def show():
    printLogin = Label(window, text="Login: " +
                       loginInput.get()).grid(row=4, column=0)
    printPassword = Label(window, text="Password: " + passwordInput.get()
                          ).grid(row=4, column=1)


# main
window = Tk()
window.title("passBase")

# add small logo
window.iconbitmap('source\ico\key.ico')

# add text
helloText = Label(window, text="Hello in passBase!", bg="black", fg="white")
helloText.grid(row=0, column=1)

loginText = Label(window, text="Login: ", bg="black", fg="white")
loginText.grid(row=1, column=0)

passwordText = Label(window, text="Password: ", bg="black", fg="white")
passwordText.grid(row=2, column=0)

# inputs
loginInput = Entry(window)
loginInput.grid(row=1, column=2)

passwordInput = Entry(window)
passwordInput.grid(row=2, column=2)

# add button
submitBtn = Button(window, text="Submit", command=show)
submitBtn.grid(row=3, column=2)

window.mainloop()
