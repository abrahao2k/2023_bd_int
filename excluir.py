# IMPORTAR O DRIVER
import mariadb
# CRIAR A CONEXÃO
conexao = mariadb.connect(host="localhost",user="root",password="",
                          database="concurso")
# CRIAR O CURSOR
cursor = conexao.cursor()
#print("Conectou.")

print("=== EXCLUIR REGISTRO ===")
id_cand = input("Digite o ID do candidato: ")

cmd = "SELECT * FROM candidato WHERE id = " + id_cand
cursor.execute(cmd)

dados = cursor.fetchall()
if len(dados) == 0 :
    print("Candidato não encontrado.")
else:
    print(dados)
    resposta = input("Excluir esse registro? (s/n) ")
    if resposta.lower() == "s":
        cursor.execute("DELETE FROM candidato WHERE id = " + id_cand)
        conexao.commit()
        print("Registro excluído.")

cursor.close()
conexao.close()
print("Fim do programa. Até a próxima!")
        
    
    
    
    
    
    