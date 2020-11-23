matrica = []

for i in range(3):  # način unosa elemenata u matricu
    redak = list(map(int, input("Unesi 5 brojeva: ").split()))
    matrica.append(redak)

for i in range(3):  # način ispisivanja matrica
    for j in range(5):
        print(matrica[i][j], end=" ")
    print()  # novi redak

for redak in matrica: #još jedan način raspisivanja matrice (najlakši)
    print(*redak)   #ako maknemo oznaku * ispisat će se matrica sa zagradama, zarezima i sl.

