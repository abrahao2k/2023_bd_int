# CONEXAO COM BANCO
import mariadb    #importar o driver
conexao = mariadb.connect(
    host="localhost", user="root",
    password="", database="concurso")
#print("Conexao OK.")
cursor = conexao.cursor()
#######################################
nome = input("Nome do candidato: ")
pontos = input("Pontos: ")

#sql = "INSERT INTO candidato VALUES(null, %s, %s)"
#cursor.execute(sql, (nome, pontos) )

sql = f"INSERT INTO candidato VALUES(null, '{nome}', '{pontos}')"
cursor.execute(sql)

conexao.commit()  # confirma a gravação no banco
print("Inserido com sucesso.")

## CONSULTAR OS DADOS DA TABELA ##
cursor.execute("SELECT * FROM candidato")

for linha in cursor:    # trabalha uma linha por vez
    print(linha[1], linha[2])

print(cursor.rowcount, "registros encontrados.")
#rowcount - contagem de linhas (resultados)
