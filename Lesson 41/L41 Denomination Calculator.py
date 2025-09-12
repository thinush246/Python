from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Main Window
window = Tk()
window.title("Denomination Counter")
window.config(bg="aqua")
window.geometry("650x400")

# Image
upload = Image.open("Lesson 41/app-image.jpeg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(window, image=image, bg="light blue")
label.place(x=180, y=20)

# Welcome Label
label1 = Label(
    window,
    text="Hello, Welcome to Denomination Counter Application.",
    bg="aqua"
)
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to show messagebox
def msg():
    MsgBox = messagebox.askquestion(
        "Alert", "Do you want to calculate the denomination count?"
    )
    if MsgBox == "yes":
        topwin()

# Button
button1 = Button(
    window,
    text="Let's get started!",
    command=msg,
    bg="green",
    fg="white"
)
button1.place(x=260, y=360)

# Top Window
def topwin():
    top = Toplevel()
    top.title("Denominations Counter")
    top.config(bg="light yellow")
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg="light yellow")
    entry = Entry(top)
    Lbl = Label(top, text="Here are number of notes for each denomination", bg="light yellow")

    L1 = Label(top, text="2000", bg="light yellow")
    L2 = Label(top, text="1000", bg="light yellow")
    L3 = Label(top, text="500", bg="light yellow")
    L4 = Label(top, text="100", bg="light yellow")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)

    def den_counter():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000

            note1000 = amount // 1000
            amount %= 1000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100

            # Clear old results
            for box in (t1, t2, t3, t4):
                box.delete(0, END)

            # Insert new results
            t1.insert(END, str(note2000))
            t2.insert(END, str(note1000))
            t3.insert(END, str(note500))
            t4.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    # Button
    btn = Button(top, text="Calculate", command=den_counter, bg="lime", fg="black")

    # Place Widgets
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    Lbl.place(x=140, y=170)

    L1.place(x=180, y=200)
    L2.place(x=180, y=230)
    L3.place(x=180, y=260)
    L4.place(x=180, y=290)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    t4.place(x=270, y=290)

window.mainloop()