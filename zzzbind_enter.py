import tkinter


def cardmotion(event, btn):
    if event.state == 9:
        if btn['relief'] == 'raised':
            btn['relief'] = 'sunken'
        else:
            btn['relief'] = 'raised'

def teste(event, btn):
    # botao = event.widget.winfo_containing(event.x_root, event.y_root)
    print(btn['text'],  event)
    


root = tkinter.Tk()
root.wm_geometry('500x500')

frame = tkinter.Frame(root, )
frame.pack()

for i in range(9):
    btn = tkinter.Button(frame, text = i, padx = 10, pady = 10)
    btn.grid(row = 0, column = i, padx = 5, pady = 10)
    btn.bind('<Enter>', lambda event, btn = btn: cardmotion(event, btn))
    # btn.bind('<<B1-Enter>>', lambda event, btn = btn: teste(event, btn))
    

root.mainloop()




