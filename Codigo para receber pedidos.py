print('Bem-vindo a Lanchonete da Isabel Ribeiro Barbosa')
print('******************Cardápio******************')
print('| Código |        Descrição        | Valor |')
print('|   100  |     Cachorro-Quente     |  9,00 |')
print('|   101  |  Cachorro-Quente Duplo  | 11,00 |')
print('|   102  |          X-Egg          | 12,00 |')
print('|   103  |         X-Salada        | 13,00 |')
print('|   104  |         X-Bacon         | 14,00 |')
print('|   105  |         X-Tudo          | 17,00 |')
print('|   200  |    Refrigerante Lata    |  5,00 |')
print('|   201  |       Chá Gelado        |  4,00 |')
print('')

valor_total = 0
while True:
    # Escolha do produto
    produto = int(input('Digite o código do que você deseja: '))
    # Valores digitados que nao estão no cardápio
    if (produto != 100 and produto != 101 and produto != 102 and produto != 103 and produto != 104 and produto != 105 and produto != 200 and produto != 201):
        print('Operação inválida!')
        print('')
        continue
    # Atribuição do código ao nome do produto e seu respectivo valor
    else:
        if (produto == 100):
            produto = 'Cachorro-Quente'
            valor = 9
        elif (produto == 101):
            produto = 'Cachorro-Quente Duplo'
            valor = 11
        elif (produto == 102):
            produto = 'X-Egg'
            valor = 1
        elif (produto == 103):
            produto = 'X-Salada'
            valor = 13
        elif (produto == 104):
            produto = 'X-Bacon'
            valor = 14
        elif (produto == 105):
            produto = 'X-Tudo'
            valor = 17
        elif (produto == 200):
            produto = 'Refrigerante Lata'
            valor = 5
        else:
            produto = 'Chá Gelado'
            valor = 4
        print('Você pediu um {} no valor de {:.2f} reais'.format(produto, valor))
        # Variável para somar os valores dos produtos escolhidos
        valor_total += valor
    print('')
    print('Você deseja pedir mais alguma coisa? ')
    print('1 - Sim')
    print('0 - Não')
    # Variável para escolher se vai continuar pedindo ou encerrar
    outro_pedido = int(input('>> '))
    # Encerrando pedido e imprimindo o valor a ser pago pelo cliente
    if (outro_pedido == 0):
        print('Pedido encerrado')
        print('O total a ser pago é {:.2f} reais'.format(valor_total))
        break
    # Opção para o cliente que deseja continuar pedindo
    else:
        continue
