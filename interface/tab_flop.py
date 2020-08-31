import tkinter


class FrameFlopButtons:
    def __init__(self, master):
        buttons_frame = tkinter.Frame(master)
        buttons_frame.place(x = 10, y = 57)
    
        button_f1 = tkinter.Button(buttons_frame, text = 'F1', width = 10)
        button_f1.grid(row = 0, column = 0, padx = 5, pady = 3)

        button_f2 = tkinter.Button(buttons_frame, text = 'F2', width = 10)
        button_f2.grid(row = 1, column = 0, padx = 5, pady = 3)

        button_f3 = tkinter.Button(buttons_frame, text = 'F3', width = 10)
        button_f3.grid(row = 2, column = 0, padx = 5, pady = 3)


class FrameFlopEquity:

    def __init__(self, master):
        # main frame
        range_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        range_frame.place(x = 120, y = 10)


        label_hands_f1 = tkinter.Label(range_frame, text = 'Range\n(mãos)')
        label_hands_f1.grid(row = 0, column = 1)

        label_eq_villain_f1 = tkinter.Label(range_frame, text = 'Eq. Vilão\n(%)')
        label_eq_villain_f1.grid(row = 0, column = 2)

        label_eq_hero_f1 = tkinter.Label(range_frame, text = 'Eq. Hero\n(%)')
        label_eq_hero_f1.grid(row = 0, column = 3)

        label_eq_split_f1 = tkinter.Label(range_frame, text = 'Split\n(%)')
        label_eq_split_f1.grid(row = 0, column = 4)


        entry_hands_f1 = tkinter.Entry(range_frame, width = 8)
        entry_hands_f1.grid(row = 1, column = 1, padx = 5, pady= 7)

        entry_eq_villain_f1 = tkinter.Entry(range_frame, width = 8)
        entry_eq_villain_f1.grid(row = 1, column = 2, padx = 5, pady= 7)

        entry_eq_hero_f1 = tkinter.Entry(range_frame, width = 8)
        entry_eq_hero_f1.grid(row = 1, column = 3, padx = 5, pady= 7)

        entry_eq_split_f1 = tkinter.Entry(range_frame, width = 8)
        entry_eq_split_f1.grid(row = 1, column = 4, padx = 5, pady= 7)
    

        entry_hands_f2 = tkinter.Entry(range_frame, width = 8)
        entry_hands_f2.grid(row = 2, column = 1, padx = 5, pady= 7)

        entry_eq_villain_f2 = tkinter.Entry(range_frame, width = 8)
        entry_eq_villain_f2.grid(row = 2, column = 2, padx = 5, pady= 7)

        entry_eq_hero_f2 = tkinter.Entry(range_frame, width = 8)
        entry_eq_hero_f2.grid(row = 2, column = 3, padx = 5, pady= 7)

        entry_eq_split_f2 = tkinter.Entry(range_frame, width = 8)
        entry_eq_split_f2.grid(row = 2, column = 4, padx = 5, pady= 7)
    

        entry_hands_f3 = tkinter.Entry(range_frame, width = 8)
        entry_hands_f3.grid(row = 3, column = 1, padx = 5, pady= 7)

        entry_eq_villain_f3 = tkinter.Entry(range_frame, width = 8)
        entry_eq_villain_f3.grid(row = 3, column = 2, padx = 5, pady= 7)

        entry_eq_hero_f3 = tkinter.Entry(range_frame, width = 8)
        entry_eq_hero_f3.grid(row = 3, column = 3, padx = 5, pady= 7)

        entry_eq_split_f3 = tkinter.Entry(range_frame, width = 8)
        entry_eq_split_f3.grid(row = 3, column = 4, padx = 5, pady= 7)

class FrameFlopFoldEquity:

    def __init__(self, master):
        range_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        range_frame.place(x = 400, y = 10)

        label_fe_hands_f1 = tkinter.Label(range_frame, text = 'FE/Block\n(mãos)')
        label_fe_hands_f1.grid(row = 0, column = 1)

        label_fe_percent_f1 = tkinter.Label(range_frame, text = 'FE/Block\n(%)')
        label_fe_percent_f1.grid(row = 0, column = 2)

        label_cbet_f1 = tkinter.Label(range_frame, text =  'Cbet\n(%)')
        label_cbet_f1.grid(row = 0, column = 3)


        entry_fe_hands_f1 = tkinter.Entry(range_frame, width = 8)
        entry_fe_hands_f1.grid(row = 1, column = 1, padx = 5, pady= 7)

        entry_fe_percent_f1 = tkinter.Entry(range_frame, width = 8)
        entry_fe_percent_f1.grid(row = 1, column = 2, padx = 5, pady= 7)

        entry_cbet_f1 = tkinter.Entry(range_frame, width = 8)
        entry_cbet_f1.grid(row = 1, column = 3, padx = 5, pady= 7)


        entry_fe_hands_f2 = tkinter.Entry(range_frame, width = 8)
        entry_fe_hands_f2.grid(row = 2, column = 1, padx = 5, pady= 7)

        entry_fe_percent_f2 = tkinter.Entry(range_frame, width = 8)
        entry_fe_percent_f2.grid(row = 2, column = 2, padx = 5, pady= 7)

        entry_cbet_f2 = tkinter.Entry(range_frame, width = 8)
        entry_cbet_f2.grid(row = 2, column = 3, padx = 5, pady= 7)


        entry_fe_hands_f3 = tkinter.Entry(range_frame, width = 8)
        entry_fe_hands_f3.grid(row = 3, column = 1, padx = 5, pady= 7)

        entry_fe_percent_f3 = tkinter.Entry(range_frame, width = 8)
        entry_fe_percent_f3.grid(row = 3, column = 2, padx = 5, pady= 7)

        entry_cbet_f3 = tkinter.Entry(range_frame, width = 8)
        entry_cbet_f3.grid(row = 3, column = 3, padx = 5, pady= 7)