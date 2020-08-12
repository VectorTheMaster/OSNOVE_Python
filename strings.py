s = "Ovo je string"
s[0]  # označava poziciju u stringu, u ovom slučaju 0 je prva pozicija odnosno O

a = str(input("Riječ: "))

print(a.upper())  # pretvara sva slova u velika tiskana
print(a.lower())  # pretvara sva slova u mala tiskana


"1 2 3 4 6".replace("6", "5")  # zamjenjuje određeni dio stringa drugime
# zamjenjuje određeni dio i to točno prvih n puta
"Mississipi".replace("ss", "z", 2)


recenica = "Primjer za splitting string"
rijeci = recenica.split()  # odvaja rijeci zasebno u listu
rijeci1 = recenica.split("s")  # odvaja rijeci prije pojave znaka "s"
# odvajanje izvrsava samo jednom (u ovom slučaju)
rijeci2 = recenica.split(maxsplit=1)
print(rijeci)
print(rijeci1)
print(rijeci2)

b = " "  # razmak kao graničnik
# razmak se umeće između svakog znaka te se oni spajaju u jedan
print(b.join(rijeci))


rijec = "Proba"
print(rijec * 3)  # ispisati ce rijec 3 puta spojeno

print("Rijec Proba unatrag izgleda ovako:",
      rijec[::-1])  # ispisuje rijec unatrag
