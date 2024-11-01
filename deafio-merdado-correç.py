# # SISTEMA de Mercado: 

# - Dicionarios 
# - Conteúdo dicionário
# - Fazer compra
# - Verificar e pagar  

print('BEM VINDO AO MERCADO')

produtos = {
    'arroz':10,
    'fejaoo':7,
    'cereal': 12
}

lista1_keys = []
lista2_values = []

for x,y in produtos.items():
    lista1_keys.append(x)
    lista2_values.append(y)
    print(lista1_keys, lista2_values)


meus_valores = []
carrinho = []

deseja = input('Deseja comprar algo? s/n?')

while deseja != 'n':
    escolha = int(input('Escolha seu produto: 0, 1, 2: '))
    carrinho.append(lista1_keys[escolha])
    print(carrinho)

    deseja = input('Deseja continuar? s/n: ')
    meus_valores.append(lista2_values[escolha])

else:
    
    print(carrinho)
    soma = sum(meus_valores)
    print(f'O total da sua compra é {soma}')

    deletar = input('Você gostaria de deletar algum produto? s/n: ')
    if deletar == 's':
        escolha_del = int(input('Escolha seu produto para deletar: 0, 1, 2: '))
        del carrinho[escolha_del]
        print(carrinho)
        soma = sum(meus_valores)
        print(f'Total a pagar {soma}')
        print(carrinho)
        print('OBRIGADO, volte sempre')

    else:
        soma = sum(meus_valores)
        print(f'Total a pagar {soma}')
        print(carrinho)
        print('OBRIGADO, volte sempre')

