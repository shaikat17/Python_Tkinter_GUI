BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random


current_data = {}
learn_list = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    #print(original_data)
    learn_list = original_data.to_dict(orient="records")
else:
    learn_list = data.to_dict(orient="records")


def next_card():
	global current_data, window_timer
	window.after_cancel(window_timer)
	current_data = random.choice(learn_list)
	canvas.itemconfig(current_title, text="French", fill="black")
	canvas.itemconfig(current_word, text=current_data['French'], fill="black")
	canvas.itemconfig(card_back, image=card_front_img)
	window_timer = window.after(3000, func=flip_card)

def flip_card():
	canvas.itemconfig(current_title, text="English", fill="white")
	canvas.itemconfig(current_word, text=current_data['English'], fill="white")
	canvas.itemconfig(card_back, image=card_back_img)
	
def is_known():
    learn_list.remove(current_data)
    #print(len(learn_list))
    data = pd.DataFrame(learn_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_back = canvas.create_image(400, 263, image=card_front_img)
current_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
current_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
check_image = PhotoImage(file="./images/right.png")

unknown_btn = Button(image=cross_image, command=next_card)
unknown_btn.grid(row=1, column=0)

known_btn = Button(image=check_image, command=is_known)
known_btn.grid(row=1, column=1)

next_card()

window.mainloop()
