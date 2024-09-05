import tkinter as tk

def getLastNumber(string: str) -> str:
    result = ''
    for i in range(len(string)):
        print('debugg1:',string, string[-(i+1)].isnumeric())
        if(string[-(i+1)].isnumeric() or string[-(i+1)] == '.'):
            result += string[-(i+1)]
        else:
            break
    return result[::-1]

def setGeometry(master:tk.Tk, width:int = None, height:int = None,x:int = None, y:int = None, resizable:bool = True):
    """Sets the window size and put it at center of the screen.
    If WIDTH or HEIGHT were given than uses this values instead."""
    x = x if x else int((master.winfo_screenwidth() - width) / 2)
    y = y if y else int((master.winfo_screenheight() - height) / 2)

    master.geometry(f'{width}x{height}+{x}+{y}')
    master.resizable(resizable, resizable)

class Pyculator:
    __symbols = ['+', '-', '/', '*', '.']
    MAX_INT = 9223372036854775807
    def __init__(self) -> None:
        self.expression: str = ''
        self.number: str = '0'
        self._parent_open: int = 0
        self._parent_close: int = 0
    
    def addChar(self, char: str) -> str:
        """Adds a character to the Calculation string. CANNOT add a new symbol if the last character is a symbol"""

        if(char.isnumeric() or char == '.'):
            self.addChar(char)
        

        #lastChar = self.getLastChar()
        #lastNum = getLastNumber(self.expression)
        
    def addNumber(self, char:str) -> str:
        
        if(not self.getLastChar().isnumeric()):
            self.number = char
            return char
        if(float(self.number) > self.MAX_INT):
            char = ''
        self.number += char
        return self.number
    
    def clear(self) -> str:
        self.number = '0'
        return self.number
    
    def getNumber(self) -> str:
        return self.number
    
    def setNumber(self, num: str) -> str:
        self.number = num
        return self.number
    
    def getLastChar(self) -> str:
        return self.expression[-1]

    def getLastDigit(self) -> str:
        return self.number[-1]

    def backSpace(self) -> str:
        match(self.getLastChar()):
            case '(':
                self._parent_open -= 1
            case ')':
                self._parent_close -= 1

        self.expression = '0' if self.expression[:-1] == '' else self.expression[:-1]
        return self.expression



class PyculatorGUI(Pyculator):
    __FontS = ('Arial', 16)
    __BgColor = '#4d4d4d'

    def __init__(self) -> None:
        super().__init__()

        self.root = tk.Tk()
        setGeometry(self.root, 400, 500,None,None, False)
        self.root.title('Pyculator')
        self.root.configure(background='#282828')

        self._stringExp = tk.StringVar()
        self._stringExp.set(self.expression)
        self._stringNumber = tk.StringVar()
        self._stringNumber.set(self.number)

        #Label Expression
        tk.Label(
            self.root,
            textvariable=self._stringExp,
            font=('Arial', 14),
            height=3,
            highlightthickness=1,
            highlightbackground='gray',
            background='#282828',
            fg='white',
            justify='right',
            wraplength=368,
            anchor='se'
        ).pack(padx=15,pady=(15,1), fill='x')
        #Label Number
        tk.Label(
            self.root,
            textvariable=self._stringNumber,
            font=('Arial', 14),
            height=1,
            highlightthickness=1,
            highlightbackground='gray',
            background='#282828',
            fg='white',
            justify='right',
            wraplength=368,
            anchor='se'
        ).pack(padx=15,pady=(1,15), fill='x')

        #Numeric Frame
        self.btn_frame = tk.Frame(self.root)
        for i in range(4):
            self.btn_frame.columnconfigure(i, weight=1)
        self.btn_frame.pack(padx=15, pady=15, fill='x')

        #Numbers
        botoes_num = [
            ('C', 0, 0), ('CE', 0, 1), ('🡐', 0, 2),('(', 0, 3),
            (')', 1, 0), ('x^y', 1, 1), ('√', 1, 2),('+', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),('-', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),('🞶', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),('/', 4, 3),
            ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2),('=', 5, 3),
        ]

        for char, row, col in botoes_num:
            tk.Button(
                self.btn_frame,
                text=char,
                command= lambda x = char: self._stringNumber.set(self.addChar(x)),
                font=self.__FontS,
                background=self.__BgColor if char != '=' else '#007fff',
                fg='white'
            ).grid(row=row, column=col, sticky='we')

        self.root.mainloop()

if __name__ == '__main__':
    PyculatorGUI()