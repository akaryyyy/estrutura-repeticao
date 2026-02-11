notas = [5, 6, 7, 8, 9]

aprovados = 0
acompanhamento = 0


for nota in notas:
    if nota >= 7:
     print(f"Nota {nota} - Funcionário aprovado!")
     aprovados += 1
    else:
     print(f"Nota {nota} - Funcionário em acompanhamento")
     acompanhamento += 1

print("\nResumo final:")
print(f"Aprovados: {aprovados}")
print(f"Em acompanhamento: {acompanhamento}")


