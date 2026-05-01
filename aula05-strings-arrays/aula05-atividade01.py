nomes = ["Ana", "Maria", "Vini", "Mat"]

for i in range(len(nomes)):
    for j in range(i+1, len(nomes)):
        print(nomes[i], nomes[j])