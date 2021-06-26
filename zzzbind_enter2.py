import tkinter as tk

current_widget = None
def show_info(event):
    global current_widget
    widget = event.widget.winfo_containing(event.x_root, event.y_root)
    if current_widget != widget:
        current_widget = widget
        print(widget)
        # current_widget.event_generate("<<B1-Enter>>")

def on_enter(event):
    if event.widget['relief'] == 'raised':
        event.widget.configure(relief="sunken")
    else:
        event.widget.configure(relief="raised")


root = tk.Tk()
root.wm_geometry('500x500')
l1 = tk.Button(root, text='AKs')
l2 = tk.Button(root, text='AQs')

l1.pack(padx=20, pady=20)
l2.pack(padx=20, pady=20)

root.bind("<B1-Motion>", show_info)
l1.bind("<<B1-Enter>>", on_enter)
l2.bind("<<B1-Enter>>", on_enter)


# tk.mainloop()