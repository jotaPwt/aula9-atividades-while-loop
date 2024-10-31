# ATIVIDADE 1

# Crie um sistema de banco, com as seguintes operações:

# ** Utilize While ou loop **

# # SISTEMA De banco

# - Acesso a conta

lista_acesso = []

cad_acesso = input('Cadastere seu acesso no banco: ')
print('Cadatro concluido')

lista_acesso.append(cad_acesso)

for i in range(3, -1, -1):
    acesso = input('Digite seu acesso: ')
    if acesso == cad_acesso:
        print('Bem vindo a sua conta')  
        saldo = 1000
        print('======================')
        print(f'Seu saldo atual é {saldo}')
    # - Fazer um deposito
        print('======================')
        print('Qual ação voce gostaria de realizar:')

        print('''
        id 0 = fazer um saque: 
        id 1 = fazer um depósito
        ''')

        acao = int(input('Digite o ID da ação desejada: '))

        if acao == 0:
            saque = int(input('insira o valor que voce gostaria sacar >>'))
            if saque > saldo:
                print('Voce nao tem todo esse dinheiro')
                pass
            elif saque <= saldo:
                print('Saque concluido')
                break
            elif saque == 0:
                print('nao é possivel sacar 0 reais')
            else:
                print('Ação indisponivel')

        elif acao == 1:
            dep = int(input('insira o valor que voce gostaria de depositar >>'))
            print('Depósito concluido com sucesso')
            
            break
        
        

    else:
        print(f'esse não é seu acesso. você tem {i} chances')
        if i > 4:
            print('Acesso Bloqueado')
            break


print('''
    id 0 - sim
    id 1 - não, ver extrato
''')

sair = input('Você gostaria de sair do sistema?')


if sair == 0:
    print('Saiu')
else:
        print('Extrato')
        if acao == 1:
            print(f'Voce depositou {dep} reais')
        if acao == 0:
            print(f'Voce sacou {saque} reais')
# - Ver extrato
    
enter = input('Digite enter para sair: ')

# - Fazer um saque 
# - Sair do sistema 



# ...........................................................

# ATIVIDADE 2

# CRIE A TABUADA COM O LOOP WHILE
# ESCOLHA UM NÚMERO E FAÇA O CALCULO DA MULTIPLICAÇÃO COM 
# TODOS OS NÚMEROS


# --------------------------ATIVIDADE 2-----------------------------

# n = int(input('Digite o numero da sua tabuda, COM FOR'))

# for i in range(1,11):
#     res = n * i
#     print(f'{n} X {i} = {res}')


# n = int(input('Digite o numero da sua tabuda, COM WHILE'))

# contador = 0

# while contador < 10:
#     contador = contador + 1
#     resultado = n * contador
#     print(f'{n} X {contador} = {resultado}')
    