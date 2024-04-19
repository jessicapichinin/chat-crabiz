from usuario import Usuario
from mensagem import Mensagem
from conexao import Conexao
from contato import Contato

class Chat:
    def __init__(self, nome_usuario:str, telefone_usuario:str):
        self.nome_usuario = nome_usuario
        self.telefone_usuario = telefone_usuario

    def enviar_mensagem(self, conteudo:str, destinatario:Contato) -> bool:
        try:
            mybd = Conexao.conectar()

            mycursor = mybd.cursor()

            sql = "INSERT INTO tb_mensagem (tel_remetente, mensagem, tel_destinatario) VALUES (%s, %s, %s)"
            val = (self.telefone_usuario, conteudo, destinatario.telefone)
            mycursor.execute(sql, val)  

            mybd.commit()
            mybd.close()
            
            print(conteudo)
            return True 
        
        except:
            return False

    def verificar_mensagem(self, quantidade:int, destinatario:Contato | None=0):

        mydb = Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"SELECT nome, mensagem FROM tb_mensagem m "\
              f"INNER JOIN tb_usuario u "\
              f"ON m.tel_remetente = u.tel "\
              f"WHERE m.tel_remetente = '{self.telefone_usuario}' "\
              f"AND m.tel_destinatario = '{destinatario.telefone}' "\
              f"OR m.tel_remetente = '{destinatario.telefone}' "\
              f"AND m.tel_destinatario = '{self.telefone_usuario}' "

        mycursor.execute(sql)

        resultado = mycursor.fetchall()

        mensagens = []
        for linha in resultado:
            mensagem = {"nome":linha[0], "mensagem":linha[1]}
            mensagens.append(mensagem)
        return (mensagens)
    
    def retorna_contatos(self):
        mydb = Conexao.conectar()
        mycursor = mydb.cursor()

        sql = "SELECT nome, tel FROM tb_usuario ORDER BY nome"
        mycursor.execute(sql)

        resultado = mycursor.fetchall()

        lista_contatos = []
        
        for linha in resultado:
            # pegar contatos
            contatos = {"nome":linha[0], "telefone":linha[1]}
            lista_contatos.append(contatos)
        return(lista_contatos)