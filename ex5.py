carros = ['monza','fusca','jipe','corsa','calhambeque','punto','marea']
print(carros)
verificar = input("Qual item deseja verificar? ")
if verificar in carros:
    print("Sim, está na lista!")
else:
    print("Não está na lista")