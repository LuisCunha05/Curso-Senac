"""Crie um modelo usando Tkinter, com banco de dados, que terá 3 tipos de acesso: admin, cliente, famoso. O admin é obrigado a logar para poder criar as fofocas, o cliente não é obrigado a logar e pode só seguir a navegação pela página sem realizar o login, o famoso deve fazer o login para reportar alguma fofoca sobre ele, que ele não tenha gostado.
O login do cliente serve somente para acumular pontos pela sua leitura frequente de fofocas.
Cada fofoca criada deve conter: 3 imagens e um textos."""

import tkinter as tk
import urllib.request
import hashlib
import mysql.connector as sql
from tkinter import messagebox
from typing import Literal

class Fofoca:
    colorBG = '#AF9BEF'
    colorBT = '#4CAF50'
    colorBB = '#90cdd5'

    configServerDB = {
        'host':'10.28.2.34',
        'user':'suporte',
        'password':'suporte',
        'database':'fofoca'
    }
    configLocalDB = {
        'host':'127.0.0.1',
        'user':'root',
        'password':'',
        'database':'fofoca'
    }

    def __init__(self) -> None:
        self.main = tk.Tk()
        #setGeometry(self.main, scale=0.5, width=500)
        self.main.state('zoomed')
        self.main.title('Fofoca.com')
        self.main.configure(background='#d59890')

        self.USE_LOCAL_DB = False
        
        

        self.home()

        self.main.mainloop()
    
    def home(self):
        #Header
        self.fHeader = tk.Frame(self.main, background=self.colorBB)
        self.fHeader.place(relwidth=0.8, height=50, anchor='n', rely=0.02, relx=0.5)

        self.bEntrar = tk.Button(self.fHeader, text='Entrar', foreground='white', background=self.colorBB, font=getFont('Courier New', 14), border=0, relief='groove', command=self.login)
        self.bEntrar.place(relx=0, rely=0.5, anchor='w', relheight=1)

        tk.Label(self.fHeader, text='Fofoca.com', foreground='white', background=self.colorBB, font=getFont('Courier New', 32)).place(relx=0.5, rely=0.5, anchor='center')

        self.lPonto = tk.Label(self.fHeader, text='Pontos: 0', foreground='white', background=self.colorBB, font=getFont('Courier New', 14))
        #self.lPonto.place(relx=1, rely=0.5, anchor='e', relheight=1)

        #Content
        self.fContent = tk.Frame(self.main, background='red', height=700)
        self.fContent.place(relx=0.5, rely=0.1, relwidth=0.8, anchor='n')

        #Footer
        self.fFooter = tk.Frame(self.main, background=self.colorBB)
        self.fFooter.place(relwidth=0.8, height=60, anchor='n', rely=0.85, relx=0.5)

        self.bVoltar = tk.Button(self.fFooter, text='Voltar', foreground='white', background=self.colorBB, font=getFont('Courier New', 14), border=0, relief='groove', command=lambda: print('Voltar'))
        self.bVoltar.place(relx=0, rely=0.5, anchor='w', relheight=1)

        self.bReportar = tk.Button(self.fFooter, text='Reportar', foreground='white', background=self.colorBB, font=getFont('Courier New', 14), border=0, relief='groove', command=lambda: print('Report'))
        #self.bReportar.place(relx=0.5, rely=0.5, anchor='center', relheight=1)

        self.bAvancar = tk.Button(self.fFooter, text='Avançar', foreground='white', background=self.colorBB, font=getFont('Courier New', 14), border=0, relief='groove', command=self.placeReport)
        self.bAvancar.place(relx=1, rely=0.5, anchor='e', relheight=1)

        self.USE_LOCAL_DB = messagebox.askyesno('Usar Database local?', 'Deseja usar a database local?')
        self.main.focus_force() #This fixes a bug where entry doesn't work until windown re-gain focus

    def login(self):
        if(hasattr(self, 'fLogin')):
            self.fLogin.place(relheight=1, relwidth=1)
            return

        self.fLogin = tk.Frame(self.main, background=self.colorBG)
        self.fLogin.place(relheight=1, relwidth=1)

        holder = tk.Frame(self.fLogin, background='green')
        holder.place(relx=0.5, rely=0.4, width=400, anchor='center')

        tk.Label(holder, text='Bem Vindo!', font=getFont('Courier New'), foreground='white', background=self.colorBG).pack(pady=20)

        #User
        tk.Label(holder, text='Usuário', font=getFont('Courier New'), foreground='white', background=self.colorBG, anchor='w', justify='left').pack(padx=20, fill='x')
        self.eUser = tk.Entry(holder, font=getFont('Courier New', 14), foreground='gray')
        self.eUser.pack(padx=20, fill='x')

        #password
        tk.Label(holder, text='Senha', font=getFont('Courier New'), foreground='white', background=self.colorBG, anchor='w', justify='left').pack(padx=20, fill='x')
        self.ePassword = tk.Entry(holder, font=getFont('Courier New', 14), foreground='gray')
        self.ePassword.pack(padx=20, fill='x')
        self.ePassword.config(show='*')

        def showOrHidePassword():
            if(self.showPassword.get()):
                self.ePassword.config(show='')
                return
            self.ePassword.config(show='*')

        self.showPassword = tk.IntVar()
        tk.Checkbutton(holder, text='Mostrar Senha',foreground='white', font=getFont('Courier New', 14), variable=self.showPassword, background='green', command=showOrHidePassword).pack(padx=20, anchor='w')

        #Button
        buttons = tk.Frame(holder, background='green')
        buttons.pack(pady=20, padx=60, fill='x')
        tk.Button(buttons, text='Entrar', foreground='white', background=self.colorBT, font=getFont('Courier New'), border=0, relief='groove', command=self.validateLogin).pack(side='right')

        tk.Button(buttons, text='Voltar', foreground='white', background='red', font=getFont('Courier New'), border=0, relief='groove', command=self.fLogin.place_forget).pack(side='left')

    def validateLogin(self):
        user = self.eUser.get()
        password = toSHA256(self.ePassword.get())

        if(not self.connectDB()):
            return
        try:
            self.cursor.execute("select id_user,passw,id_user_type from usuario where username = %(user)s", {'user':user})
            data = self.cursor.fetchone()
            print(data)

            if(not data):
                messagebox.showerror('Login Inexistente!', 'Login não encontrado!')
                return
            
            userID, passwordDb, userType = data

            if(passwordDb != password):
                messagebox.showerror('Senha Incorreta!', 'Senha Incorreta!\nTente Novamente!')
                return
            
            self.db.disconnect()
        except Exception as e:
            messagebox.showerror('Algo deu errado!', f'Algo deu errado!\nErro: {e}')
            return

        self.eUser.delete(0, 'end')
        self.ePassword.delete(0, 'end')
        self.main.focus()
        self.lastUser = user
        self.lastUserID = userID
        self.lastUserType = userType

        #handle ui changes based in the new logged user
        self.forgetPoints()
        self.forgetReport()
        match(userType):
            case 1:
                print('Admin')
            case 2:
                self.placeReport()
            case 3:
                self.placePoints()

        self.bEntrar.configure(text=user.capitalize())
        self.fLogin.place_forget()

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

    def placeReport(self):
        if(self.bReportar.winfo_viewable()):
            return
        self.bReportar.place(relx=0.5, rely=0.5, anchor='center', relheight=1)

    def forgetReport(self):
        if(self.bReportar.winfo_viewable()):
            self.bReportar.place_forget()
    
    def placePoints(self):
        if(self.lPonto.winfo_viewable()):
            return
        self.lPonto.place(relx=1, rely=0.5, anchor='e', relheight=1)

    def forgetPoints(self):
        if(self.lPonto.winfo_viewable()):
            self.lPonto.place_forget()




def getImageFromUrl(url:str) -> bytes:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        #print(result)
        return result
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code}")
        return None

def getFont(name: Literal['Helvetica', 'Arial', 'Segoe UI', 'Comic Sans MS', 'Calibri', 'Courier New'] = 'Helvetica', size: int = 16, style: Literal['bold', 'italic'] = 'normal') -> tuple[str,int,str]:
    return (name, size, style)

def toSHA256(string: str) -> str:
    """Returns the Hash of the given string using SHA256"""
    return hashlib.sha256(string.encode()).hexdigest()

if(__name__ == '__main__'):
    Fofoca()