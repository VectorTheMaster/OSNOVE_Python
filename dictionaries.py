sport = {"nogomet": 1,
    "atletika": 3,
    "kosarka": 5,
    "rukomet": 2
}      

print (sport.get("nogomet"))    #nogomet je povezan sa brojem 1 sto znaci da ce ispisati taj broj
print (sport.get("plivanje"))       #plivanje nije dio sporta te ce ispisati nista ("None")

sport["golf"] = 3      #stvara novu varijablu golf te mu pridružuje vrijednost 3
print (sport)

#dict.items()       ispisuje sve članove dictionaria
print (sport.items())

#dict.keys()
print (sport.keys())

#dict.values()
print(sport.values())

#dict.pop()
sport.pop("golf")
print(sport)

#dict.popitem()   izbacuje zadnji član i njegovu vrijednost
print(sport.popitem())  #ispisuje člana koji je izbacio
sport.popitem()     #izbacili smo posljednjeg člana ("kosarka")
print (sport)

#dict.clear()  čisti cijeli dictionari



