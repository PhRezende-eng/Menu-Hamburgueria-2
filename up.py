#coding: utf-8

from os import system 
from time import sleep

opcaoMenu = 0

valorTotal = 0

def opcao1(valorTotal):
    opcaoHamburger = 0
    print('Aguarde. . .')
    sleep(2)
    system('cls')
    while opcaoHamburger != 4:
        print('''========= Hamburgers =========\n
    ( 1 )  R$ 10,00 - X-Bacon
    ( 2 )  R$ 14,90 - X-Bacon Duplo
    ( 3 )  R$ 19,90 - X-Picanha
    ( 4 )  Voltar ao Menu\n''')

        opcaoHamburger = int(input('>>>>>>>>>> Digite uma opção: '))

        if opcaoHamburger == 1:
            valorTotal += 10
            print('X-Bacon adicionado ao carrinho com sucesso!')
            sleep(2)
            system('cls')
        
        elif opcaoHamburger == 2:
            valorTotal += 14.90
            print('X-Bacon Duplo adicionado ao carrinho com sucesso!')
            sleep(2)
            system('cls')
        
        elif opcaoHamburger == 3:
            valorTotal += 19.90
            print('X-Picanha adicionado ao carrinho com sucesso!')
            sleep(2)
            system('cls')
        
        elif opcaoHamburger == 4:
            print('Voltando. . .')
            sleep(2)
            system('cls')
        
        else:
            print('Opção inválida. Digite novamente.')
            sleep(2)
            system('cls')
    return(valorTotal)
            

def opcao2(valorTotal):
    opcaoBebidas = 0
    print('Aguarde. . .')
    sleep(2)
    system('cls')
    while opcaoBebidas != 3:
        print('''========= Bebidas =========\n
    ( 1 )  R$ 5,90 - Coca-Cola
    ( 2 )  R$ 7,90 - Suco De Laranja
    ( 3 )  Voltar ao Menu\n''')
    
        opcaoBebidas = int(input('>>>>>>>>>> Digite uma opção: '))

        if opcaoBebidas == 1:
            valorTotal += 5.90
            print('Coca-Cola  adicionado ao carrinho com sucesso!')
            sleep(2)
            system('cls')

        elif opcaoBebidas == 2:
            valorTotal += 7.90
            print('Suco de Laranja adicionado ao carrinho com sucesso!')
            sleep(2)
            system('cls')

        elif opcaoBebidas == 3:
            print('Voltando. . .')
            sleep(2)
            system('cls')

        else:
            print('Opção inválida. Digite novamente.')
            sleep(2)
            system('cls')
    return (valorTotal)



while opcaoMenu != 4:
    system('cls')
    print('''========= Menu =========\n
    ( 1 )  Hamburgers
    ( 2 )  Bebidas
    ( 3 )  Valor da Conta
    ( 4 )  Fechar Pedido\n''')

    opcaoMenu = int(input('>>>>>>>>>> Digite uma opção: '))

    if opcaoMenu == 1:
        valorTotal = opcao1(valorTotal)
    
    elif opcaoMenu == 2:
        valorTotal = opcao2(valorTotal)

    elif opcaoMenu == 3:
        print('O Valor da sua Conta é: R$ {}'.format(round(valorTotal,2)))
        sleep(2)
        system('cls')
    
    elif opcaoMenu == 4:
        print('Pedido Fechado.')
        print('O Valor da sua Conta é: R$ {}'.format(round(valorTotal,2)))
        print('Obrigado pela escolha!')
        sleep(2)
        system('cls')
        system("pause")
             
    else:
        print('Opção inválida. Digite Novamente.')
        sleep(2)
        system('cls')
