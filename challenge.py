contasbancarias = []
missoes = ["Missão 1: Faça 15 posts - Recompensa: 300 pontos.", "Missão 2: Entre em 3 comunidades - Recompensa: 150 pontos.", "Missão 3: Poste 5 fotos em diferentes linhas do metrô de São Paulo - Recompensa: Uma pelúcia do metrô de São Paulo."]

def conversao (a):
    valor_convertido = a * 0.009
    return valor_convertido

def simulacao_conversao (b):
    valor_simulado = b * 0.009
    return valor_simulado

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

current_pontos = 6000
limite_pontos_resgate = 5000
opcao = -1
resgate = 0
saldo_atual = 0

# ==================================
# PARA SER FEITO: codar as opções 10, 11 e 12. Além disso, talvez criar um jeito de escolher em qual conta depositar o resgate
# ==================================

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
    print("12 - Conferir limite de pontos resgatados.")
    print("0 - Sair.")

    opcao = int(input("Escolha uma opção: "))

    match opcao:

        case 1:
            user_conta_banc = input("Digite o nome de usuário de sua conta bancária: ")
            senha_conta_banc = input("Digite a senha da conta: ")
            conta_banc ={"Usuário": user_conta_banc, "Senha": senha_conta_banc}
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
                   contasbancarias.remove(a)
                   encontrado = True
                   print("Conta removida.")
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
            simu_pont = simulacao_conversao(pontos_simulacao)
            print(f"{pontos_simulacao} pontos são iguais a R$ {simu_pont:.2f}.")

        case 7:
            pontos_convert = int(input("Insira a quantidade de pontos que você deseja converter em dinheiro: "))

            if pontos_convert > current_pontos or pontos_convert > limite_pontos_resgate:
                print("Não foi possível prosseguir pois você inseriu um valor maior do que possui.")
            elif pontos_convert == 0:
                print("Não é possível converter 0 pontos")
            else:
                current_pontos -= pontos_convert
                limite_pontos_resgate -= pontos_convert
                conv_pontos_din = conversao(pontos_convert)
                resgate += conv_pontos_din
                print(f"Você converteu {pontos_convert} em R$ {conv_pontos_din:.2f} com sucesso!")

        case 8: 
            saldo_atual += resgate
            print(f"Parabéns, você resgatou R$ {resgate}.")

        case 9:
            print(f"Atualmente seu saldo é de R$ {saldo_atual}.")


        case 0:
            print("Encerrando sistema...")
            break
