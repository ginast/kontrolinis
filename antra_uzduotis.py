"""Sukurti funkciją, kuri priimtų tuple ir grąžintų kitą tuple, tik su pašalintais dublikatais. Eiliškumas elementų turi išlikti toks pats:
Pvz: jeigu funkcija priima (1, 2, 3, 4, 3, 2, 1) tuple, tai turėtų grąžinti (1, 2, 3, 4)
Pvz: jeigu funkcija priima (‘a’, ‘d’, ‘g’, ‘h’, ‘i’, ‘q’, ‘q’, ‘h’, ‘d’) tuple, tai turėtų grąžinti (‘a’, ‘d’, ‘g’, ‘h’, ‘i’, ‘q’)
Paduoti tuple į funkciją (reikšmes sugalvokite patys) ir išspausdinti funkcijos rezultatą
"""



def funkcija(tuple):
    return list(set([i for i in tuple]))

tuple = (1, 2, 3, 4, 3, 2, 1, 8, 9, 20, 20, 27, 9)
print(funkcija(tuple))