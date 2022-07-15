from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image as image


root = Tk()
root.title("Image conversion")
#root.iconbitmap("logo.ico")
root.geometry("500x650")
root.configure(bg="#1b1b21")

# create the function that will convert from png to jpg
def pngTojpg():
    global picture

    for item in frame.winfo_children():
        item.destroy()

    root.filename = filedialog.askopenfilename(title="Choose a picture", filetypes= (("png files", "*.png"), ("all tyopes", "*.*")))
    if root.filename != '':
        png_pic = image.open(root.filename)
        r_png_pic = png_pic.resize((450, 500), image.ANTIALIAS)
        picture = ImageTk.PhotoImage(r_png_pic)

        lab = Label(frame, image=picture)
        lab.pack()

        if file_name.get() == '':
            lab.destroy()
            error = Label(root, text="Enter your file name please", fg="red", bg="#1b1b21", padx=40)
            error.grid(row=3, column=0, columnspan=2)
        else:
            with open((root.filename), "rb") as pic:
                b_pic = pic.read()
            with open((file_name.get() + ".jpg"), "wb") as n_pic:
                jpg_pic = n_pic.write(b_pic)
            save = Label(root, text="Your picture is saved successfully", fg="white", bg="#1b1b21", padx=40)
            save.grid(row=3, column=0, columnspan=2)

# create the function that will convert from jpg to png
def jpgTopng():
    global picture1

    for item in frame.winfo_children():
        item.destroy()

    root.filename = filedialog.askopenfilename(title="Choose a picture", filetypes= (("jpg files", "*.jpg"), ("all tyopes", "*.*")))
    if root.filename != '':
        jpg_pic = image.open(root.filename)
        r_jpg_pic = jpg_pic.resize((450, 500), image.ANTIALIAS)
        picture1 = ImageTk.PhotoImage(r_jpg_pic)

        lab = Label(frame, image=picture1)
        lab.pack()

        if file_name.get() == '':
            lab.destroy()
            error = Label(root, text="Enter your file name please", fg="red", bg="#1b1b21", padx=40)
            error.grid(row=3, column=0, columnspan=2)
        else:
            with open((root.filename), "rb") as pic:
                b_pic = pic.read()
            with open((file_name.get() + ".png"), "wb") as n_pic:
                png_pic = n_pic.write(b_pic)
            save = Label(root, text="Your picture is saved successfully", fg="white", bg="#1b1b21", padx=40)
            save.grid(row=3, column=0, columnspan=2)

def clearAll():
    for item in frame.winfo_children():
        item.destroy()
    file_name.delete(0, END)


# create a frame
frame = Frame(root, width=450, height=500)

# create the buttons
pngTojpg = Button(root, text="pngTjpg", padx=20, pady=7, font="none 12 bold", command=pngTojpg)
clear = Button(root, text="clear", padx=20, pady=7, font="none 12 bold", command=clearAll)
jpgTopng = Button(root, text="jpgTopng", padx=20, pady=7, font="none 12 bold", command=jpgTopng)

# create a label for the file name
file_name_label = Label(root, text="file name", bg="#1b1b21", font="propaganda 12 bold")

#create an entry for the file name
file_name = Entry(root, font="none 12 bold")

frame.grid(row=0, column=0, columnspan=3, padx=27, pady=(2,5))
pngTojpg.grid(row=1, column=0)
clear.grid(row=1, column=1)
jpgTopng.grid(row=1, column=2)
file_name_label.grid(row=2, column=0, pady=(20,0))
file_name.grid(row=2, column=1, pady=(20,0))

root.mainloop()
