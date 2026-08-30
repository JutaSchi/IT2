#Lag et program der brukeren skriver inn nye tall helt til brukeren skriver inn et tall som er
#  større enn 10. Finn det største og det minste tallet, og beregn summen og gjennomsnittet
#  av alle tallene brukeren skriver inn.
tall = []

while True:
    nummer = float(input("Skriv inn et tall: "))

    if nummer > 10:
        break

    tall.append(nummer)

if tall:
    print("Største tall:", max(tall))
    print("Minste tall:", min(tall))
    print("Sum:", sum(tall))
    print("Gjennomsnitt:", sum(tall) / len(tall))
else:
    print("Du skrev ikke inn noen tall.")