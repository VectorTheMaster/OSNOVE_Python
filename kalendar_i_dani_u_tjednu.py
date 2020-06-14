import calendar
import datetime
import time

print (calendar.weekheader(4)) #brojka u zagradi govori koliko ce se slova ispisati od dana
print()

print (calendar.firstweekday()) #dani u tjednu su označeni brojkama, Pon = 0, Uto = 1 ... Prvi dan u tjednu kod Pythona je ponedjeljak
print() #ispisuje prazan redak

print (calendar.month(2020, 5, (3) )) #ispisuje mjesec svibanj 2020. godine, dani u tjednu pišu se s tri slova
print()

print (calendar.monthcalendar(2020, 5)) #ispisuje matricu 5. mjeseca 2020. godine
print()


print(calendar.calendar(2020)) #ispisuje sve mjesece i dane u 2020. godini
print()

dan_u_tjednu = calendar.weekday(2020, 5, 13) #ispisuje broj dana, 13.5. 2020. je srijeda odnosno 2, jer pon krece sa 0
print (dan_u_tjednu)
print ()

prijestupna = calendar.isleap(2020) #provjerava je li 2020. godina prijestupna
print (prijestupna)
print ()

