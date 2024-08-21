import tkinter as tk
print(float('2.2'))
def getLastNumber(string: str) -> str:
    result = ''
    for i in range(len(string)):
        print('debugg1:',string, string[-(i+1)].isnumeric())
        if(string[-(i+1)].isnumeric() or string[-(i+1)] == '.'):
            result += string[-(i+1)]
        else:
            break
    return result[::-1]

class Pyculator:
    __symbols = ['+', '-', '/', '*', '.']
    MAX_INT = 9223372036854775807
    def __init__(self) -> None:
        self.calc: str = '0'
        self._parent_open = 0
        self._parent_close = 0
    
    def addChar(self, char: str) -> str:
        """Adds a character to the Calculation string. CANNOT add a new symbol if the last character is a symbol"""

        lastChar = self.getLastChar()
        lastNum = getLastNumber(self.calc)
        print(lastNum)
        if(char.isnumeric()):
            if(lastChar == ')'):
                char += '*'
            elif(lastNum != '' and float(lastNum) > self.MAX_INT):
                return self.calc

        match(char):
            case '(':
                if(self._parent_open >= 5):
                    return self.calc
                else:
                    self._parent_open += 1
                    temp = lastNum
                    if(lastChar == ')' or temp != '0' and temp != '' ):
                        char = '*' + char
            case ')':
                if(self._parent_close >= self._parent_open or lastNum == ''):
                    return self.calc
                else:
                    self._parent_close += 1
            case '.':
                if(not lastChar.isnumeric() or '.' in lastNum):
                    return self.calc

        if(char in Pyculator.__symbols and lastChar in Pyculator.__symbols ):
            return self.calc
        
        if(lastNum == '0' and char != ''):
            self.calc = char
            return self.calc
        self.calc += char
        return self.calc
    
    def clear(self) -> str:
        self.calc = '0'
        self._parent_open = 0
        self._parent_close = 0
        return self.calc
    
    def getLastChar(self) -> str:
        return self.calc[-1]

    def backSpace(self) -> str:
        match(self.getLastChar()):
            case '(':
                self._parent_open -= 1
            case ')':
                self._parent_close -= 1

        self.calc = '0' if self.calc[:-1] == '' else self.calc[:-1]
        return self.calc



class PyculatorGUI(Pyculator):
    def __init__(self) -> None:
        super().__init__()

        self.root = tk.Tk()
        self.root.geometry('500x600')
        self.root.resizable(width=False, height=False)
        self.root.title('Pyculator')
        self.root.configure(background='#282828')

        self._stringCalc = tk.StringVar()
        self._stringCalc.set(self.calc)
        
        self.pyc_label = tk.Label(
            self.root,
            textvariable=self._stringCalc,
            font=('Arial', 14),
            height=4,
            highlightthickness=1,
            highlightbackground='gray',
            background='#282828',
            fg='#ffffff',
            justify='right',
            wraplength=468,
            anchor='se'
            )
        self.pyc_label.pack(padx=15,pady=15, fill='x')

        #Numeric Frame
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)
        self.btn_frame.columnconfigure(2, weight=1)

        #Numbers
        self.btn_1 = tk.Button(self.btn_frame, text='1', command= lambda: self._stringCalc.set(self.addChar('1')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_1.grid(row=2, column=0, sticky='we')
        self.btn_2 = tk.Button(self.btn_frame, text='2', command= lambda: self._stringCalc.set(self.addChar('2')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_2.grid(row=2, column=1, sticky='we')
        self.btn_3 = tk.Button(self.btn_frame, text='3', command= lambda: self._stringCalc.set(self.addChar('3')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_3.grid(row=2, column=2, sticky='we')
        self.btn_4 = tk.Button(self.btn_frame, text='4', command= lambda: self._stringCalc.set(self.addChar('4')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_4.grid(row=1, column=0, sticky='we')
        self.btn_5 = tk.Button(self.btn_frame, text='5', command= lambda: self._stringCalc.set(self.addChar('5')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_5.grid(row=1, column=1, sticky='we')
        self.btn_6 = tk.Button(self.btn_frame, text='6', command= lambda: self._stringCalc.set(self.addChar('6')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_6.grid(row=1, column=2, sticky='we')
        self.btn_7 = tk.Button(self.btn_frame, text='7', command= lambda: self._stringCalc.set(self.addChar('7')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_7.grid(row=0, column=0, sticky='we')
        self.btn_8 = tk.Button(self.btn_frame, text='8', command= lambda: self._stringCalc.set(self.addChar('8')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_8.grid(row=0, column=1, sticky='we')
        self.btn_9 = tk.Button(self.btn_frame, text='9', command= lambda: self._stringCalc.set(self.addChar('9')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_9.grid(row=0, column=2, sticky='we')
        self.btn_0 = tk.Button(self.btn_frame, text='0', command= lambda: self._stringCalc.set(self.addChar('0')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_0.grid(row=3, column=1, sticky='we')
        self.btn_pi = tk.Button(self.btn_frame, text='π', command= lambda: self._stringCalc.set(self.addChar('π')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_pi.grid(row=3, column=0, sticky='we')
        self.btn_dot = tk.Button(self.btn_frame, text='.', command= lambda: self._stringCalc.set(self.addChar('.')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_dot.grid(row=3, column=2, sticky='we')

        self.btn_frame.pack(padx=15, pady=15, fill='x')

        #Operations Frame
        self.op_frame = tk.Frame(self.root)
        self.op_frame.columnconfigure(0, weight=1)
        self.op_frame.columnconfigure(1, weight=1)
        self.op_frame.columnconfigure(2, weight=1)

        #Commands
        self.btn_clear = tk.Button(self.op_frame, text='C', command= lambda: self._stringCalc.set(self.clear()), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_clear.grid(row=0, column=0, sticky='we')
        self.btn_clear_entry = tk.Button(self.op_frame, text='CE', command= lambda: self._stringCalc.set(self.clear()), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_clear_entry.grid(row=0, column=1, sticky='we')
        self.btn_backspace = tk.Button(self.op_frame, text='🡐', command= lambda: self._stringCalc.set(self.backSpace()), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_backspace.grid(row=0, column=2, sticky='we')

        #Operations
        self.btn_plus = tk.Button(self.op_frame, text='+', command= lambda: self._stringCalc.set(self.addChar('+')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_plus.grid(row=1, column=0, sticky='we')
        self.btn_minus = tk.Button(self.op_frame, text='-', command= lambda: self._stringCalc.set(self.addChar('-')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_minus.grid(row=1, column=1, sticky='we')
        self.btn_multiply = tk.Button(self.op_frame, text='🞶', command= lambda: self._stringCalc.set(self.addChar('*')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_multiply.grid(row=1, column=2, sticky='we')
        self.btn_division = tk.Button(self.op_frame, text='/', command= lambda: self._stringCalc.set(self.addChar('/')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_division.grid(row=2, column=0, sticky='we')
        self.btn_open_parent = tk.Button(self.op_frame, text='(', command= lambda: self._stringCalc.set(self.addChar('(')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_open_parent.grid(row=2, column=1, sticky='we')
        self.btn_close_parent = tk.Button(self.op_frame, text=')', command= lambda: self._stringCalc.set(self.addChar(')')), font=('Arial', 16), background='#4d4d4d', fg='#ffffff')
        self.btn_close_parent.grid(row=2, column=2, sticky='we')

        self.op_frame.pack(padx=15, fill='x')

        #self.btn_quit = tk.Button(self.root, text="Quit", font=('Arial', 16), background='#4d4d4d', fg='#ffffff', width=15, command=self.root.destroy).pack()

        self.root.mainloop()


PyculatorGUI()