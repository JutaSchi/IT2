#Lag et program som beregner summen og gjennomsnittet av alle positive heltall
#opp til og med et tall som skrives inn av brukeren.

n = int(input("Skriv inn et positivt heltall: "))

sum = 0

for i in range(1, n + 1):
    sum += i

gjennomsnitt = sum / n

print("Summen er:", sum)
print("Gjennomsnittet er:", gjennomsnitt)
