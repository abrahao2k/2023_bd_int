import mariadb
conexao = mariadb.connect(host="localhost",user="root",password="",
                          database="concurso")
cursor = conexao.cursor()
print("=== ATUALIZAR REGISTRO ===")
id_cand = input("Digite o ID do candidato: ")
cmd = "SELECT * FROM candidato WHERE id = " + id_cand
cursor.execute(cmd)
dados = cursor.fetchall()
if len(dados) == 0 :
    print("Candidato não encontrado.")
else:
    
    print(f"nome: {dados[0][1]}")
    print(f"pontuacao: {dados[0][2]}")
    
    coluna = input("Qual coluna deseja alterar? ")
    
    if coluna in ("nome", "pontuacao"):
        conteudo  = input("Qual o novo conteúdo? ")
        cmd = f'''UPDATE candidato SET {coluna} = "{conteudo}"
                  WHERE id = {id_cand};'''
        cursor.execute(cmd)
        conexao.commit()
        print("Atualizado com sucesso.")
    else:
        print("Essa coluna não existe. Tente novamente.")
        
cursor.close()
conexao.close()
print("Fim do programa. Até a próxima!")
    