print("\nBem Vindo! Por favor, insira as próximas informações ")

peso_valido = False
while peso_valido == False:
    peso_user = float(input("\nDigite o seu peso em kg: "))
    if peso_user > 0:
        peso_valido = True
    else:
        print("\nPeso inválido, Digite Novamente")

altura_valida = False
while altura_valida == False:
    altura_user = float(input("\nDigite sua altura em metros: "))
    if altura_user > 0:
        altura_valida = True
    else:
        print("\nAltura inválida, Digite novamente")

imc_calculado = False
hidratacao_calculada = False
calorias_calculadas = False
meta_definida = False

executar = True

while executar == True:
    print('\n-----------MENU-----------'
          '\n 1: Calcule meu IMC'
          '\n 2: Calcule minha meta de hidratação diária'
          '\n 3: Estime meu gasto calórico de atividade física'
          '\n 4: Exiba minha meta diária de exercícios'
          '\n 5: Meu resumo diário')

    seletor = input("\nDigite o número da opção que deseja acessar: ")

    if seletor == "1":
        print('\n-----------CALCULO DE IMC-----------\n')
        imc = peso_user / (altura_user**2)
        print(f"Seu IMC: {round(imc, 2)}")
        imc_calculado = True

        if imc < 18.5:
            print("\nAbaixo do peso")
        elif imc < 25:
            print("\nPeso normal")
        elif imc < 30:
            print("\nSobrepeso")
        else:
            print("\nObesidade")

    elif seletor == "2":
        print('\n-----------CALCULO DE META DE HIDRATAÇÃO DIÁRIA-----------\n')
        hidratacao_diaria = peso_user * 0.035
        print(f"Sua meta de hidratação diária é de: {round(hidratacao_diaria, 2)} L")
        hidratacao_calculada = True

    elif seletor == "3":
        print('\n-----------CALCULO DE GASTO CALÓRICO POR ATIVIDADE FÍSICA-----------\n'
              '\n1:Caminhada '
              '\n2:Corrida '
              '\n3:Musculação '
              '\n4:Ciclismo')

        atividade = input("\nDigite o número da atividade que deseja calcular: ")

        met_valido = False

        if atividade == "1":
            met = 3.5
            met_valido = True
        elif atividade == "2":
            met = 8.0
            met_valido = True
        elif atividade == "3":
            met = 6.0
            met_valido = True
        elif atividade == "4":
            met = 7.5
            met_valido = True
        else:
            print("Atividade inválida!")

        if met_valido == True:
            tempo = float(input("\nQuanto tempo (em minutos) de exercícios?: "))
            calorias_gastas = met * peso_user * (tempo / 60)
            print(f"\nA sua quantidade de calorias gastas foi de: {round(calorias_gastas, 2)}")
            calorias_calculadas = True

    elif seletor == "4":
        print("\n-----------META DIÁRIA DE EXERCÍCIOS-----------\n"
              '\n Qual é o seu objetivo?'
              '\n 1: Emagrecer'
              '\n 2: Manter Peso'
              '\n 3: Ganhar Massa')

        objetivo = input("\nDigite o número do seu objetivo: ")

        if objetivo == "1":
            meta_diaria = "45-60 min"
            meta_definida = True
        elif objetivo == "2":
            meta_diaria = "30-45 min"
            meta_definida = True
        elif objetivo == "3":
            meta_diaria = "60-90 min"
            meta_definida = True
        else:
            print("Opção inválida!")

        if meta_definida == True:
            print(f"\nSua meta diária de exercícios é: {meta_diaria}")

    elif seletor == "5":
        print("\n-----------MEU RESUMO DIÁRIO-----------\n")

        if imc_calculado == True:
            print(f"Seu IMC: {round(imc, 2)}")
        else:
            print("Seu IMC: não calculado")

        if calorias_calculadas == True:
            print(f"Sua quantidade de calorias gastas: {round(calorias_gastas, 2)}")
        else:
            print("Sua quantidade de calorias gastas: nenhuma")

        if meta_definida == True:
            print(f"Sua meta diária de exercícios é: {meta_diaria}")
        else:
            print("Sua meta diária de exercícios é: não definida")

        if hidratacao_calculada == True:
            print(f"Meta de hidratação diária: {round(hidratacao_diaria, 2)} L")
        else:
            print("Meta de hidratação diária: não calculada")

    else:
        print("Opção inválida!")

    voltar = input("\nDeseja continuar o programa? (s/n): ")
    if voltar != "s":
        executando = False
        print("\nPrograma encerrado")