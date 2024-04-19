import mysql.connector

class Conexao():
    def conectar():
        #conectando ao banco de dados
        mydb = mysql.connector.connect(
        host="projetochat2.mysql.database.azure.com",
        user="equipe",
        password="123456789",
        database="CRABIZ"
        )

        return mydb
    
# python -m pip install mysql-connector-python