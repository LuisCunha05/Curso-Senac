
import tkinter as tk
from tkinter import messagebox
import mysql.connector as sql



class LoginDB:
    fontM = ('Helvetica', 14)
    fontG = ('Helvetica', 18)
    colorBG = '#AF9BEF'
    colorBT = '#4CAF50'

    USE_LOCAL_DB = True # Change this depending on environment 

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
        setGeometry(self.main, scale=0.4, width=500)
        self.main.title('Login')
        #self.main.wm_attributes('-transparentcolor','purple')
        if(self.USE_LOCAL_DB):
            self.db = sql.connect(**self.configLocalDB)
        else:
            self.db = sql.connect(**self.configServerDB)
        self.cursor = self.db.cursor()


        self.login()

        self.main.mainloop()

    def login(self):
        if(hasattr(self, 'fLogin')):
            self.fLogin.tkraise()
            return

        self.fLogin = tk.Frame(self.main, background=self.colorBG)
        self.fLogin.place(relheight=1, relwidth=1)

        tk.Label(self.fLogin, text='Bem Vindo!', font=self.fontG, foreground='white', background=self.colorBG).pack(pady=20)

        tk.Label(self.fLogin, text='Usuário', font=self.fontG, foreground='white', background=self.colorBG, anchor='w', justify='left').pack(padx=100, fill='x')
        self.eUser = tk.Entry(self.fLogin, font=self.fontM, foreground='gray')
        self.eUser.pack(padx=100, fill='x')

        tk.Label(self.fLogin, text='Senha', font=self.fontG, foreground='white', background=self.colorBG, anchor='w', justify='left').pack(padx=100, fill='x')
        self.ePassword = tk.Entry(self.fLogin, font=self.fontM, foreground='gray')
        self.ePassword.pack(padx=100, fill='x')
        self.ePassword.config(show='*')

        tk.Button(self.fLogin, text='Entrar', foreground='white', background=self.colorBT, font=self.fontG, border=0, relief='groove', command=self.validateLogin).pack(pady=20)

    def cadastro(self):
        if(hasattr(self, 'fCadastro')):
            self.fCadastro.tkraise()
            return

        self.fCadastro = tk.Frame(self.main, background='purple')
        self.fCadastro.place(relheight=1, relwidth=1)

        tk.Label(self.fCadastro, text='Novo Usuário', font=self.fontG, foreground='white', background=self.colorBG).pack(pady=20)

        #Usuário
        tk.Label(self.fCadastro, text='Usuário', font=self.fontG, foreground='white', background=self.colorBG, anchor='w', justify='left').pack(padx=100, fill='x')
        self.eCadUser = tk.Entry(self.fCadastro, font=self.fontM, foreground='gray')
        self.eCadUser.pack(padx=100, fill='x')

        #Senha
        tk.Label(self.fCadastro, text='Senha', font=self.fontG, foreground='white', background=self.colorBG, anchor='w', justify='left').pack(padx=100, fill='x')
        self.eCadPassword = tk.Entry(self.fCadastro, font=self.fontM, foreground='gray')
        self.eCadPassword.pack(padx=100, fill='x')
        self.eCadPassword.config(show='*')

        #Confirmar Senha
        tk.Label(self.fCadastro, text='Confirmar Senha', font=self.fontG, foreground='white', background=self.colorBG, anchor='w', justify='left').pack(padx=100, fill='x')
        self.eCadConfword = tk.Entry(self.fCadastro, font=self.fontM, foreground='gray')
        self.eCadConfword.pack(padx=100, fill='x')
        self.eCadConfword.config(show='*')

        #Texto do Usuário
        tk.Label(self.fCadastro, text='Digite uma mensagem!', font=self.fontG, foreground='white', background=self.colorBG, anchor='w', justify='left').pack(padx=100, fill='x')
        self.eCadText = tk.Text(self.fCadastro, font=self.fontM, foreground='white', background='gray', height=3)
        self.eCadText.pack(padx=100, fill='x')

        tk.Button(self.fCadastro, text='Cadastrar', foreground='white', background=self.colorBT, font=self.fontG, border=0, relief='groove', command=self.validateCad).pack(pady=20)

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
            if(messagebox.askyesno('Deseja se cadastrar?', 'Deseja criar um novo usuário?')):
                self.cadastro()
            return
        
        self.cursor.execute(f"select IF((SELECT senha from usuario where id_user={userID}) = SHA2('{password}', 256), 1, 0)")
        senha = self.cursor.fetchall()
        senha= senha[0][0]
        if(not senha):
            messagebox.showerror('Senha Incorreta!', 'Senha Incorreta!')
            return
        print('yooooooooooooooo')

    def validateCad(self):
        #object.user = utk.Entry.get()
        user = self.eCadUser.get()
        password = self.eCadPassword.get()
        cpassword = self.eCadConfword.get()
        uText = self.eCadText.get("1.0", "end-1c")

        try:
            self.cursor.execute(f"select id_user from usuario where login_user='{user}'")
            exists = self.cursor.fetchone()
        except:
            messagebox.showerror('Algo deu errado!', f'O cadastro não pode ser finalizado!\nErro: {e}')
            return
        
        if(exists):
            messagebox.showerror('Usuário já existe!', 'O nome de usuário já existe!')
            return
        elif(user == '' or len(user) < 5):
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
        elif(len(uText)> 256):
            messagebox.showerror('Mensagem é muito longa', 'A mensagem não pode ser maior que 256 caracteres.')
            return

        try:
            self.cursor.execute(f"insert into usuario values (NULL, '{user}', SHA2('{password}', 256), '{uText}')")
            self.db.commit()
            messagebox.showinfo('Cadastrado', 'Cadrastro realizado com sucesso!\nClique para voltar ao a página do Login')
            self.login()
        except Exception as e:
            messagebox.showerror('Algo deu errado!', f'O cadastro não pode ser finalizado!\nErro: {e}')
            return

        self.eCadUser.delete(0, 'end')
        self.eCadPassword.delete(0, 'end')
        self.eCadConfword.delete(0, 'end')
        self.eCadText.delete("1.0", "end-1c")
        self.main.focus()

def setGeometry(master:tk.Tk, scale:float = 0.7, width:int = None, height:int = None,x:int = None, y:int = None, resizable:bool = True):
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