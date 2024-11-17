import sqlite3

class sqlite_db:
    def __init__(self, banco=None):
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)

    def open(self, banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("conexão criada com sucesso!")
        except sqlite3.Error as e:
            print("Não foi possível estabelecer conexão!")

    def criar_tabelas(self):
        cur = self.cursor
        cur.execute("""CREATE TABLE funcs(
            id integer primary key autoincrement,
            nome text NOT NULL,
            endereço text NOT NULL,
            documento integer NOT NULL,
            admin integer
            )""")

    def inserir_apaga_atualiza(self, query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()

    def pega_dados(self, query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()

db = sqlite_db("manager.db")



#APAGAR
#db.inserir_apaga_atualiza("DELETE FROM funcs WHERE nome='IGOR'") 

#INSERIR
db.inserir_apaga_atualiza("INSERT INTO funcs (nome, documento, endereco, admin) VALUES ('Paulo', '13894532', 'Avenida Nações Unidas', '127')") 


#ATUALIZAR
#db.inserir_apaga_atualiza("UPDATE funcs SET nome=' IgorTech' WHERE nome='IGOR'")

#SELECIONAR
#print(db.pega_dados("SELECT * FROM funcs")[1][3]) #PEGA TUDO DE FUNCIONARIOS

#INSERIR LOGIN
#db.inserir_apaga_atualiza("INSERT INTO user (username, password, acesso) VALUES ('Jose', '2409', 'admin') ")




#db = sqlite_db("fun.db")
#db = sqlite_db("user.db")

#db = sqlite_db("add.db")
#db.criar_tabelas()

#db = sqlite_db("manager.db")
#db.criar_tabelas()

#nome = "Homer"
#endereço = "AV Ações Unidas"
#cpf = "41223456786"
#id = "A29"
#db.inserir_apaga_atualiza("INSERT INTO funcs (nome, documento, endereco, admin) VALUES ('{}', '{}', '{}', '{}')".format(nome, cpf, endereço, id))
