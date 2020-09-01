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
            new_button = tkinter.Button(buttons_frame, text = f'{self.name}{n + 1}', width = 10, command = RangeWindow)
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


class RangeWindow:
 
    def __init__(self):
        range_window = tkinter.Toplevel()
        range_window.title("Selecione o Range")
        # range_window.geometry('300x300')


        cards_frame = tkinter.Frame(range_window)
        cards_frame.grid(row = 0, column = 0, padx = 5, pady = 5)

        # create buttons
        for column in range(13):
            for row in range(13):
                card_button = tkinter.Button(cards_frame, text = 'Ax')
                card_button.grid(row = row, column = column)

        # select colors and others options
        options_frame = tkinter.Frame(range_window)
        options_frame.grid(row = 0, column = 1, padx = 5, pady = 5)

        button_clear = tkinter.Button(options_frame, text = "Limpar")
        button_clear.grid(row = 0, column = 0)

        for i in range(8):
            color_button = tkinter.Button(options_frame, width = 2)
            color_button.grid(row = i + 1, column = 0, pady = 3)

        next_button = tkinter.Button(options_frame, text = 'Próx. Slot')
        next_button.grid(pady = 15)

        # create status bar
        status_bar = tkinter.Label(range_window, text = 'status_bar', bd = 1, relief = 'sunken', anchor = 'e')
        status_bar.grid(sticky = 'we')

        # comments
        comments_frame = tkinter.Frame(range_window)
        comments_frame.grid()

        comments_label = tkinter.Label(comments_frame, text = 'Comentários')
        comments_label.grid(row = 0, column = 0)

        text_box = tkinter.text(comments_frame, width = 50, height = 10)
        text_box.grid(row = 1, column = 0)

        #card suit selection
        suit_selection = tkinter.Button(comments_frame, text = "Selecionar Naipe")
        suit_selection.grid(row = 2, column = 0)

