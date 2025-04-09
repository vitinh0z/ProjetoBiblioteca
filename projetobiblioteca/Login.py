


while True:
    usuario = input("Digite Nome do Usuario: ")
    senha = input("Digite Senha: ")

    if usuario == cadastroUsuario and senha == cadastroSenha:
        print("Login bem-sucedido!\n")
        print(f"Bem vindo {usuario}")
        break 

    else:
        print("Login ou senha incorretos. Tente novamente.\n")

        
