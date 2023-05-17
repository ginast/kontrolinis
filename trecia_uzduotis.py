"""Trečia užduotis

Sukurti programą, kuri saugotų duomenis apie darbuotojus Pickle faile bei atliktų su duomenimis įvairius veiksmus:
Sukurti funkciją, kuri sukuria darbuotoją (vardas, amžius, darbo pozicija) ir jį grąžina
Sukurti funkciją, kuri išsaugo darbuotojus į failą (pickle)
Sukurti funkciją, kuri užkrauna darbuotojus iš failo ir juos grąžina (pickle)
Panaudoti sukūrimo funkciją kelis kartus su kokiomis norite reikšmėmis
Panaudoti išsaugojimą į failą funkciją
Panaudoti užkrovimo iš failo funkciją
Atspausdinkite užkrautus iš failo duomenis
"""

import pickle
darbuotojas1 = input("Iveskite darbuotojo vardą, pavardę, darbo poziciją:   ")
print(darbuotojas1)
darbuotojas2 = input("Iveskite darbuotojo vardą, pavardę, darbo poziciją:   ")
print(darbuotojas2)



with open("darbuotoju_sarasas.pkl", "wb") as pickle_out:
    pickle.dump(darbuotojas1, pickle_out)
    pickle.dump(darbuotojas2, pickle_out)

with open("darbuotoju_sarasas.pkl", "rb") as pickle_in:
    naujas_darbuotojas1 = pickle.load(pickle_in)
    naujas_darbuotojas2 = pickle.load(pickle_in)


print(naujas_darbuotojas1)
print(naujas_darbuotojas2)

