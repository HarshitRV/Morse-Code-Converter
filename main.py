from tkinter import *
from tkinter.ttk import *

style = Style()

style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'red')
# Configs
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Buttons function

def enter():
    pass

# UI SETUP

window = Tk()
window.title("Morse Code Converter")
window.geometry("600x600")
window.config(padx=30, pady=30)

# Label enter text
enter_text = Label(text="English Text", font=(FONT_NAME, 30, "bold"))
enter_text.grid(row=0, column=0)

# Entry text
text_entry = Text(width=70,height=10,highlightcolor="black")
text_entry.grid(row=1,column=0,columnspan=1)
text_entry.config(highlightcolor="black", highlightbackground="black")

# Label enter morse
enter_morse_text = Label(text="Morse Code", font=(FONT_NAME, 30, "bold"))
enter_morse_text.grid(row=2, column=0)

# Entry morse
morse_entry = Text(width=70,height=10,highlightcolor="black")
morse_entry.grid(row=3,column=0,columnspan=1)
morse_entry.config(highlightcolor="black", highlightbackground="black")

# Buttons
convert_button = Button(window, text = 'Quit !',
                style = 'W.TButton',
             command = enter)
convert_button.grid(row=4, column=0)

window.mainloop()

# from morse import MorseCode

# translate = MorseCode()

# message = input("Enter a message: ")

# encoded_message = translate.to_morse(message)

# print(encoded_message)

# decode = encoded_message

# decoded_message = translate.to_english(decode)

# print(decoded_message)