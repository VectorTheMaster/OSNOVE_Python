l = [1, 2 , 3] #primjer jedne liste
print (l) #printa cijelu listu
print (l[1]) #printa određenu poziciju u listi, u ovom slučaju drugu po redu (kreće od 0)
print (l[1:3]) #ispisuje od drugog do četvrtog (ne ubrajajući) znaka u listi, kreće od 0
print (l[:2]) #ispisuje do trećeg člana (ne uključujući)


l.append(5) #dodaje u listu l na kraj još jedan znak
print("nakon append funkcije lista izgleda ovako: ", l)

l.insert(3, 4) #dodaje znak na određeno mjesto, prvo u zagradi govori gdje (kreće od 0), a drugo govori što se dodaje
print ("Nakon insert funkcije imamo listu: ", l)

l.remove(5) #izbacuje određeni znak iz liste
print ("Nakon izbacivanja znaka lista izgleda ovako: ", l)

l.reverse() #okreće listu tako da ono što je bilo zadnje postaje prvo i obrnuto
print("Nakon okretanja liste, lista izgleda ovako: ", l)



brojevi = [4, 5, 3, 1, 8]
print ("Imamo brojeve: ", brojevi)
brojevi.sort() #sortira brojeve u listi
print ("Nakon sortiranja brojeva lista izgleda ovako :", brojevi)

l.extend(brojevi) #dodaje znakove liste brojevi u listu l (NE DODAJE LISTU NEGO ZNAKOVE!)
print (l)

n = l.count(1) #broji koliko puta se pojavljuje određeni znak
print (n)

x = l.index(2) #pokazuje na kojoj poziciji u listi se nalazi određeni znak
print ("Broj dva se u listi prikazuje na", x+1 ,"mjestu") 

print (l.pop(1)) #izbacuje znak sa drugog mjesta te ga ispisuje
print (l) 

print (sum(l)) #zbraja brojeve u listi
