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
    EMPTY = ''
    __symbols = ['+', '-', '/', '*', '.']
    MAX_INT = 9223372036854775807
    def __init__(self) -> None:
        self.__expression: str = self.EMPTY
        self.__number: str = '0'
        self.__openP: int = 0
        self.__closeP: int = 0
        self.__clearNumber: bool = False
    
    def addChar(self, char: str) -> str:
        """Adds a character to the Calculation string. CANNOT add a new symbol if the last character is a symbol"""

        if(char.isnumeric() or char == '.'):
            self.addNumber(char)
            return self.get
        self.addSymbol(char)


    def addNumber(self, char:str) -> str:
        if(char == 'C'):
            self.unsetCleanable()
            return self.setNumber('0')
        elif(char == '='):
            return self.setNumber(eval(self.getExpression() + self.getNumber()))

        elif(self.getNumber() == '0' or self.getCleanable()):
            self.unsetCleanable()
            if(char == '.'):
                char = '0.'
            return self.setNumber(char)
        elif(char  == '.' and '.' in self.getNumber() or float(self.getNumber() + char) > self.MAX_INT or len(self.getNumber() + char) > len(str(self.MAX_INT))):
            char = self.EMPTY
        

        return self.addToNumber(char)
    
    def addSymbol(self, char: str) -> str:
        self.setCleanable()
        match(char):
            case 'CE':
                return self.clearExpression()
            case '(':
                self.addOpenParenthesis()
                if(self.getExpression() != self.EMPTY):
                    char = '*('
            case ')':
                if(self.getCloseParenthesis() < self.getOpenParenthesis()):
                    self.addCloseParenthesis()
                else:
                    char = self.EMPTY
            case '🞶':
                char = '*'
        result = self.getNumber() + char if char != self.EMPTY else self.EMPTY
        return self.addToExpression(result)

    def getLastChar(self) -> str:
        return self.__expression[-1]

    def getLastDigit(self) -> str:
        return self.__number[-1]
    
    def clear(self) -> str:
        return self.setNumber('0')
    
    def clearExpression(self) -> str:
        return self.setExpression(self.EMPTY)

    def backSpace(self) -> str:
        match(self.getLastChar()):
            case '(':
                self.removeOpenParenthesis()
            case ')':
                self.removeCloseParenthesis()

        self.__expression = '0' if self.__expression[:-1] == self.EMPTY else self.__expression[:-1]
        return self.__expression
    
    def getNumber(self) -> str:
        return self.__number
    
    def setNumber(self, num: str) -> str:
        self.__number = num
        return self.__number
    
    def addToNumber(self, char: str) -> str:
        self.__number += char
        return self.__number
    
    def getExpression(self) -> str:
        return self.__expression
    
    def setExpression(self, char: str) -> str:
        self.__expression = char
        return self.__expression
    
    def addToExpression(self, char:str) -> str:
        self.__expression += char
        return self.__expression
    
    def getOpenParenthesis(self):
        return self.__openP

    def addOpenParenthesis(self):
        self.__openP += 1

    def removeOpenParenthesis(self):
        if(self.__openP > 0):
            self.__openP -= 1

    def getCloseParenthesis(self):
        return self.__closeP

    def addCloseParenthesis(self):
        self.__closeP += 1

    def removeCloseParenthesis(self):
        if(self.__closeP > 0):
            self.__closeP -= 1
    
    def setCleanable(self):
        """Sets the Number field to be reseted in the next number input"""
        self.__clearNumber = True
    
    def unsetCleanable(self):
        """Unsets the Number field to be reseted in the next number input"""
        self.__clearNumber = False
    
    def getCleanable(self) -> bool:
        """Get current Number field status for reseting"""
        return self.__clearNumber



class PyculatorGUI(Pyculator):
    __FontS = ('Arial', 16)
    __ColorLG = '#4d4d4d'
    __ColorDG = '#282828'
    def __init__(self) -> None:
        super().__init__()

        self.root = tk.Tk()
        setGeometry(self.root, 350, 480,None,None, False)
        self.root.title('Pyculator')
        self.root.configure(background=self.__ColorDG)

        self._stringExp = tk.StringVar()
        self._stringExp.set(self.getExpression())
        self._stringNumber = tk.StringVar()
        self._stringNumber.set(self.getNumber())

        #Label Expression
        tk.Label(
            self.root,
            textvariable=self._stringExp,
            font=('Arial', 14),
            height=3,
            highlightthickness=1,
            highlightbackground='gray',
            background=self.__ColorDG,
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
            background=self.__ColorDG,
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
            ('C',   0, True), ('CE',  1, False), ('🡐', 2, False),('(',  3, False),
            (')',   0, False),('x^y', 1, False), ('√',  2, False),('+',  3, False),
            ('7',   0, True), ('8',   1, True),  ('9',  2, True),('-',  3, False),
            ('4',   0, True), ('5',   1, True),  ('6',  2, True),('🞶', 3, False),
            ('1',   0, True), ('2',   1, True),  ('3',  2, True),('/',  3, False),
            ('+/-', 0, False),('0',   1, True),  ('.',  2, True),('=',  3, True),
        ]
        row = 0
        for char, col, isnum in botoes_num:
            tk.Button(
                self.btn_frame,
                text=char,
                command= lambda x = char, var=isnum: self._stringNumber.set(self.addNumber(x)) if var else self._stringExp.set(self.addSymbol(x)),
                font=self.__FontS,
                background=self.__ColorLG if char != '=' else '#007fff',
                fg='white',
                relief='groove'
            ).grid(row=row, column=col, sticky='we')

            if(col == 3): row += 1

        self.root.mainloop()

if __name__ == '__main__':
    PyculatorGUI()