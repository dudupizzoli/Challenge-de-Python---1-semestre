contasbancarias = []
missoes = ["Missão 1: Faça 15 posts - Recompensa: 300 pontos.", "Missão 2: Entre em 3 comunidades - Recompensa: 150 pontos.", "Missão 3: Poste 5 fotos em diferentes linhas do metrô de São Paulo - Recompensa: Uma pelúcia do metrô de São Paulo."]

def conversao (a):
    valor_convertido = a * 0.009
    return valor_convertido

def validacao (pontos, pontos_atuais, limite):
    if pontos > pontos_atuais:
        print("Não foi possível prosseguir pois você inseriu um valor maior do que possui.")
        return False
    elif pontos > limite:
        print("Não foi possível prosseguir pois você inseriu um valor maior do que o seu limite.")
        return False
    elif pontos <= 0:
        print("Não é possível converter 0 ou menos pontos")
        return False
    else:
        return True

login = False
username_cad = "Usuario_teste"
senha_cad = "senha_usuario"

while login == False:
    print("\n===== Login do Usuário =====")
    username = input("Insira seu nome de usuário: ")
    senha = input("Insira sua senha: ")

    if username == username_cad and senha == senha_cad:
        login = True
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")

transferir_bu = 0
creditos_bu = 0
current_pontos = 9000
limite_pontos_resgate = 8000
opcao = -1
resgate = 0
saldo_atual = 0

while opcao != 0:
    print("\n===== MENU =====")
    print("1 - Cadastrar conta bancária.")
    print("2 - Conferir contas bancárias cadastradas.")
    print("3 - Remover conta bancária cadastrada.")
    print("4 - Conferir missões.")
    print("5 - Ver quantidade de pontos.")
    print("6 - Simular conversão de pontos.")
    print("7 - Converter pontos em dinheiro.")
    print("8 - Resgatar dinheiro.")
    print("9 - Conferir saldo.")
    print("10 - Converter pontos em créditos do bilhete único.")
    print("11 - Transferir os créditos para o bilhete único.")
    print("12 - Conferir a quantidade de créditos do bilhete único.")
    print("13 - Conferir limite de pontos resgatados.")
    print("0 - Sair.")

    opcao = int(input("Escolha uma opção: "))

    match opcao:

        case 1:
            user_conta_banc = input("Digite o nome de usuário de sua conta bancária: ")
            senha_conta_banc = input("Digite a senha da conta: ")
            conta_banc ={"user_conta_banc": user_conta_banc, "senha_conta_banc": senha_conta_banc}
            contasbancarias.append(conta_banc)
            print("Conta cadastrada com sucesso!")
        
        case 2:
            if len(contasbancarias) == 0:
                print("Nenhuma conta bancária cadastrada.")
            else: 
                for a in contasbancarias:
                    print("Usuário: ", a["user_conta_banc"])
            
        case 3:
            user_conta_banc = input("Nome de usuário da conta a ser removida: ")
            senha_conta_banc = input("Senha da conta a ser removida: ")
            encontrado = False

            for a in contasbancarias:
               if a["user_conta_banc"] == user_conta_banc and a["senha_conta_banc"] == senha_conta_banc:
                   confirm = int(input("Você realmente deseja remover a conta? Digite '1' para sim e '2' para não."))
                   if confirm == 1:
                    contasbancarias.remove(a)
                    encontrado = True
                    print("Conta removida.")
                    break
                   else:
                       print("Conta não removida.")
                       encontrado = True
                       break
            
            if not encontrado:
               print("Conta não encontrada.")

        case 4:
            if len(missoes) == 0:
                print("Nenhuma missão disponível.")
            else: 
                for missao in missoes:
                    print(missao)

        case 5:
            print("Você possui um total de ", current_pontos, "pontos.")
        
        case 6:
            pontos_simulacao = int(input("Insira a quantidade de pontos para fazer a simulação de uma conversão: "))
            simu_pont = conversao(pontos_simulacao)
            print(f"{pontos_simulacao} pontos são iguais a R$ {simu_pont:.2f}.")

        case 7:
            pontos_convert = int(input("Insira a quantidade de pontos que você deseja converter em dinheiro: "))

            if validacao(pontos_convert, current_pontos, limite_pontos_resgate):            
                current_pontos -= pontos_convert
                limite_pontos_resgate -= pontos_convert
                conv_pontos_din = conversao(pontos_convert)
                resgate += conv_pontos_din
                print(f"Você converteu {pontos_convert} em R$ {conv_pontos_din:.2f} com sucesso!")
            

        case 8: 
            if resgate == 0:
                print("Você não converteu pontos em dinheiro, por isso não foi possível realizar o resgate.")
            else:
                saldo_atual += resgate
                print(f"Parabéns, você resgatou R$ {resgate}.")
                resgate = 0

        case 9:
            print(f"Atualmente seu saldo é de R$ {saldo_atual}.")
        
        case 10:
            pontos_convert_bu = int(input("Insira a quantidade de pontos que você deseja converter em créditos para o bilhete único: "))

            if validacao(pontos_convert_bu, current_pontos, limite_pontos_resgate):
                current_pontos -= pontos_convert_bu
                limite_pontos_resgate -= pontos_convert_bu
                conv_pontos_bu = conversao(pontos_convert_bu)
                transferir_bu += conv_pontos_bu
                print(f"Você converteu {pontos_convert_bu} em R$ {conv_pontos_bu:.2f} para o bilhete único com sucesso!")

        case 11: 
            if transferir_bu == 0:
                print("Você não converteu pontos em créditos, por isso não foi possível realizar a transferência.")
            else:
                creditos_bu += transferir_bu
                print(f"Parabéns, você resgatou R$ {transferir_bu:.2f}.")
                transferir_bu = 0

        case 12:
            print(f"Atualmente você possui R$ {creditos_bu:.2f} no bilhete único.")

        case 13:
            print(f"Seu limite atual é de {limite_pontos_resgate} pontos.")

        case 0:
            print("Encerrando sistema...")
            break
            
