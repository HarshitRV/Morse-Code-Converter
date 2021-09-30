from tkinter import *

# Configs
FONT_NAME = "Courier"

# Buttons function

def enter():
    normal_text = text_entry.get("1.0",'end-1c')
    morse_text = morse_entry.get("1.0",'end-1c')
    print(normal_text, morse_text)

    text_entry.delete("0", END)
    text_entry.insert("Herefiw iwefi oiwf")

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
convert_button = Button(window, text = 'Convert',command = enter, background="red")
convert_button.grid(row=4, column=0)

window.mainloop()