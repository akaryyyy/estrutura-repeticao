'''
Tipo de dado - Python 

Int = Numero inteiro
Float = Numeros quebrados(flutuantes)
String = Texto
Boolean = True or False


List = Lista
Uma coleção de valores que podemos guardar juntos em uma unica variavel
'''

numerosMegaSena = [10, 29, 30, 40, 50]
mochila = ["Caderno", "Garrafa", "Pen Drive", 15000, "Estojo", "Guarda Chuva"]

compras = ["Abacaxi", "Uva", "Goiaba", "Chocolate"]

print(compras[3])
print(compras[0])

item = input("Qual item?")

compras.append("Suco")
compras.append("Refrigerante")

compras.remove("Abacaxi")

print(len(compras))

print(compras)

'''
1. Cada item da lista ocupa uma posição
2. Cada posição tem um número (índice)
3. Identifica o item pela posição

// 4 Itens 
// 0: Abacaxi
// 1: Uva
// 2: Goiaba
// 3: Chocolate

compras = ["Abacaxi", "Uva", "Goiaba", "Chocolate"]

'''

