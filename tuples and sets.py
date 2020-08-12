t = ("Karlo", 17, "Krk")      #Tuple je sličan listi samo što se ne mogu uređivati znakovi u njemu, ne može se ništa dodavati, izbacivati...

s = {1,2,3,4,5}     #sets je također sličan listi, razlika je u tome što set ne može imati više istih znakova (korisno je nekad listu pretvoriti u set kako bi se izbacili isti znakovi)
print (s)      

s1 = {1,1,2,3,2,5,1}    #primjer seta koji ima više istih znakova
print (s1)  #duplikati se neće ispisati

l = [1,2,3,3,4,4,4,5,"abc","abc"] #lista koja ima više istih znakova
a = set(l)      #lista se mijenja u set što znači da se izbacuju duplikati
b = list(a)     #set se mijenja u listu zbog lakšeg daljnjeg oblikovanja 
print (b)
