from conexao import Conexao
from hashlib import sha256

class Usuario:
    def __init__(self):
        self.tel = None
        self.nome = None
        self.senha = None
        self.logado = False

    def cadastrar(self, tel, nome, senha):
        # criptografando a senha
        senha = sha256(senha.encode()).hexdigest()
        try:
            #conectando ao banco de dados

            mydb = Conexao.conectar()

            #criando o cursor
            mycursor = mydb.cursor()

            sql = "INSERT INTO tb_usuario (tel, nome, senha) VALUES (%s, %s, %s)"
            val = (tel, nome, senha)
            mycursor.execute(sql, val)

            mydb.commit()
            mydb.close()

            self.tel = tel
            self.nome = nome
            self.senha = senha
            self.logado = True

            return True

        except:
            return False
        
    def verificar(self):
        try:
            if self.tel == self.tel:
                return True
        except:
            return False
        
    def logar(self, tel, senha):
        # criptografando a senha
        senha = sha256(senha.encode()).hexdigest()

        mybd = Conexao.conectar()

        mycursor = mybd.cursor()

        sql = ("SELECT tel, nome, senha FROM tb_usuario WHERE tel = %s AND senha = %s")
        valores = (tel, senha)
        mycursor.execute(sql, valores)

        resultado = mycursor.fetchone()

        if not resultado == None:
            self.logado = True
            self.nome = resultado[1]
            self.tel = resultado[0]
            self.senha = resultado[2]

        else:
            self.logado = False