import tkinter as tk

window = tk.Tk()
window.title("My App")

label1 = tk.Label(
    window,
    text = "Hello, Tkinter",
    background = "#34A2FE",
    foreground = "white",
    width = 20,
    height = 10
)
label1.pack()

button1 = tk.Button(
    window,
    text = "Click Here!",
    fg = "blue",
    bg = "red"
)
button1.pack()

entry1 = tk.Entry(window)
entry1.pack()

entry1.insert(0,"World")
entry1.insert(0, "Hello ")

some_text = entry1.get()
print(some_text)

entry1.delete(0)
entry1.delete(0,2)
entry1.delete(0, tk.END)

window.mainloop()