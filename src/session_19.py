import tkinter as tk

window = tk.Tk()

Text_box = tk.Text()
Text_box.pack()

Text_box.insert("1.0", "hello")
Text_box.insert("2.0", "\nhello again")
Text_box.insert(tk.END,"\nput me at the end:)")


text = Text_box.get("1.0", tk.END)
print(text)


window.mainloop()