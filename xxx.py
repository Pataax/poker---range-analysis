from tkinter import *


def btn_pincel_click():
    global foo

    if foo == 0:
        foo = 1
        btn_pincel.config(relief = 'sunken')
    else:
        foo = 0
        btn_pincel.config(relief = 'raised')
    print(foo)


def btn1_motion(event):
    global foo, bar
    if (foo == 1) and (bar != btn1['text']):
        if btn1['relief'] == 'raised':
            btn1['relief'] = 'sunken'
            bar = btn1['text']
            print(bar)
        else:
            if btn1['relief'] == 'sunken':
                btn1['relief'] = 'raised'
                bar = btn1['text']
                print(bar)
    

def btn1_leave(event):
    global bar
    bar = ''


def btn2_motion(event):
    global foo, bar
    if (foo == 1) and (bar != btn2['text']):
        if btn2['relief'] == 'raised':
            btn2['relief'] = 'sunken'
            bar = btn2['text']
            print(bar)
        else:
            if btn2['relief'] == 'sunken':
                btn2['relief'] = 'raised'
                bar = btn2['text']
                print(bar)
    

def btn2_leave(event):
    global bar
    bar = ''

foo = 0
bar = ''

master = Tk()

btn_pincel = Button(master, text = 'pincel', command = btn_pincel_click)
btn_pincel.pack()

btn1 = Button(master, text = 'AK', font=('Arial', 24))
btn1.pack()
btn1.bind('<Motion>', btn1_motion)
btn1.bind('<Leave>', btn1_leave)

btn2 = Button(master, text = 'AQ', font=('Arial', 24))
btn2.pack()
btn2.bind('<Motion>', btn2_motion)
btn2.bind('<Leave>', btn2_leave)

mainloop()