lista = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]

maior = max(lista)
print("Maior número:", maior)

menor = min(lista)
print("Menor número:", menor)

pares = [num for num in lista if num % 2 == 0]
print("Números pares:", pares)

primeiro = lista[0]
qtde_primeiro = lista.count(primeiro)
print("Quantidade de ocorrências do primeiro elemento:", qtde_primeiro)

media = sum(lista) / len(lista)
print("Média dos números:", round(media, 2))

soma_neg = sum(num for num in lista if num < 0)
print("Soma dos números negativos:", soma_neg)
