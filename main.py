print("Bem Vindo! Por favor, insira as próximas informações ")
while True:
      peso_user = float(input("Digite o seu Peso em kg: "))
      if peso_user <= 0:
            print("Peso inválido, Digite Novamente")
      else:

            altura_user = float(input("Digite sua altura em metros: "))
            if altura_user <= 0:
                  print("Altura Inválida, Digite novamente")

            else:


                  # Inicializados aqui para o resumo (opcao 5) funcionar
                  # mesmo antes de o usuario calcular cada item
                  imc = None
                  hidratacao_diaria = None
                  calorias_gastas = 0
                  meta = None

                  while True:
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
                              print(f"Seu IMC é igual a: {round(imc, 2)}")

                              if imc < 18.5:
                                    print("\nAbaixo do peso")
                              elif imc < 25:
                                    print("\nPeso normal")
                              elif imc < 30:
                                    print("\nSobrepeso")
                              else:
                                    print("\nObesidade")

                              voltar = input("\nDeseja voltar ao menu? (digite s ou n): ")
                              if voltar != "s":
                                    print("\nPrograma Encerrado")
                                    break

                        elif seletor == "2":
                              print('\n-----------CALCULO DE META DE HIDRATAÇÃO DIÁRIA-----------\n')
                              hidratacao_diaria = peso_user * 0.035
                              print(f"A quantidade de agua ideal que você deve ingerir é de: {round(hidratacao_diaria, 2)}")

                              voltar = input("\nDeseja voltar ao menu? (digite s ou n): ")
                              if voltar != "s":
                                    print("\nPrograma Encerrado")
                                    break

                        elif seletor == "3":
                              print('\n-----------CALCULO DE GASTO CALÓRICO POR ATIVIDADE FÍSICA-----------\n'
                                    '\n 1: Caminhada'
                                    '\n 2: Corrida'
                                    '\n 3: Musculação'
                                    '\n 4: Ciclismo')

                              atividade = input("\nDigite o número da atividade que deseja calcular: ")

                              ## MET significa Equivalente Metabólico da Tarefa (do inglês Metabolic Equivalent of Task),
                              #  é uma unidade de medida que quantifica o gasto energético de atividades físicas

                              if atividade == "1":
                                    met = 3.5
                              elif atividade == "2":
                                    met = 8.0
                              elif atividade == "3":
                                    met = 6.0
                              elif atividade == "4":
                                    met = 7.5
                              else:
                                    print("Atividade inválida!")
                                    continue

                              tempo = float(input("\nQuanto tempo (em minutos) de exercícios?: "))

                              tempo_horas = tempo / 60
                              calorias_gastas = met * peso_user * tempo_horas

                              print(f"\nA sua quantidade de calorias gastas foi de: {round(calorias_gastas, 2)}")

                              voltar = input("\nDeseja voltar ao menu? (digite s ou n): ")
                              if voltar != "s":
                                    print("\nPrograma Encerrado")
                                    break

                        elif seletor == "4":
                              print("\n-----------META DIÁRIA DE EXERCÍCIOS-----------\n"
                                    '\n Qual é o seu objetivo?'
                                    '\n 1: Emagrecer'
                                    '\n 2: Manter Peso'
                                    '\n 3: Ganhar Massa')

                              objetivo = input("\nDigite o número do seu objetivo: ")

                              if objetivo == "1":
                                    meta = "\n45 a 60 minutos por dia"
                              elif objetivo == "2":
                                    meta = "\n30 a 45 minutos por dia"
                              elif objetivo == "3":
                                    meta = "\n60 a 90 minutos por dia"
                              else:
                                    print("\nOpção inválida!")
                                    continue

                              print(f"\nSua meta diária de exercícios é: {meta}")

                              voltar = input("\nDeseja voltar ao menu? (digite s ou n): ")
                              if voltar != "s":
                                    print("\nPrograma Encerrado")
                                    break

                        elif seletor == "5":
                              print("\n-----------MEU RESUMO DIÁRIO-----------\n")

                              if imc:
                                    print(f"\nIMC: {round(imc, 2)}")
                              else:
                                    print("\nIMC: não calculado")

                              if calorias_gastas > 0:
                                    print(f"\nCalorias gastas: {round(calorias_gastas, 2)} kcal")
                              else:
                                    print("\nCalorias gastas: nenhuma atividade registrada")

                              if meta:
                                    print(f"\nMeta de exercícios: {meta}")
                              else:
                                    print("\nMeta de exercícios: não definida")

                              if hidratacao_diaria:
                                    print(f"\nMeta de hidratação: {hidratacao_diaria} litros/dia")
                              else:
                                    print("\nMeta de hidratação: não calculada")

                              voltar = input("\nDeseja voltar ao menu? (digite s ou n): ")
                              if voltar != "s":
                                    print("\nPrograma Encerrado")
                                    break


            break