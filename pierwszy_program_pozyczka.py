# main function

def wielkosc_zadluzenia(kwota_poczatkowa, wartosc_oprocentowania, wartosc_raty):
        wielkosc_zadluzenia_zmienna = (1 + ((wartosc_oprocentowania + 3) / 1200)) \
                                      * kwota_poczatkowa - wartosc_raty
        diff = kwota_poczatkowa - wielkosc_zadluzenia_zmienna
        print(f"Twoja pozostała kwota kredytu to "
              f"{round(wielkosc_zadluzenia_zmienna, 2)}, "
              f"to {round(diff, 2)} mniej niż w poprzednim miesiącu.")


# define variables / user inputs
kwota_poczatkowa = float(input("Wprowadź kwotę początkową kredytu: "))
wartosc_oprocentowania = float(input("Wprowadź wartość oprocentowania ponad inflację: "))
wartosc_raty = float(input("Wprowadź wysokość raty kredytu: "))

# connecting user inputs with function
variables_in_function = wielkosc_zadluzenia(kwota_poczatkowa,
                                            wartosc_oprocentowania,
                                            wartosc_raty)