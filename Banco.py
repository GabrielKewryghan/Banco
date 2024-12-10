#cadastro do usuario e senha
saldo = 0.0
#Menu principal
while True:
    print ("Bem vindo! \n Digite 1.cadastrar 2.login 3.pagamento 4.extrato 5.encerrar")

    #Ler a escolha do usuario
    escolha_menu = int(input()) #Lê a escolha do usuario

    #se usuario escolher cadastro
    if escolha_menu == 1:
        usuario = input("Crie um nome de usuario: ")
        senha = input("Crie um senha: ")
    elif escolha_menu == 2: #se o usuario escolher login
        #comparar as inf. cadastradas com uma leitura
        login_usuario = input("Digite seu usuário: ")
        login_senha = input("Digite sua senha: ")
        if login_usuario == usuario and login_senha == senha:
            print("Login realizado com sucesso")
            #se login correto entra no menu principal
            print ("Bem vindo",usuario)
            while True: #enquanto que exibira o menu princiapl
                print("1.deposito 2.sacar 3.extrato 4.encerrar")
                escolha_principal = int(input())
                if escolha_principal == 1: #se o usuario escolher depositar
                    #Le o valor a ser depositado
                    valor_deposito = float(input())
                    saldo = saldo + valor_deposito #Atualiza o valor
                    print("Novo saldo é", saldo)
                elif escolha_principal == 2: #saque
                    valor_saque = float(input("Digite o valor do saque: "))
                    saque_saque = input ("digite sua senha: ")
                    if saque_saque == senha: #se senha correta
                        saldo = saldo - valor_saque
                    else:
                        print("senha incorreta")
                elif escolha_principal == 3: #se o usuario escolher pagar
                    valor_pix = float(input("Digite o valor do pix: "))
                    senha_pix = input("digite sua senha: ")
                    if senha_pix == senha:
                        saldo = saldo - valor_pix
                    else:
                        print ("senha incorreta")
                elif escolha_principal == 4: #visualizar o saldo
                    senha_extrato = input("digite sua senha: ")
                    if senha_pix == senha:
                        print ("Extrato: ",saldo)
                    else:
                        print ("senha incorreta")
                elif escolha_principal == 5: #encerrar
                    senha_encerrar = input("digite sua senha: ")
                    if senha_encerrar == senha:
                        break
                    else:
                        print ("senha incorreta")
        else:
            print("Usuario ou senha incorretos")