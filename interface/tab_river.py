import tkinter


class FrameRiverButtons:
    def __init__(self, master):
        buttons_frame = tkinter.Frame(master)
        buttons_frame.place(x = 10, y = 57)
    
        button_r1 = tkinter.Button(buttons_frame, text = 'R1', width = 10)
        button_r1.grid(row = 0, column = 0, padx = 5, pady = 3)

        button_r2 = tkinter.Button(buttons_frame, text = 'R2', width = 10)
        button_r2.grid(row = 1, column = 0, padx = 5, pady = 3)

        button_r3 = tkinter.Button(buttons_frame, text = 'R3', width = 10)
        button_r3.grid(row = 2, column = 0, padx = 5, pady = 3)


class FrameRiverEquity:

    def __init__(self, master):
        # main frame
        range_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        range_frame.place(x = 120, y = 10)


        label_hands_r1 = tkinter.Label(range_frame, text = 'Range\n(mãos)')
        label_hands_r1.grid(row = 0, column = 1)

        label_eq_villain_r1 = tkinter.Label(range_frame, text = 'Eq. Vilão\n(%)')
        label_eq_villain_r1.grid(row = 0, column = 2)

        label_eq_hero_r1 = tkinter.Label(range_frame, text = 'Eq. Hero\n(%)')
        label_eq_hero_r1.grid(row = 0, column = 3)

        label_eq_split_r1 = tkinter.Label(range_frame, text = 'Split\n(%)')
        label_eq_split_r1.grid(row = 0, column = 4)


        entry_hands_r1 = tkinter.Entry(range_frame, width = 8)
        entry_hands_r1.grid(row = 1, column = 1, padx = 5, pady= 7)

        entry_eq_villain_r1 = tkinter.Entry(range_frame, width = 8)
        entry_eq_villain_r1.grid(row = 1, column = 2, padx = 5, pady= 7)

        entry_eq_hero_r1 = tkinter.Entry(range_frame, width = 8)
        entry_eq_hero_r1.grid(row = 1, column = 3, padx = 5, pady= 7)

        entry_eq_split_r1 = tkinter.Entry(range_frame, width = 8)
        entry_eq_split_r1.grid(row = 1, column = 4, padx = 5, pady= 7)
    

        entry_hands_r2 = tkinter.Entry(range_frame, width = 8)
        entry_hands_r2.grid(row = 2, column = 1, padx = 5, pady= 7)

        entry_eq_villain_r2 = tkinter.Entry(range_frame, width = 8)
        entry_eq_villain_r2.grid(row = 2, column = 2, padx = 5, pady= 7)

        entry_eq_hero_r2 = tkinter.Entry(range_frame, width = 8)
        entry_eq_hero_r2.grid(row = 2, column = 3, padx = 5, pady= 7)

        entry_eq_split_r2 = tkinter.Entry(range_frame, width = 8)
        entry_eq_split_r2.grid(row = 2, column = 4, padx = 5, pady= 7)
    

        entry_hands_r3 = tkinter.Entry(range_frame, width = 8)
        entry_hands_r3.grid(row = 3, column = 1, padx = 5, pady= 7)

        entry_eq_villain_r3 = tkinter.Entry(range_frame, width = 8)
        entry_eq_villain_r3.grid(row = 3, column = 2, padx = 5, pady= 7)

        entry_eq_hero_r3 = tkinter.Entry(range_frame, width = 8)
        entry_eq_hero_r3.grid(row = 3, column = 3, padx = 5, pady= 7)

        entry_eq_split_r3 = tkinter.Entry(range_frame, width = 8)
        entry_eq_split_r3.grid(row = 3, column = 4, padx = 5, pady= 7)

class FrameRiverFoldEquity:

    def __init__(self, master):
        range_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        range_frame.place(x = 400, y = 10)

        label_fe_hands_r1 = tkinter.Label(range_frame, text = 'FE/Block\n(mãos)')
        label_fe_hands_r1.grid(row = 0, column = 1)

        label_fe_percent_r1 = tkinter.Label(range_frame, text = 'FE/Block\n(%)')
        label_fe_percent_r1.grid(row = 0, column = 2)

        label_cbet_r1 = tkinter.Label(range_frame, text =  'Cbet\n(%)')
        label_cbet_r1.grid(row = 0, column = 3)


        entry_fe_hands_r1 = tkinter.Entry(range_frame, width = 8)
        entry_fe_hands_r1.grid(row = 1, column = 1, padx = 5, pady= 7)

        entry_fe_percent_r1 = tkinter.Entry(range_frame, width = 8)
        entry_fe_percent_r1.grid(row = 1, column = 2, padx = 5, pady= 7)

        entry_cbet_r1 = tkinter.Entry(range_frame, width = 8)
        entry_cbet_r1.grid(row = 1, column = 3, padx = 5, pady= 7)


        entry_fe_hands_r2 = tkinter.Entry(range_frame, width = 8)
        entry_fe_hands_r2.grid(row = 2, column = 1, padx = 5, pady= 7)

        entry_fe_percent_r2 = tkinter.Entry(range_frame, width = 8)
        entry_fe_percent_r2.grid(row = 2, column = 2, padx = 5, pady= 7)

        entry_cbet_r2 = tkinter.Entry(range_frame, width = 8)
        entry_cbet_r2.grid(row = 2, column = 3, padx = 5, pady= 7)


        entry_fe_hands_r3 = tkinter.Entry(range_frame, width = 8)
        entry_fe_hands_r3.grid(row = 3, column = 1, padx = 5, pady= 7)

        entry_fe_percent_r3 = tkinter.Entry(range_frame, width = 8)
        entry_fe_percent_r3.grid(row = 3, column = 2, padx = 5, pady= 7)

        entry_cbet_r3 = tkinter.Entry(range_frame, width = 8)
        entry_cbet_r3.grid(row = 3, column = 3, padx = 5, pady= 7)