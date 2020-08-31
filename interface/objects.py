import tkinter


class FrameStreetsButtons:

    def __init__(self, master, qtd, name, row, column):
        self.qtd = qtd
        self.name = name
        self.row = row
        self.column = column
        buttons_dict = {}

        buttons_frame = tkinter.Frame(master, width = 80, height = 115)
        buttons_frame.grid(row = self.row, column = self.column, sticky = 's', ipady = 8)
    
        for n in range(self.qtd):
            new_button = tkinter.Button(buttons_frame, text = f'{self.name}{n + 1}', width = 10)
            buttons_dict[f'{self.name}{n + 1}'] = new_button
            print(buttons_dict)
            new_button.grid(row = n, column = 0, padx = 5, pady = 3, sticky = 's')


class FrameStreetsTable:

    def __init__(self, master, rows, table_type, row, column):
        self.rows = rows
        self.table_type = table_type
        self.row = row
        self.column = column

        title_dict = {
            'equity': ['Range\n(mãos)', 'Eq. Vilão\n(%)', 'Eq. Hero\n(%)', 'Split\n(%)'],
            'fold_equity': ['FE/Block\n(mãos)', 'FE/Block\n(%)', 'Cbet\n(%)'],
        }
        
        
        # main frame
        range_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        range_frame.grid(row = self.row, column = self.column, padx = 10, pady = 10)

        # create the labels with the titles
        for i in range(len(title_dict[self.table_type])):
            label = tkinter.Label(range_frame, text = title_dict[self.table_type][i])
            label.grid(row = 0, column = i, padx = 5)

        # create the entries(?)
        for i in range(len(title_dict[self.table_type])):
            for x in range(self.rows):
                entry = tkinter.Entry(range_frame, width = 8)
                entry.grid(row = x + 1, column = i, padx = 5, pady = 7)


class FrameCards:

    def __init__(self, master, row, column):
        self.row = row
        self.column = column

        # main frame
        main_frame = tkinter.Frame(master, padx = 5, pady = 5, bd = 2, relief = 'groove')
        main_frame.grid(row = self.row, column = self.column, pady = 10, columnspan = 3)

        labels_list = ['Hero', 'Flop', 'Turn', 'River']

        for i in range (len(labels_list)):
            frame = tkinter.Frame(main_frame)
            frame.grid(row = 0, column = i, padx = 5)

            label = tkinter.Label(frame, text = f'{labels_list[i]}:')
            label.grid(row = 0, column = 0)

            entry = tkinter.Entry(frame, width = 5)
            entry.grid(row = 0, column = 1, padx = 5)

            button_choose = tkinter.Button(frame, width = 2, height = 1)
            button_choose.grid(row = 0, column = 2, padx = 5, pady = 5)

            button_clear = tkinter.Button(frame, width = 2)
            button_clear.grid(row = 0, column = 3)
