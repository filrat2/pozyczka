# import needed modules
import pandas as pd


# main function
def wielkosc_zadluzenia(kwota_poczatkowa, wartosc_oprocentowania, wartosc_raty):
    wielkosc_zadluzenia_zmienna = (1 + ((wartosc_oprocentowania + 3) / 1200)) \
                                      * kwota_poczatkowa - wartosc_raty
    diff = kwota_poczatkowa - wielkosc_zadluzenia_zmienna
    print(f"Twoja pozostała kwota kredytu to "
          f"{round(wielkosc_zadluzenia_zmienna, 2)}, "
          f"to {round(diff, 2)} mniej niż w poprzednim miesiącu.\n")


# create data frame from *.csv file
df = pd.read_csv("pozyczka_dane.csv")
df = df.reset_index()
df

obj = []

# for loop - create list with lists containing attributes for every month
for index, row in df.iterrows():
    if index == 24:
        break
    else:
        obj.append([df.loc[(index + 1), "inflacja"],
                    df.loc[index, "pozyczka"],
                    200])

# run function 'wielkosc_zadluzenia' by for loop with attributes from list
for i in range(0, len(obj)):
    wielkosc_zadluzenia(obj[i][1], obj[i][0], obj[i][2])
