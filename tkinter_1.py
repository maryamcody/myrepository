from tkinter import *
window= Tk()
window.title("My window")
window.geometry("300x300")

greeting =Label(text="hello",fg="black",bg="white")
button=Button(text="click me",fg="white",bg="black")
entry=Entry(fg="black",bg="white",width=50)

greeting.pack()
button.pack()
entry.pack()

frame=Frame(master=window,relief="raised",borderwidth=5)

frame.pack()
label=Label(master=frame ,text="hey",fg="black",bg="pink")
label.pack()

textbox=Text(fg="green",bg="Black")
textbox.pack()

window.mainloop()