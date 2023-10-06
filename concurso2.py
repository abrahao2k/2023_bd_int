# CONEXAO COM BANCO
import mariadb    #importar o driver
conexao = mariadb.connect(
    host="localhost", user="root",
    password="", database="concurso")
#print("Conexao OK.")
cursor = conexao.cursor()
#######################################
print("=== PESQUISAR CANDIDATO ===")
pesquisa = input("Digite o nome: ")
sql = f"SELECT * FROM candidato WHERE nome LIKE '%{pesquisa}%' "
cursor.execute(sql)
if cursor.rowcount > 0 :
    for linha in cursor:
        print(linha[1], linha[2])
else:
    print("Candidato não encontrado.")