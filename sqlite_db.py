import sqlite3

class DB:
    def __init__(self, nome: str) -> None:
        self.nome = nome
    
    def conectar(self):
        self.db = sqlite3.connect(self.nome)
        self.cursor = self.db.cursor()

    def fechar(self):
        self.cursor.close()
        self.db.close()

    def commit(self):
        self.db.commit()
    
    def exec(self, query: str, args = ()):
        self.cursor.execute(query, args)

    def f_all(self):
        return self.cursor.fetchall()
    
    def f_many(self, quantidade: int):
        return self.cursor.fetchmany(size=quantidade)
    
    def f_one(self):
        return self.cursor.fetchone()
