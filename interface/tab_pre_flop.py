import tkinter


class FramePreFlopButtons:
    def __init__(self, master):
        buttons_frame = tkinter.Frame(master)
        buttons_frame.place(x = 10, y = 57)
    
        button_pf1 = tkinter.Button(buttons_frame, text = 'PF1', width = 10)
        button_pf1.grid(row = 0, column = 0, padx = 5, pady = 3)

        button_pf2 = tkinter.Button(buttons_frame, text = 'PF2', width = 10)
        button_pf2.grid(row = 1, column = 0, padx = 5, pady = 3)


class FramePreFlopEquity:

    def __init__(self, master):
        # main frame
        range_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        range_frame.place(x = 120, y = 10)


        label_hands_pf1 = tkinter.Label(range_frame, text = 'Range\n(mãos)')
        label_hands_pf1.grid(row = 0, column = 1)

        label_eq_villain_pf1 = tkinter.Label(range_frame, text = 'Eq. Vilão\n(%)')
        label_eq_villain_pf1.grid(row = 0, column = 2)

        label_eq_hero_pf1 = tkinter.Label(range_frame, text = 'Eq. Hero\n(%)')
        label_eq_hero_pf1.grid(row = 0, column = 3)

        label_eq_split_pf1 = tkinter.Label(range_frame, text = 'Split\n(%)')
        label_eq_split_pf1.grid(row = 0, column = 4)


        entry_hands_pf1 = tkinter.Entry(range_frame, width = 8)
        entry_hands_pf1.grid(row = 1, column = 1, padx = 5, pady= 7)

        entry_eq_villain_pf1 = tkinter.Entry(range_frame, width = 8)
        entry_eq_villain_pf1.grid(row = 1, column = 2, padx = 5, pady= 7)

        entry_eq_hero_pf1 = tkinter.Entry(range_frame, width = 8)
        entry_eq_hero_pf1.grid(row = 1, column = 3, padx = 5, pady= 7)

        entry_eq_split_pf1 = tkinter.Entry(range_frame, width = 8)
        entry_eq_split_pf1.grid(row = 1, column = 4, padx = 5, pady= 7)
    

        entry_hands_pf2 = tkinter.Entry(range_frame, width = 8)
        entry_hands_pf2.grid(row = 2, column = 1, padx = 5, pady= 7)

        entry_eq_villain_pf2 = tkinter.Entry(range_frame, width = 8)
        entry_eq_villain_pf2.grid(row = 2, column = 2, padx = 5, pady= 7)

        entry_eq_hero_pf2 = tkinter.Entry(range_frame, width = 8)
        entry_eq_hero_pf2.grid(row = 2, column = 3, padx = 5, pady= 7)

        entry_eq_split_pf2 = tkinter.Entry(range_frame, width = 8)
        entry_eq_split_pf2.grid(row = 2, column = 4, padx = 5, pady= 7)


class FramePreFlopFoldEquity:

    def __init__(self, master):
        range_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        range_frame.place(x = 400, y = 10)

        label_fe_hands_pf1 = tkinter.Label(range_frame, text = 'FE/Block\n(mãos)')
        label_fe_hands_pf1.grid(row = 0, column = 1)

        label_fe_percent_pf1 = tkinter.Label(range_frame, text = 'FE/Block\n(%)')
        label_fe_percent_pf1.grid(row = 0, column = 2)

        label_cbet_pf1 = tkinter.Label(range_frame, text =  'Cbet\n(%)')
        label_cbet_pf1.grid(row = 0, column = 3)


        entry_fe_hands_pf1 = tkinter.Entry(range_frame, width = 8)
        entry_fe_hands_pf1.grid(row = 1, column = 1, padx = 5, pady= 7)

        entry_fe_percent_pf1 = tkinter.Entry(range_frame, width = 8)
        entry_fe_percent_pf1.grid(row = 1, column = 2, padx = 5, pady= 7)

        entry_cbet_pf1 = tkinter.Entry(range_frame, width = 8)
        entry_cbet_pf1.grid(row = 1, column = 3, padx = 5, pady= 7)


        entry_fe_hands_pf2 = tkinter.Entry(range_frame, width = 8)
        entry_fe_hands_pf2.grid(row = 2, column = 1, padx = 5, pady= 7)

        entry_fe_percent_pf2 = tkinter.Entry(range_frame, width = 8)
        entry_fe_percent_pf2.grid(row = 2, column = 2, padx = 5, pady= 7)

        entry_cbet_pf2 = tkinter.Entry(range_frame, width = 8)
        entry_cbet_pf2.grid(row = 2, column = 3, padx = 5, pady= 7)
