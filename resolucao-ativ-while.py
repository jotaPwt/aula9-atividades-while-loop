# dicionario de produtos 

d = {

'arroz':20,
'feijão':10,
'tempero':10

}

# loop for para extrair os dados e transformar em lista

lista1_keys  =  []
lista2_values  =  []
for n,x in d.items():
    lista1_keys.append(n)
    lista2_values.append(x)
    print(lista1_keys, lista2_values)


# meu carrinho e valor
carrinho = []
meus_valores = []



pergunta = input('Fazer pedido? s/n>>')
while  pergunta != 'n':
    escolha  =  int(input('escolha 0, 1, 2:'))
    carrinho.append(lista1_keys[escolha])
    print(carrinho)
    pergunta  = input('Deseja continuar? s/n')
    meus_valores.append(lista2_values[escolha])
           
            
else:
    print('Obrigada volte sempre!!')
    soma =  sum(meus_valores)  
    print('Total a pagar: R$ ', soma) 
          