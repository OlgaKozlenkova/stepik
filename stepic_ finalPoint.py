napr = {"север": (0, 1), "запад": (-1, 0), "юг": (0, -1), "восток": (1, 0)}
n = int(input("Vvedite chislo n: "))
x_list = [(input("napravlenie i sm. cherez probel: ")).split(" ") for x in range(n)]
dvizh = [(napr[x][0] * int(y), napr[x][1] * int(y)) for x, y in x_list]
res = (sum([x for x, y in dvizh]), sum([y for x, y in dvizh]))
print(" ".join(map(str, res)))

