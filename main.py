from tkinter import *
from morse import MorseCode

translate = MorseCode()

def morse_code():
    text = e.get()
    print(text)
    e.delete(0, END)
    e.insert(0, translate.to_morse(text))

# UI SETUP
root = Tk()
root.title("Morse Code Converter")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
e.focus()

morse = Button(root, text="To Morse", command=morse_code).grid(row=1, column=0)
exit = Button(root, text="Exit", command=root.quit).grid(row=1, column=1)
english = Button(root, text="To English").grid(row=1, column=2)

root.mainloop()