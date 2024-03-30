import tkinter as tk

paned_window = tk.PanedWindow()
paned_window.grid()

left_pane = tk.Label(paned_window, text="left pane")
paned_window.add(left_pane)

nested_pane = tk.PanedWindow(paned_window, orient= "vertical")
paned_window.add(nested_pane)

top_label = tk.Label(nested_pane, text="top pane")
nested_pane.add(top_label)

bottom_textbox = tk.Text(nested_pane)
bottom_textbox.configure(
    bg = 'white',
    fg = 'black', 
    height = 10, 
    width = 20, 
    font = "Times 12 italic bold")
nested_pane.add(bottom_textbox)


paned_window.mainloop()