#Skriv kode som be bruker å skrive et positiv heltall 
#Man skal skrive tall fortløpende inntil man skrive "-1" 
#For hvert tall bruker skriver skal du: 
#legg tallet til listen 
#legg tallet til mengde 
#registrer tallet i ordboken, men antall ganger den har blitt tastet 
#(tips: hvis tallet er i ordbok øk med 1 antall ganger den tallet dukker opp 
#hvis tallet ikke er i ordboken fra før, legge det med antall ganger lik 1 ) 

tall_liste = []
tall_mengde = set()
tall_orbok = {}

while True:
    tall = int(input("Skriv et positivt heltall (-1 for å avslutte): "))

    if tall == -1:
        break

    # Tall append list
    tall_liste.append(tall)

    # mengde
    tall_mengde.add(tall)

    if tall in tall_orbok:
        tall_orbok[tall] += 1
    else:
        tall_orbok[tall] = 1

print("Liste:", tall_liste)
print("Mengde:", tall_mengde)
print("Ordbok:", tall_orbok)