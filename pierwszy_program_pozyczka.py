def wielkosc_zadluzenia(kwota_poczatkowa, wartosc_oprocentowania, wartosc_raty):
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

kwota_poczatkowa = float(input("Wprowadź kwotę początkową kredytu: "))
wartosc_oprocentowania = float(input("Wprowadź wartość oprocentowania: "))
wartosc_raty = float(input("Wprowadź wysokość raty kredytu: "))

variables_in_function = wielkosc_zadluzenia(kwota_poczatkowa, wartosc_oprocentowania, wartosc_raty)