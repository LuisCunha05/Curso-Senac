
import tkinter as tk
import io
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from tkinter import filedialog as fd
import mysql.connector as sql
import hashlib
from dictqueue import DictQueue


class LoginDB:
    fontM = ('Helvetica', 14)
    fontG = ('Helvetica', 18)
    colorBG = '#AF9BEF'
    colorBT = '#4CAF50'

    USE_LOCAL_DB = False # Change this depending on environment 

    configServerDB = {
        'host':'10.28.2.34',
        'user':'suporte',
        'password':'suporte',
        'database':'login'
    }
    configLocalDB = {
        'host':'127.0.0.1',
        'user':'root',
        'password':'',
        'database':'login'
    }

    def __init__(self) -> None:
        self.main = tk.Tk()
        #setGeometry(self.main, scale=0.5, width=500)
        self.main.state('zoomed')
        self.main.title('Login')
        #self.main.wm_attributes('-transparentcolor','purple')

        self.frameQ = DictQueue()

        self.login()

        self.main.mainloop()

    def connectDB(self) -> bool:
        """Returns True is connection is made successfuly and false otherwise"""
        try:
            if(self.USE_LOCAL_DB):
                self.db = sql.connect(**self.configLocalDB)
            else:
                self.db = sql.connect(**self.configServerDB)
            self.cursor = self.db.cursor()
            return True
        except Exception as e:
            print(f'Não foi possivel conectar ao bando de dados\nErro: {e}')
            return False

    def login(self):
        if(hasattr(self, 'fLogin')):
            self.fLogin.tkraise()
            return

        self.fLogin = tk.Frame(self.main, background=self.colorBG)
        self.fLogin.place(relheight=1, relwidth=1)

        tk.Label(self.fLogin, text='Bem Vindo!', font=self.fontG, foreground='white', background=self.colorBG).pack(pady=20)

        tk.Label(self.fLogin, text='Usuário', font=self.fontG, foreground='white', background=self.colorBG, anchor='w', justify='left').pack(padx=700, fill='x')
        self.eUser = tk.Entry(self.fLogin, font=self.fontM, foreground='gray')
        self.eUser.pack(padx=700, fill='x')

        tk.Label(self.fLogin, text='Senha', font=self.fontG, foreground='white', background=self.colorBG, anchor='w', justify='left').pack(padx=700, fill='x')
        self.ePassword = tk.Entry(self.fLogin, font=self.fontM, foreground='gray')
        self.ePassword.pack(padx=700, fill='x')
        self.ePassword.config(show='*')

        tk.Button(self.fLogin, text='Entrar', foreground='white', background=self.colorBT, font=self.fontG, border=0, relief='groove', command=self.validateLogin).pack(pady=20)

        self.check = tk.IntVar()
        tk.Checkbutton(self.fLogin, text='Usar Banco de Dados Local',variable=self.check, command=self.changeDB, background=self.colorBG, foreground='black', font=self.fontM).pack(pady=20)

    def changeDB(self):
        if(self.check.get()):
            self.USE_LOCAL_DB = True
        else:
            self.USE_LOCAL_DB = False

    def generateUserPage(self):
        try:
            self.frameQ.get(self.lastUser)['frame'].tkraise()
            return
        except KeyError as e:
            print(e)
            pass

        #Get user info
        if(not self.connectDB()):
            return
        
        self.cursor.execute(f'SELECT color,texto,img from usuario where login_user="{self.lastUser}"')
        color, text, blob = self.cursor.fetchone()
        self.db.disconnect()

        #Create elements
        self.frameQ.put(self.lastUser, {'frame':tk.Frame(self.main, background=color)})
        frame = self.frameQ.get(self.lastUser)['frame']
        frame.place(relheight=1, relwidth=1)

        invColor = getInverseColor(color)
        fontColor = getFontColor(invColor)

        tk.Label(frame, text=f'Bem Vindo, {self.lastUser}!', font=fontColor, foreground=fontColor, background=invColor).pack(pady=20)

        tk.Label(frame, text=f'{text}', font=self.fontM, foreground=fontColor, background=invColor, wraplength=400, height=6).pack(pady=(0,20), fill='x', padx=700)

        if(blob):
            self.frameQ.put(self.lastUser, {'img':tk.PhotoImage(data=blob, format='png')})
            tk.Label(frame, image=self.frameQ.get(self.lastUser)['img'], height=400, width=400).pack(pady=(10,0))

        tk.Button(frame, text='Sair', foreground=fontColor, background=invColor, font=self.fontG, border=0, relief='groove', command=self.login).pack(side='bottom', pady=20)


    def cadastro(self):
        if(hasattr(self, 'fCadastro')):
            self.fCadastro.tkraise()
            return

        self.fCadastro = tk.Frame(self.main, background='purple')
        self.fCadastro.place(relheight=1, relwidth=1)

        tk.Label(self.fCadastro, text='Novo Usuário', font=self.fontG, foreground='white', background='purple').pack(pady=20)

        #Usuário
        tk.Label(self.fCadastro, text='Usuário', font=self.fontG, foreground='white', background='purple', anchor='w', justify='left').pack(padx=700, fill='x')
        self.eCadUser = tk.Entry(self.fCadastro, font=self.fontM, foreground='gray')
        self.eCadUser.pack(padx=700, fill='x')

        #Senha
        tk.Label(self.fCadastro, text='Senha', font=self.fontG, foreground='white', background='purple', anchor='w', justify='left').pack(padx=700, fill='x')
        self.eCadPassword = tk.Entry(self.fCadastro, font=self.fontM, foreground='gray')
        self.eCadPassword.pack(padx=700, fill='x')
        self.eCadPassword.config(show='*')

        #Confirmar Senha
        tk.Label(self.fCadastro, text='Confirmar Senha', font=self.fontG, foreground='white', background='purple', anchor='w', justify='left').pack(padx=700, fill='x')
        self.eCadConfword = tk.Entry(self.fCadastro, font=self.fontM, foreground='gray')
        self.eCadConfword.pack(padx=700, fill='x')
        self.eCadConfword.config(show='*')

        #Texto do Usuário
        tk.Label(self.fCadastro, text='Digite uma mensagem!', font=self.fontM, foreground='white', background='purple', anchor='w', justify='left').pack(padx=700, fill='x')
        self.eCadText = tk.Text(self.fCadastro, font=self.fontM, foreground='white', background='gray', height=3)
        self.eCadText.pack(padx=700, fill='x')

        #Escolher cor
        def saveColor():
            self.color = askcolor()
            self.color = self.color[1] if self.color[1] else '#000000'

        tk.Label(self.fCadastro, text='Escolha uma Cor', font=self.fontM, foreground='white', background='purple', anchor='center', justify='left').pack(padx=700, fill='x', pady=(10, 0))
        tk.Button(self.fCadastro, text='Escolher', foreground='white', background='#a3b8c8', font=self.fontG, border=0, relief='groove', command=saveColor).pack()

        #Escolher Imagem
        tk.Label(self.fCadastro, text='Escolha uma Imagem', font=self.fontM, foreground='white', background='purple', anchor='center', justify='left').pack(padx=700, fill='x', pady=(10, 0))
        tk.Button(self.fCadastro, text='Escolher', foreground='white', background='#a3ffc8', font=self.fontG, border=0, relief='groove', command=self.select_file).pack()


        #Finalizar cadastro
        tk.Button(self.fCadastro, text='Cadastrar', foreground='white', background=self.colorBT, font=self.fontG, border=0, relief='groove', command=self.validateCad).pack(pady=20)

    def validateLogin(self):
        user = self.eUser.get()
        password = toSHA256(self.ePassword.get())

        if(not self.connectDB()):
            return

        self.cursor.execute(f"select id_user from usuario where login_user='{user}'")
        userID = self.cursor.fetchone()

        try:
            userID = userID[0]
        except TypeError:
            print('no user')

        if(not userID):
            messagebox.showerror('Login Inexistente !', 'Login não encontrado!')
            if(messagebox.askyesno('Deseja se cadastrar?', 'Deseja criar um novo usuário?')):
                self.cadastro()
            return
        
        #self.cursor.execute(f"SELECT senha from usuario where id_user={userID}")
        #senhasha = self.cursor.fetchone()
        #print(senhasha)
        #print(password)

        self.cursor.execute(f"select IF((SELECT senha from usuario where id_user={userID}) = '{password}', 1, 0)")
        senha = self.cursor.fetchone()
        senha = senha[0]

        if(not senha):
            messagebox.showerror('Senha Incorreta!', 'Senha Incorreta!\nTente Novamente!')
            return
        
        self.db.disconnect()

        self.eUser.delete(0, 'end')
        self.ePassword.delete(0, 'end')
        self.main.focus()
        self.lastUser = user
        self.generateUserPage()

    def validateCad(self):
        #object.user = utk.Entry.get()
        user = self.eCadUser.get()
        password = self.eCadPassword.get()
        cpassword = self.eCadConfword.get()
        uText = self.eCadText.get("1.0", "end-1c")

        if(not self.connectDB()):
            return

        try:
            self.cursor.execute(f"select id_user from usuario where login_user='{user}'")
            exists = self.cursor.fetchone()
        except:
            messagebox.showerror('Algo deu errado!', f'O cadastro não pode ser finalizado!\nErro: {e}')
            return
        
        if(exists):
            messagebox.showerror('Usuário já existe!', 'O nome de usuário já existe!')
            return
        elif(len(user) < 5):
            messagebox.showerror('Login Incorreto!', 'O login é muito curto!')
            return
        elif(len(password) < 6):
            messagebox.showerror('Senha Invalida!', 'A senha é muito curta!')
            return
        elif(user == password):
            messagebox.showwarning('Senha Invalida!', 'A senha não pode ser igual ao login!')
            return
        elif(password != cpassword):
            messagebox.showerror('Senha Incorreta!', 'As senhas são diferentes!')
            return
        elif(len(uText)> 256):
            messagebox.showerror('Mensagem é muito longa', 'A mensagem não pode ser maior que 256 caracteres.')
            return

        try:
            q = "insert into usuario values (NULL, %s, %s, %s, %s, %s)"
            self.cursor.execute(q, (user, toSHA256(password), self.color, uText, binaryDataFromFile(self.path)))
            self.db.commit()
            messagebox.showinfo('Cadastrado', 'Cadrastro realizado com sucesso!\nClique para voltar ao a página do Login')
            self.login()
        except Exception as e:
            messagebox.showerror('Algo deu errado!', f'O cadastro não pode ser finalizado!\nErro: {e}')
            return

        self.db.disconnect()

        self.eCadUser.delete(0, 'end')
        self.eCadPassword.delete(0, 'end')
        self.eCadConfword.delete(0, 'end')
        self.eCadText.delete("1.0", "end-1c")
        self.main.focus()

    def select_file(self):
        filetypes = (
            ('Images', '*.png'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        self.path = filename

def binaryDataFromFile(path: str) -> bytes:
    """Convert image to binary data"""
    if(path == ''):
        return None

    with open(path, 'rb') as file:
        binaryData = file.read()

    return binaryData

def setGeometry(master:tk.Tk, scale:float = 0.7, width:int = None, height:int = None,x:int = None, y:int = None, resizable:bool = True):
    """Sets the window size and put it at center of the screen, by default uses 70% of the screen.
    If WIDTH or HEIGHT were given than uses this values instead."""
    width = width if width else int(master.winfo_screenwidth() * scale)
    height = height if height else int(master.winfo_screenheight() * scale)
    x = x if x else int((master.winfo_screenwidth() - width) / 2)
    y = y if y else int((master.winfo_screenheight() - height) / 2)

    master.geometry(f'{width}x{height}+{x}+{y}')
    master.resizable(resizable, resizable)

def toSHA256(string: str) -> str:
    """Returns the Hash of the given string using SHA256"""
    return hashlib.sha256(string.encode()).hexdigest()

def getFontColor(color: str) -> str:
    color = color[1:]

    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)

    if (red*0.299 + green*0.587 + blue*0.114) > 150: #186
        return '#000000'
    else:
        return '#ffffff'
    
def getInverseColor(color: str) -> str:
    color = color[1:]
    
    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)

    red = 255 - red
    green = 255 - green
    blue = 255 - blue

    return f'#{red:02x}{green:02x}{blue:02x}'

if(__name__ == '__main__'):
    LoginDB()