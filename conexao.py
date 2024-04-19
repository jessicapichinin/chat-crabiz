import mysql.connector

class Conexao():
    def conectar():
        #conectando ao banco de dados
        mydb = mysql.connector.connect(
        host="10.110.140.130",
        user="equipe",
        password="123456789",
        database="CRABIZ"
        )

        return mydb
    
# python -m pip install mysql-connector-python