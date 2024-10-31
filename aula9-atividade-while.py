# ** Utilize While ou loop **

# # SISTEMA de Mercado: 

# - Dicionarios 
# - Conteúdo dicionário
# - Fazer compra
# - Verificar e pagar  


print('======== Bem Vindo ao Mercado =========')

produtos = {
    'arroz ': 10,
    'feijao ': 7,
    'cereal ': 15
}



str_produtos = []
int_produtos = []

for x, y in produtos.items():
    str_produtos.append(x)
    int_produtos.append(y)
    print(x,y)



carrinho = []
valores = []
# escolha = int(input('Digite o numero do ID correspondente a sua escolha de produto: '))

for n in range(1,3):
    print('''
        1 - arroz 
        2 - feijao 
        3 - cereal
    ''')
    escolha = int(input('Digite o numero do ID correspondente a sua escolha de produto: '))
    if escolha == 1:
        print(f'{str_produtos[0]} foi adicionado ao carrinho')
        carrinho = str_produtos[0]

        print(f'''
            ALGO MAIS?
                
            (1) - SIM
            (2) - NÃO
                
            Seu carrinho: {carrinho("arroz")}
        ''')

        algo_mais = int(input('Digite um numero correspondente a ação que deseja: '))

        if algo_mais == 1:
            next
        elif algo_mais == 2:
            break
    elif escolha == 2:
        print(f'{str_produtos[1]} foi adicionado ao carrinho')
        carrinho = str_produtos[1]
        print(f'''
            ALGO MAIS?
                
            (1) - SIM
            (2) - NÃO
                
            Seu carrinho: {carrinho}
        ''')

        algo_mais = int(input('Digite um numero correspondente a ação que deseja: '))

        if algo_mais == 1:
            next
        elif algo_mais == 2:
            break
    elif escolha == 3:
        print(f'{str_produtos[2]} foi adicionado ao carrinho')
        carrinho = str_produtos[2]
        print(f'''
            ALGO MAIS?
                
            (1) - SIM
            (2) - NÃO
                
            Seu carrinho: {carrinho}
        ''')

        algo_mais = int(input('Digite um numero correspondente a ação que deseja: '))

        if algo_mais == 1:
            next
        elif algo_mais == 2:
            break


    # else:
    #     print('Digite um numero produto valido')