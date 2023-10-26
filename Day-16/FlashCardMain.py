from tkinter import *
import pandas
import time
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("100DayOfCodePython\Day-16\Words\FrenchWords.csv")
# print(data)
data = data.to_dict(orient="records") # to reform the dictionary to desired form({french:word, english:word})
# print(data)
# print(data["French"][10])
# print(data["English"][10])
ch = {}


# making flashCards
def MakeFlashCard():
    global ch, flip_timer
    window.after_cancel(flip_timer)
    ch = random.choice(data)
    canvas.itemconfig(canvas_title, text=f"French", fill="black")
    canvas.itemconfig(canvas_word, text=f"{ch['French']}", fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, FlipCard)

def FlipCard():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(canvas_title, text=f"English", fill="white")
    canvas.itemconfig(canvas_word, text=f"{ch['English']}", fill="white")


# ---------------------------------------UI Setup------------------------------------------------------#
# window
window = Tk()
window.title("Flash Card Application")
window.minsize(width=900, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, FlipCard)
# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="100DayOfCodePython\Day-16\images\card_front.png")
back_img = PhotoImage(file="100DayOfCodePython\Day-16\images\card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "bold"), tag="title")
canvas_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"), tag="word")
canvas.grid(row=0, column=0, rowspan=3, columnspan=3)

# Buttons
ukimg = PhotoImage(file="100DayOfCodePython\Day-16\images\wrong.png")
unknown_Button = Button(image=ukimg)
unknown_Button.config(highlightthickness=0)
unknown_Button.grid(row=3, column=0)

kimg = PhotoImage(file="100DayOfCodePython\Day-16\images\correct.png")
known_Button = Button(image=kimg)
known_Button.config(highlightthickness=0)
known_Button.grid(row=3, column=2)

next_Button = Button(text="NEXT WORD!!", command=MakeFlashCard)
next_Button.config(highlightthickness=0)
next_Button.grid(row=3, column=1)

MakeFlashCard()

window.mainloop()