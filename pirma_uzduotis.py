"""Pirma užduotis

Sukurti funkciją, kuri iš vardų sąrašo sudarytų sąrašą tik iš vardų pirmų raidžių ir tą sąrašą grąžintų:
Pvz: paduodamas sąrašas į funkciją: [‘Jonas’, ‘Petras’, ‘Linas’], tai grąžinamas turėtų būti [‘J’, ‘P’, ‘L’]
Paduoti vardų sąrašą į funkciją (vardus galite sugalvoti patys) ir atspausdinti funkcijos rezultatą

"""

def funkcija():

    vardai = input("Iveskite 3 vardus")
    newlist = [x[0].upper() for x in vardai.split()]
    return newlist

print(funkcija())
