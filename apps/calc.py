import tkinter as tk

#test

class Pyculator:
    def __init__(self) -> None:

        self.root = tk.Tk()
        self.root.geometry('500x700')
        self.root.title('Pyculator')

        self.pyc_label = tk.Label(
            self.root, text='Pyculator',
            font=('Arial', 14),
            height=3,
            highlightthickness=1,
            highlightbackground='gray',
            )
        self.pyc_label.pack(padx=15,pady=15, fill='x')

        #Botões Numéricos
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)
        self.btn_frame.columnconfigure(2, weight=1)

        self.btn_1 = tk.Button(self.btn_frame, text='1', font=('Arial', 16))
        self.btn_1.grid(row=2, column=0, sticky='we')
        self.btn_2 = tk.Button(self.btn_frame, text='2', font=('Arial', 16))
        self.btn_2.grid(row=2, column=1, sticky='we')
        self.btn_3 = tk.Button(self.btn_frame, text='3', font=('Arial', 16))
        self.btn_3.grid(row=2, column=2, sticky='we')
        self.btn_4 = tk.Button(self.btn_frame, text='4', font=('Arial', 16))
        self.btn_4.grid(row=1, column=0, sticky='we')
        self.btn_5 = tk.Button(self.btn_frame, text='5', font=('Arial', 16))
        self.btn_5.grid(row=1, column=1, sticky='we')
        self.btn_6 = tk.Button(self.btn_frame, text='6', font=('Arial', 16))
        self.btn_6.grid(row=1, column=2, sticky='we')
        self.btn_7 = tk.Button(self.btn_frame, text='7', font=('Arial', 16))
        self.btn_7.grid(row=0, column=0, sticky='we')
        self.btn_8 = tk.Button(self.btn_frame, text='8', font=('Arial', 16))
        self.btn_8.grid(row=0, column=1, sticky='we')
        self.btn_9 = tk.Button(self.btn_frame, text='9', font=('Arial', 16))
        self.btn_9.grid(row=0, column=2, sticky='we')
        self.btn_0 = tk.Button(self.btn_frame, text='0', font=('Arial', 16))
        self.btn_0.grid(row=3, column=1, sticky='we')
        self.btn_pi = tk.Button(self.btn_frame, text='π', font=('Arial', 16))
        self.btn_pi.grid(row=3, column=0, sticky='we')
        self.btn_dot = tk.Button(self.btn_frame, text='.', font=('Arial', 16))
        self.btn_dot.grid(row=3, column=2, sticky='we')

        self.btn_frame.pack(fill='x', padx=15, pady=15)

        self.op_frame = tk.Frame(self.root)
        self.op_frame.columnconfigure(0, weight=1)
        self.op_frame.columnconfigure(1, weight=1)
        self.op_frame.columnconfigure(2, weight=1)
        self.btn_plus = tk.Button(self.op_frame, text='+', font=('Arial', 16))
        self.btn_plus.grid(row=3, column=1, sticky='we')
        self.btn_minus = tk.Button(self.op_frame, text='-', font=('Arial', 16))
        self.btn_minus.grid(row=3, column=0, sticky='we')
        self.btn_multiply = tk.Button(self.op_frame, text='x', font=('Arial', 16))
        self.btn_multiply.grid(row=3, column=2, sticky='we')
        
        self.op_frame.pack(padx=15, fill='x')


        self.btn_quit = tk.Button(self.root, text="Quit", command=self.root.destroy).pack()

        self.root.mainloop()

Pyculator()