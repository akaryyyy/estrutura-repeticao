#nome_alunos = ["Antonio", "Hidalguinho", "Fefe", "Uilian", "Eztefania", "Luzkinha", "Rapaizinho de rosa", "Didi", "Leandrin do Gr@u", "Lele"]

#for aluno in nome_alunos:
    #print(aluno)


veículos = ["Fusca", "Doublo", "Uno", "Monza", "Corolla", "Gol", "HB20"]

# Outros carros: Nome do carro + carro legal
# Gol, Uno e Monza: Nome do carro + carros classicos

for veiculo in veículos:
    if veiculo in ("Gol", "Uno", "Monza"):
        print(f"{veiculo}, carro classico!")
    else:
        print(f"{veiculo}, carro legal!")    