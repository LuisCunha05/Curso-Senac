import tkinter as tk


class Pyculator:
    def __init__(self) -> None:

        self.root = tk.Tk()
        self.root.geometry('500x600')
        self.root.resizable(width=False, height=False)
        self.root.title('Pyculator')
        self.root.configure(background='#282828')
        
        self.pyc_label = tk.Label(
            self.root, text='Pyculator Ultra Long test for testing purposes, still not enought so we have to continue and see where it lands!',
            font=('Arial', 14),
            height=4,
            highlightthickness=1,
            highlightbackground='gray',
            background='#282828',
            fg='#ffffff',
            justify='right',
            wraplength=468
            )
        self.pyc_label.pack(padx=15,pady=15, fill='x')

        #Numeric Frame
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)
        self.btn_frame.columnconfigure(2, weight=1)

        #Numbers
        self.btn_1 = tk.Button(self.btn_frame, text='1', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_1.grid(row=2, column=0, sticky='we')
        self.btn_2 = tk.Button(self.btn_frame, text='2', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_2.grid(row=2, column=1, sticky='we')
        self.btn_3 = tk.Button(self.btn_frame, text='3', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_3.grid(row=2, column=2, sticky='we')
        self.btn_4 = tk.Button(self.btn_frame, text='4', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_4.grid(row=1, column=0, sticky='we')
        self.btn_5 = tk.Button(self.btn_frame, text='5', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_5.grid(row=1, column=1, sticky='we')
        self.btn_6 = tk.Button(self.btn_frame, text='6', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_6.grid(row=1, column=2, sticky='we')
        self.btn_7 = tk.Button(self.btn_frame, text='7', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_7.grid(row=0, column=0, sticky='we')
        self.btn_8 = tk.Button(self.btn_frame, text='8', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_8.grid(row=0, column=1, sticky='we')
        self.btn_9 = tk.Button(self.btn_frame, text='9', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_9.grid(row=0, column=2, sticky='we')
        self.btn_0 = tk.Button(self.btn_frame, text='0', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_0.grid(row=3, column=1, sticky='we')
        self.btn_pi = tk.Button(self.btn_frame, text='π', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_pi.grid(row=3, column=0, sticky='we')
        self.btn_dot = tk.Button(self.btn_frame, text='.', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_dot.grid(row=3, column=2, sticky='we')

        self.btn_frame.pack(padx=15, pady=15, fill='x')

        #Operations Frame
        self.op_frame = tk.Frame(self.root)
        self.op_frame.columnconfigure(0, weight=1)
        self.op_frame.columnconfigure(1, weight=1)
        self.op_frame.columnconfigure(2, weight=1)

        #Commands
        self.btn_clear = tk.Button(self.op_frame, text='C', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_clear.grid(row=0, column=0, sticky='we')
        self.btn_clear_entry = tk.Button(self.op_frame, text='CE', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_clear_entry.grid(row=0, column=1, sticky='we')
        self.btn_backspace = tk.Button(self.op_frame, text='🡐', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_backspace.grid(row=0, column=2, sticky='we')

        #Operations
        self.btn_plus = tk.Button(self.op_frame, text='+', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_plus.grid(row=1, column=0, sticky='we')
        self.btn_minus = tk.Button(self.op_frame, text='-', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_minus.grid(row=1, column=1, sticky='we')
        self.btn_multiply = tk.Button(self.op_frame, text='x', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_multiply.grid(row=1, column=2, sticky='we')
        self.btn_division = tk.Button(self.op_frame, text='/', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_division.grid(row=2, column=0, sticky='we')
        self.btn_open_parent = tk.Button(self.op_frame, text='(', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_open_parent.grid(row=2, column=1, sticky='we')
        self.btn_close_parent = tk.Button(self.op_frame, text=')', font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_close_parent.grid(row=2, column=2, sticky='we')

        self.op_frame.pack(padx=15, fill='x')

        #self.btn_quit = tk.Button(self.root, text="Quit", font=('Arial', 16), background='#4d4d4d', fg='#ffffff', width=15, command=self.root.destroy).pack()

        self.root.mainloop()

Pyculator()