def wielkosc_zadluzenia(kwota_poczatkowa, wartosc_oprocentowania, wartosc_raty = 200):
    if type(kwota_poczatkowa) != int and type(kwota_poczatkowa) != float:
        print("Kwota początkowa kredytu musi być liczbą.")
    elif kwota_poczatkowa <= 0:
        print("Kwota początkowa kredytu musi być większa niż 0.")
    elif type(wartosc_oprocentowania) != int and type(wartosc_oprocentowania) != float:
        print("Wartość oprocentowania musi być liczbą.")
    elif type(wartosc_raty) != int and type(wartosc_raty) != float:
        print("Wartość raty musi być liczbą.")
    elif wartosc_raty <= 0:
        print("Wartość raty kredytu musi być większa niż 0.")
    else:
        wielkosc_zadluzenia_zmienna = (1 + ((wartosc_oprocentowania + 3) / 12000)) * kwota_poczatkowa - wartosc_raty
        print(wielkosc_zadluzenia_zmienna)

wielkosc_zadluzenia(11804.59282, -0.453509101)


import pandas as pd
data = pd.read_csv("Desktop/pierwszy_program_dane.csv") 
data

data.loc[1, 'pozyczka']


