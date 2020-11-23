zaokruzeni_broj = round(2.56)  # zakružuje broj (u ovom slučaju na veći)
print(zaokruzeni_broj)

broj = 4.35235235235
print("%.2f" % broj)  # zaokruzuje broj na određeni broj znamenki
# drugi nacin zaokruzivanja broja na određeni broj znamenki
print("{:.3f}".format(broj))
print(round(broj, 5))  # treci nacin zaokruzivanja broja na određeni broj znamenki
