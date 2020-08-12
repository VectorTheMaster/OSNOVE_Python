broj = int(input("Unesi broj: "))
print("Djelitelji broja", broj, "su:")
for i in range(1, broj+1):
    if broj % i == 0:
        print(i)
