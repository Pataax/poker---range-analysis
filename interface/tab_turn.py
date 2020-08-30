import tkinter


class FrameTurnButtons:
    def __init__(self, master):
        buttons_frame = tkinter.Frame(master)
        buttons_frame.place(x = 10, y = 52)
    
        button_t1 = tkinter.Button(buttons_frame, text = 'T1', width = 10)
        button_t1.grid(row = 0, column = 0, padx = 5, pady = 3)

        button_t2 = tkinter.Button(buttons_frame, text = 'T2', width = 10)
        button_t2.grid(row = 1, column = 0, padx = 5, pady = 3)

        button_t3 = tkinter.Button(buttons_frame, text = 'T3', width = 10)
        button_t3.grid(row = 2, column = 0, padx = 5, pady = 3)


class FrameTurnEquity:

    def __init__(self, master):
        # main frame
        range_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        range_frame.place(x = 120, y = 10)


        label_hands_t1 = tkinter.Label(range_frame, text = 'Range\n(mãos)')
        label_hands_t1.grid(row = 0, column = 1)

        label_eq_villain_t1 = tkinter.Label(range_frame, text = 'Eq. Vilão\n(%)')
        label_eq_villain_t1.grid(row = 0, column = 2)

        label_eq_hero_t1 = tkinter.Label(range_frame, text = 'Eq. Hero\n(%)')
        label_eq_hero_t1.grid(row = 0, column = 3)

        label_eq_split_t1 = tkinter.Label(range_frame, text = 'Split\n(%)')
        label_eq_split_t1.grid(row = 0, column = 4)


        entry_hands_t1 = tkinter.Entry(range_frame, width = 8)
        entry_hands_t1.grid(row = 1, column = 1, padx = 5, pady= 5)

        entry_eq_villain_t1 = tkinter.Entry(range_frame, width = 8)
        entry_eq_villain_t1.grid(row = 1, column = 2, padx = 5)

        entry_eq_hero_t1 = tkinter.Entry(range_frame, width = 8)
        entry_eq_hero_t1.grid(row = 1, column = 3, padx = 5)

        entry_eq_split_t1 = tkinter.Entry(range_frame, width = 8)
        entry_eq_split_t1.grid(row = 1, column = 4, padx = 5)
    

        entry_hands_t2 = tkinter.Entry(range_frame, width = 8)
        entry_hands_t2.grid(row = 2, column = 1, padx = 5, pady= 5)

        entry_eq_villain_t2 = tkinter.Entry(range_frame, width = 8)
        entry_eq_villain_t2.grid(row = 2, column = 2, padx = 5)

        entry_eq_hero_t2 = tkinter.Entry(range_frame, width = 8)
        entry_eq_hero_t2.grid(row = 2, column = 3, padx = 5)

        entry_eq_split_t2 = tkinter.Entry(range_frame, width = 8)
        entry_eq_split_t2.grid(row = 2, column = 4, padx = 5)
    

        entry_hands_t3 = tkinter.Entry(range_frame, width = 8)
        entry_hands_t3.grid(row = 3, column = 1, padx = 5, pady= 5)

        entry_eq_villain_t3 = tkinter.Entry(range_frame, width = 8)
        entry_eq_villain_t3.grid(row = 3, column = 2, padx = 5)

        entry_eq_hero_t3 = tkinter.Entry(range_frame, width = 8)
        entry_eq_hero_t3.grid(row = 3, column = 3, padx = 5)

        entry_eq_split_t3 = tkinter.Entry(range_frame, width = 8)
        entry_eq_split_t3.grid(row = 3, column = 4, padx = 5)

class FrameTurnFoldEquity:

    def __init__(self, master):
        range_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        range_frame.place(x = 400, y = 10)

        label_fe_hands_t1 = tkinter.Label(range_frame, text = 'FE/Block\n(mãos)')
        label_fe_hands_t1.grid(row = 0, column = 1)

        label_fe_percent_t1 = tkinter.Label(range_frame, text = 'FE/Block\n(%)')
        label_fe_percent_t1.grid(row = 0, column = 2)

        label_cbet_t1 = tkinter.Label(range_frame, text =  'Cbet\n(%)')
        label_cbet_t1.grid(row = 0, column = 3)


        entry_fe_hands_t1 = tkinter.Entry(range_frame, width = 8)
        entry_fe_hands_t1.grid(row = 1, column = 1, padx = 5, pady= 5)

        entry_fe_percent_t1 = tkinter.Entry(range_frame, width = 8)
        entry_fe_percent_t1.grid(row = 1, column = 2, padx = 5)

        entry_cbet_t1 = tkinter.Entry(range_frame, width = 8)
        entry_cbet_t1.grid(row = 1, column = 3, padx = 5)


        entry_fe_hands_t2 = tkinter.Entry(range_frame, width = 8)
        entry_fe_hands_t2.grid(row = 2, column = 1, padx = 5, pady= 5)

        entry_fe_percent_t2 = tkinter.Entry(range_frame, width = 8)
        entry_fe_percent_t2.grid(row = 2, column = 2, padx = 5)

        entry_cbet_t2 = tkinter.Entry(range_frame, width = 8)
        entry_cbet_t2.grid(row = 2, column = 3, padx = 5)


        entry_fe_hands_t3 = tkinter.Entry(range_frame, width = 8)
        entry_fe_hands_t3.grid(row = 3, column = 1, padx = 5, pady= 5)

        entry_fe_percent_t3 = tkinter.Entry(range_frame, width = 8)
        entry_fe_percent_t3.grid(row = 3, column = 2, padx = 5)

        entry_cbet_t3 = tkinter.Entry(range_frame, width = 8)
        entry_cbet_t3.grid(row = 3, column = 3, padx = 5)