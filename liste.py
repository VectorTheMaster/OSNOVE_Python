l = [1, 2, 3, 4, 5, 6]  # primjer jedne liste
print(l)  # printa cijelu listu
# printa određenu poziciju u listi, u ovom slučaju drugu po redu (kreće od 0)
print(l[1])
print(l[-1])  # printa određenu poziciju na listi ali unatrag (kreće od -1)
# ispisuje od drugog do četvrtog (ne ubrajajući) znaka u listi, kreće od 0
print(l[1:3])
print(l[:2])  # ispisuje do trećeg člana (ne uključujući)
print(l[0:6:2])  # ispisuje od prvog do petog člana ali sa razmakom dva


l.append(5)  # dodaje u listu l na kraj još jedan znak
print("nakon append funkcije lista izgleda ovako: ", l)

# dodaje znak na određeno mjesto, prvo u zagradi govori gdje (kreće od 0), a drugo govori što se dodaje
l.insert(3, 4)
print("Nakon insert funkcije imamo listu: ", l)

l.remove(5)  # izbacuje određeni znak iz liste
print("Nakon izbacivanja znaka lista izgleda ovako: ", l)

l.reverse()  # okreće listu tako da ono što je bilo zadnje postaje prvo i obrnuto
print("Nakon okretanja liste, lista izgleda ovako: ", l)


brojevi = [4, 5, 3, 1, 8]
print("Imamo brojeve: ", brojevi)
brojevi.sort()  # sortira brojeve u listi
print("Nakon sortiranja brojeva lista izgleda ovako :", brojevi)

# dodaje znakove liste brojevi u listu l (NE DODAJE LISTU NEGO ZNAKOVE!)
l.extend(brojevi)
print(l)

n = l.count(1)  # broji koliko puta se pojavljuje određeni znak
print(n)

x = l.index(2)  # pokazuje na kojoj poziciji u listi se nalazi određeni znak
print("Broj dva se u listi prikazuje na", x+1, "mjestu")

print(l.pop(1))  # izbacuje znak sa drugog mjesta te ga ispisuje
print(l)

print(sum(l))  # zbraja sve brojeve u listi


lista = [5, 2, 3, 6]  # lista koja sadrži pet članova
# a,b,c i d varijablama se daju vrijednosti iz liste (a je prvi član, pet, b je drugi član, dva, itd.)
a, b, c, d = lista
print(a)
