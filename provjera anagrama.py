from collections import Counter

rijec1 = str(input("Prva riječ: "))
rijec2 = str(input("Druga riječ: "))

if(Counter(rijec1) == Counter(rijec2)):
    print("Anagram")
else:
    print("Not Anagram")
