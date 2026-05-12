missoes = ["Missão 1: Faça 15 posts - Recompensa: 300 pontos.", "Missão 2: Entre em 3 comunidades - Recompensa: 150 pontos.", "Missão 3: Poste 5 fotos em diferentes linhas do metrô de São Paulo - Recompensa: Uma pelúcia do metrô de São Paulo."]

def conversao (a):
    valor_convertido = a * 0.0096
    return valor_convertido

def conversao_passagem (p):
    global current_pontos
    current_pontos = current_pontos - p * 580

def conversao_desconto(d):
    global current_pontos
    current_pontos = current_pontos - d * 113

def validacao_din (pontos, pontos_atuais):
    if pontos > pontos_atuais:
        print("Não foi possível prosseguir pois você inseriu um valor maior do que possui.")
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

transferir_passagens = 0
transferir_desconto = 0
desconto_bu = 0
passagens_bu = 0
current_pontos = 9000
limite_passagens = 10
opcao = -1
resgate_din = 0
saldo_bu_atual = 0

while opcao != 0:
    print("\n===== Menu SoulUp Society =====")
    print("1 - Conferir missões.")
    print("2 - Ver quantidade de pontos.")
    print("3 - Simular conversão de pontos em dinheiro.") 
    print("4 - Converter pontos em dinheiro para o bilhete único.")
    print("5 - Transferir o dinheiro para o bilhete único.")
    print("6 - Conferir a carga do bilhete único.")
    print("7 - Converter pontos em passagens do bilhete único (1 passagem = 580 pontos).")
    print("8 - Transferir as passagens para o bilhete único.")
    print("9 - Conferir a quantidade de passagens do bilhete único.")
    print("10 - Converter pontos em vales de desconto para a passagem (cada vale garante '20%' de desconto. Esta função apenas ficará disponível após atingir o limite de compra de passagens).")
    print("11 - Transferir os vales de desconto para o bilhete único.")
    print("12 - Conferir a quantidade de vales de desconto.")
    print("13 - Conferir limite de pontos transformados em passsagens.") 
    print("0 - Sair.")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida. Digite apenas números.")
        continue

    match opcao:

        case 1:
            if len(missoes) == 0:
                print("Nenhuma missão disponível.")
            else: 
                for missao in missoes:
                    print(missao)

        case 2:
            print("Você possui um total de ", current_pontos, "pontos.")
        
        case 3:
            pontos_simulacao = int(input("Insira a quantidade de pontos para fazer a simulação de uma conversão: "))
            simu_pont = conversao(pontos_simulacao)
            print(f"{pontos_simulacao} pontos são iguais a R$ {simu_pont:.2f}.")

        case 4:
            pontos_convert = int(input("Insira a quantidade de pontos que você deseja converter em dinheiro para o bilhete único: "))

            if validacao_din(pontos_convert, current_pontos):            
                current_pontos -= pontos_convert
                conv_pontos_din = conversao(pontos_convert)
                resgate_din += conv_pontos_din
                print(f"Você converteu {pontos_convert} em R$ {conv_pontos_din:.2f} com sucesso!")
            

        case 5: 
            if resgate_din == 0:
                print("Você não converteu pontos em dinheiro, por isso não foi possível realizar a transferência.")
            else:
                saldo_bu_atual += resgate_din
                print(f"Parabéns, você resgatou R$ {resgate_din:.2f}.")
                resgate = 0

        case 6:
            print(f"Atualmente o saldo de seu bilhete é de R$ {saldo_bu_atual:.2f}.")
        
        case 7:
            conv_passagens = int(input("Insira a quantidade de passagens que você deseja adquirir para o bilhete único: "))

            if conv_passagens > limite_passagens or current_pontos < (conv_passagens * 580):
                print("Não foi possível realizar a conversão. Confira seu limite ou sua quantidade de pontos.")
            else:
                limite_passagens -= conv_passagens
                conversao_passagem(conv_passagens)
                transferir_passagens += conv_passagens
                print(f"Você converteu {conv_passagens * 580} pontos em {conv_passagens} passagem(ns) para o bilhete único com sucesso!")

        case 8: 
            if transferir_passagens == 0:
                print("Você não converteu pontos em passagens, por isso não foi possível realizar a transferência.")
            else:
                passagens_bu += transferir_passagens
                print(f"Parabéns, você resgatou {transferir_passagens} passagem(ns).")
                transferir_passagens = 0

        case 9:
            print(f"Atualmente você possui {passagens_bu} passagem(ns) no bilhete único.")
            
        case 10:
            conv_desconto = int(input("Insira a quantidade de vales que você deseja adquirir: "))
            if limite_passagens != 0 or current_pontos < conv_desconto*113:
                print("Não foi possível realizar a conversão. Confira seu limite ou sua quantidade de pontos.")
            else:
                conversao_desconto(conv_desconto)
                transferir_desconto += conv_desconto
                print(f"Você converteu {conv_desconto * 113} pontos em {conv_desconto} vale(s) para o bilhete único com sucesso!")


        case 11:
            if transferir_desconto == 0:
                print("Você não converteu pontos em vales, por isso não foi possível realizar a transferência.")
            else:
                desconto_bu += transferir_desconto
                print(f"Parabéns, você resgatou {transferir_desconto} vale(s).")
                transferir_desconto = 0

        case 12:
            print(f"Atualmente você possui {desconto_bu} vale(s) no bilhete único.")        

        case 13:
            print(f"Seu limite atual é de {limite_passagens} passagens.")

        case 0:
            print("Encerrando sistema...")
            break

        case _:
            print("Opção inválida. Digite uma opção válida do menu.")
            
