#Lag et program som leser inn data fra datasettet. lagrer det i egnet datastruktur og regner ut
#totalt antall personer som har deltatt i hver aktivitet. på tvers av alle fylker. Programmet
#skal presentere resultatet i et tabelliknende oppsett som viser aktiviteter og totalt antall 
#deltakere for hver aktivitet.
import json
print("oppgave A")
with open("friluftslivsaktiviteter_2024.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

print("Aktivitet".ljust(60), "Totalt antall")
print("-" * 80)


for aktivitet in data["aktiviteter"]:
    navn = aktivitet["friluftslivsaktivitet"]
    
    totalt = 0

    for antall in aktivitet["fylker"].values():
        totalt += antall

    print(navn.ljust(60), totalt)


#Oppgave 8b 
#Utvid programmet slik at brukeren kan angi eller velge et fylke i grensesnittet 
# (f. eks. Oslo). Programmet skal deretter vise alle aktivitetene for det valgte 
# fylket i stigende rekkefølge, både som antall og som prosentandel. 

import json
print ("Oppgave B")
with open("friluftslivsaktiviteter_2024.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

print("Fylker:")
for kode, navn in data["fylkeskoder"].items():
    print(navn)

valgt_fylke = input("\nSkriv inn fylke: ")

fylkekode = None

for kode, navn in data["fylkeskoder"].items():
    if navn.lower() == valgt_fylke.lower():
        fylkekode = kode

if fylkekode is None:
    print("error")

else:
    resultater = []

    for aktivitet in data["aktiviteter"]:
        navn = aktivitet["friluftslivsaktivitet"]
        antall = aktivitet["fylker"][fylkekode]

        prosent = antall / 1000 * 100

        resultater.append((navn, antall, prosent))
    resultater.sort(key=lambda x: x[1])

    print("\nAktiviteter i", valgt_fylke)
    print("-" * 90)
    print("Aktivitet".ljust(60), "Antall".ljust(10), "Prosent")
    print("-" * 90)
    for navn, antall, prosent in resultater:
        print(navn.ljust(60), str(antall).ljust(10), f"{prosent:.1f}%")