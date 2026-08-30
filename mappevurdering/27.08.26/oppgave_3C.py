#Lag et program som triller én terning n ganger, og som beregner 
#summen og gjennomsnittet av terningkastene.
import random

n = int(input("Skriv inn et positivt heltall: "))
sum_kast=0
for i in range (n):
    kast=random.randint(1,6)
    print("Terningkast",kast)
    sum_kast+=kast

gjennomsnitt=sum_kast/n
print("sum",sum_kast)
print("gjennomsnitt", gjennomsnitt)