import re

text = "Ovo je proba"

a = re.compile("proba")
b = a.search(text)
print(b)


# trazi u varijabli text znakove O, j i P (ispisuje samo prvi koji se pojavljuje)
a1 = re.compile("[jOP]")
b = a1.search(text)
print(b)
