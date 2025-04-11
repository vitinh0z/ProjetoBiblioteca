from db import inicializar_banco
from catalogoLivros import listar_livros

inicializar_banco()  # Garantir que a tabela 'usuarios' exista

print("1 - Cadastrar")
print("2 - Fazer login")
opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    from cadastro import cadastro, salvar_no_banco
    dados = cadastro()
    salvar_no_banco(dados["usuario"], dados["email"], dados["senha"])
    print("Cadastro realizado com sucesso!")

elif opcao == 2:
    from Login import fazer_login
    if fazer_login():
        print("Bem-vindo!")

        print("\nBiblioteca Orlando Signorelli")
        print("Escolha uma opção:")
        print("1 - Catálogo de Livros")
        print("2 - Buscar Livros")
        print("3 - Emprestar Livros")
        print("4 - Sair")

        while True:
            escolha = input("Digite a opção desejada: ")

            if escolha == "1":
                print("Você acessou o Catálogo de Livros.")
                listar_livros()

            elif escolha == "2":
                print("Você iniciou a busca por livros.")

            elif escolha == "3":
                print("Você iniciou o processo de emprestar livros.")

            elif escolha == "4":
                print("Saindo da biblioteca...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Email ou senha incorretos.")

else:
    print("Opção inválida. Tente novamente.")
