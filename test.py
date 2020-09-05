figures_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
naipes_list = ['d', 'h', 's', 'c']

# matrix = [[None for x in range(13)] for x in range (4)]
# for i in matrix:
#     print(i)


# cards = [[figure+naipe for figure in figures_list] for naipe in naipes_list]
# for i in cards:
#     print(i)


hands = [[f1+f2 for f1 in figures_list] for f2 in figures_list]
for i in hands:
    print(i)




'''
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Titulo da janela")

my_pic = Image.open('interface/images/button_clear.png')
resized = my_pic.resize((20, 20), Image.ANTIALIAS)
resized.save('interface/images/card_selection_resized.png')

new_pic = ImageTk.PhotoImage(resized)

my_label = Label(root, image = new_pic)
my_label.pack(pady = 20)


root.mainloop()
'''
