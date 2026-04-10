print("Bem Vindo! Por favor, insira as próximas informações ")

peso_user = float(input("Digite o seu Peso em kg: "))
altura_user = float(input("Digite sua altura em metros: "))

while True:
      print('-----------MENU-----------'
            '\n 1: Calcule meu IMC'
            '\n 2: Calcule minha meta de hidratação diária'
            '\n 3: Estime meu gasto calórico de atividade física'
            '\n 4: Exiba minha meta diária de exercícios'
            '\n 5: Meu resumo diário')

      seletor = input("Escreva o número da opção que deseja acessar: ")

      if seletor == "1":
            imc = peso_user / (altura_user**2)
            print(f"Seu IMC é igual a: ")

