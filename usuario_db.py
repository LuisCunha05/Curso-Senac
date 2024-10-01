import sqlite_db as db

class Usuario:
    def __init__(self, nome_banco) -> None:
        self.db = db.DB(nome_banco)
        self.db.conectar()

    def criarUsuario(self, nome:str, email: str):
        query = 'insert into usuario values (NULL, ?, ?)'

        self.db.exec(query=query, args=(nome, email))
        self.db.commit()

    def listarUsuario(self):
        query = 'select nome,email from usuario'
        self.db.exec(query=query)

        for user in self.db.f_all():
            print(f'Nome: {user[0]}, Email: {user[1]}')
    
    def atualizarUsuario(self, id: int, nome: str, email: str):
        q_nome = 'update usuario set nome = ? where id_usuario = ?'
        q_email = 'update usuario set email = ? where id_usuario = ?'

        if(nome):
            self.db.exec(q_nome, (nome, id))

        if(email):
            self.db.exec(q_email, (email, id))
        
        self.db.commit()


if __name__ == '__main__':
    doido = Usuario('test_lite.db')

    doido.criarUsuario('Jão', 'jaum@gmail.com')

    doido.listarUsuario()

    doido.atualizarUsuario(4, 'Camilão', 'camilao@gmail.com')
    print('----------------------------')
    doido.listarUsuario()