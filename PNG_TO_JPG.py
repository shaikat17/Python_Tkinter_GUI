from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image, ImageTk

pngImage = ''

def open_png():
    global pngImage
    pngImage = fd.askopenfilename(title='Open PNG File', filetypes=[('image files','.png')])
    showField.insert(END, pngImage)
    
    showimg = Image.open(pngImage)
    showimg1 = showimg.resize((30, 30), Image.ANTIALIAS)
    showimage = ImageTk.PhotoImage(showimg1)
    label = Label(frame, image=showimage)
    label.pack()

def convert_to_jpg():
    pathname = os.path.dirname(pngImage)
    filename = os.path.basename(pngImage).split('.')[0] + '.jpg'
    savepath = os.path.join(pathname,filename)
    im = Image.open(pngImage)
    rgb_im = im.convert('RGB')
    rgb_im.save(savepath)
    
    showField.insert(END, 'Successful')
    print(savepath)
    

window = Tk()
window.geometry('300x200')
window.title('PNG to JPG')


btn  = Button(window, text='Open Png File', command=open_png).grid(column=0,row=0)

showField = Text(window, height=2,width=20)
showField.grid(column=1, row=0, padx=5, pady=5)

cnBtn = btn  = Button(window, text='Convert to JPG', command=convert_to_jpg).grid(column=0, columnspan=2,row=1, sticky = W+E)

frame = Frame(window, text='hello', width=100, height=100)
frame.grid(row=3,column=0, columnspan=2)

window.mainloop()
