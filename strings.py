s = "Ovo je string"
s[0] #označava poziciju u stringu, u ovom slučaju 0 je prva pozicija odnosno O

a = str(input("Riječ: "))

print (a.upper()) #pretvara sva slova u velika tiskana
print (a.lower()) #pretvara sva slova u mala tiskana


"1 2 3 4 6".replace("6", "5") #zamjenjuje određeni dio stringa drugime
"Mississipi".replace("ss", "z", 2) #zamjenjuje određeni dio i to točno prvih n puta



recenica = "Primjer za splitting string"
rijeci = recenica.split()  #odvaja rijeci zasebno u listu
rijeci1 = recenica.split("s") #odvaja rijeci prije pojave znaka "s"
rijeci2 = recenica.split(maxsplit = 1) #odvajanje izvrsava samo jednom (u ovom slučaju)
print (rijeci)
print (rijeci1)
print (rijeci2)

b = " " #razmak kao graničnik
print (b.join(rijeci)) #razmak se umeće između svakog znaka te se oni spajaju u jedan



