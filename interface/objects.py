import tkinter


class FrameStreetsButtons:
    def __init__(self, master, qtd, name, row, column):
        self.qtd = qtd
        self.name = name
        self.row = row
        self.column = column
        self.buttons_dict = {}

        buttons_frame = tkinter.Frame(master)
        buttons_frame.grid(row = self.row, column = self.column, sticky = 's', ipady = 8)
    
        for n in range(self.qtd):
            new_button = tkinter.Button(
                buttons_frame, text = f'{self.name}{n + 1}', width = 10, 
                command = RangeWindow
                )
            new_button.grid(row = n, column = 0, padx = 5, pady = 3, sticky = 's')
            self.buttons_dict[f'{self.name}{n + 1}'] = new_button


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
        main_frame.grid(row = self.row, column = self.column, padx = 10, pady = 10, columnspan = 3)

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


class RangeWindow:
    def __init__(self):
        self.range_window = tkinter.Toplevel()
        self.range_window.title("Selecione o Range")
        self.create_range_buttons_matrix(self.range_window, 0, 0)
        self.creates_auxiliary_buttons(self.range_window, 0, 1)
        self.creates_space_comments(self.range_window, 2, 0)

    def create_range_buttons_matrix(self, master, row, column):
        self.row = row
        self.column = column
        self.range_buttons = [[None for x in range(13)] for x in range (13)]

        cards_frame = tkinter.Frame(master)
        cards_frame.grid(row = self.row, column = self.column, padx = 5, pady = 10)
        for row in range (13):
            for col in range (13):
                self.range_buttons[row][col] = tkinter.Button(cards_frame, text = 'Ax')
                self.range_buttons[row][col].grid(row = row, column = col)

    def creates_auxiliary_buttons(self, master, row, column):
        self.row = row
        self.column = column

        auxiliary_frame = tkinter.Frame(master)
        auxiliary_frame.grid(row = self.row, column = self.column, padx = 5, pady = 5)
        clear_button = tkinter.Button(auxiliary_frame, text = 'Limpar')
        clear_button.grid(padx = 5)
        for i in range(8):
            color_button = tkinter.Button(auxiliary_frame, width = 2)
            color_button.grid(pady = 5)

    def creates_space_comments(self, master, row, column):
        self.row = row
        self.column = column

        comments_frame = tkinter.Frame(master)
        comments_frame.grid(row = self.row, column = self.column, padx = 5, pady = 5)
        comments_label = tkinter.Label(comments_frame, text = 'Comentários')
        comments_label.grid(row = 0, column = 0)
        text_box = tkinter.Text(comments_frame, width = 40, height = 5)
        text_box.grid(row = 1, column = 0, padx = 5, pady = 5)


