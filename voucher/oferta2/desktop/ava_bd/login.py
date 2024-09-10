
from tkinter import *
from tkinter import messagebox
import mysql.connector as sql



class LoginDB:
    fontM = ('Helvetica', 14)
    fontG = ('Helvetica', 18)
    colorBG = '#AF9BEF'
    colorBT = '#4CAF50'

    configDB = {
        'host':'10.28.2.34',
        'user':'suporte',
        'password':'suporte',
        'database':'login'
    }
    def __init__(self) -> None:
        self.main = Tk()
        setGeometry(self.main, scale=0.4, width=500)
        self.main.title('Login')
        #self.main.wm_attributes('-transparentcolor','purple')
        self.db = sql.connect(**self.configDB)
        self.cursor = self.db.cursor()


        self.login()

        self.main.mainloop()

    def login(self):
        if(hasattr(self, 'fLogin')):
            self.fLogin.tkraise()
            return

        self.fLogin = Frame(self.main, background=self.colorBG)
        self.fLogin.place(relheight=1, relwidth=1)

        Label(self.fLogin, text='Bem Vindo!', font=self.fontG, foreground='white', background=self.colorBG).pack(pady=20)

        Label(self.fLogin, text='Usuário', font=self.fontG, foreground='white', background=self.colorBG, anchor='w', justify='left').pack(padx=100, fill='x')
        self.eUser = Entry(self.fLogin, font=self.fontM, foreground='gray')
        self.eUser.pack(padx=100, fill='x')

        Label(self.fLogin, text='Senha', font=self.fontG, foreground='white', background=self.colorBG, anchor='w', justify='left').pack(padx=100, fill='x')
        self.ePassword = Entry(self.fLogin, font=self.fontM, foreground='gray')
        self.ePassword.pack(padx=100, fill='x')
        self.ePassword.config(show='*')

        Button(self.fLogin, text='Entrar', foreground='white', background=self.colorBT, font=self.fontG, border=0, relief='groove', command=self.validateLogin).pack(pady=20)

        #self.cursor.execute('select senha from usuario')
        #opa = self.cursor.fetchall()

    def cadastro(self):
        if(hasattr(self, 'fCadastro')):
            self.fCadastro.tkraise()
            return

        self.fCadastro = Frame(self.main, background='purple')
        self.fCadastro.place(relheight=1, relwidth=1)

    def validateLogin(self):
        user = self.eUser.get()
        password = self.ePassword.get()

        self.cursor.execute(f"select id_user from usuario where login_user='{user}'")
        userID = self.cursor.fetchall()

        try:
            userID= userID[0][0]
        except IndexError:
            print('no index logger')

        if(not userID):
            messagebox.showerror('Login Inexistente !', 'Login não encontrado!')
            return
        
        self.cursor.execute(f"select IF((SELECT senha from usuario where id_user={userID}) = SHA2('{password}', 256), 1, 0)")
        senha = self.cursor.fetchall()
        senha= senha[0][0]
        if(not senha):
            messagebox.showerror('Senha Incorreta!', 'Senha Incorreta!')
            return
        
        self.cadastro()
        



def validateCad(uEntry:Entry, pEntry:Entry, cpEntry:Entry):
    #object.user = uEntry.get()
    user = uEntry.get()
    password = pEntry.get()
    cpassword = cpEntry.get()

    if(user == '' or len(user) < 5):
        messagebox.showerror('Login Incorreto!', 'O login é muito curto!')
        return
    elif(password == '' or len(password) < 6):
        messagebox.showerror('Senha Invalida!', 'A senha é muito curta!')
        return
    elif(user == password):
        messagebox.showwarning('Senha Invalida!', 'A senha não pode ser igual ao login!')
        return
    elif(password != cpassword):
        messagebox.showerror('Senha Incorreta!', 'As senhas são diferentes!')
        return

    uEntry.delete(0, 'end')
    pEntry.delete(0, 'end')
    cpEntry.delete(0, 'end')
    #object.root.focus()
    #object.home()
    #messagebox.showinfo('Cadastrado', 'Cadrastro realizado com sucesso!')

def setGeometry(master:Tk, scale:float = 0.7, width:int = None, height:int = None,x:int = None, y:int = None, resizable:bool = True):
    """Sets the window size and put it at center of the screen, by default uses 70% of the screen.
    If WIDTH or HEIGHT were given than uses this values instead."""
    width = width if width else int(master.winfo_screenwidth() * scale)
    height = height if height else int(master.winfo_screenheight() * scale)
    x = x if x else int((master.winfo_screenwidth() - width) / 2)
    y = y if y else int((master.winfo_screenheight() - height) / 2)

    master.geometry(f'{width}x{height}+{x}+{y}')
    master.resizable(resizable, resizable)


if(__name__ == '__main__'):
    LoginDB()