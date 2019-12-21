from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import imageio
import os

root = Tk()
root.geometry('400x400')
root.title("Video to GIF Converter")
root.iconbitmap("icon.ico")

menuBar = Menu(root)
root.config(menu=menuBar)
t = Text(root, height=3, width=50)
t.pack()

t.insert(END, "File Path: ")
t.config(state=DISABLED)


def browse_file():
    try:
        global clip
        filename = filedialog.askopenfilename()
        print(filename)
        video, ext = os.path.splitext(filename)
        clip = os.path.abspath(filename)
        t.insert(END, video + "\nFile Type: " + ext)
        t.config(state=DISABLED)
    except Exception as e:
        print(e)


subMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo("About Us",
                                "This video to gif converter was built using Python 3.7 \ngithub.com/wonder-child")


subMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About us", command=about_us)


def convert():
    try:
        converter_text.set("Converting..")
        output_path = os.path.splitext(clip)[0] + '.gif'
        reader = imageio.get_reader(clip)
        fps = reader.get_meta_data()['fps']
        writer = imageio.get_writer(output_path, fps=fps)

        for frames in reader:
            writer.append_data(frames)

        writer.close()
        converter_text.set("Convert")
    except Exception as e:
        converter_text.set("Convert")
        print(e)


converter_text = StringVar()
converter_text.set("Convert")
converter = Button(root, textvariable=converter_text, command=convert)
converter.pack()

root.mainloop()
