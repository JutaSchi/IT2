#Lag et program som tegner «kvadrater» ved hjelp av symbolet «#».
#Brukeren skal oppgi kvadratets sidelengde. Hvis brukeren for eksempel 
#skriver 5, skal programmet tegne:

n = int(input("Skriv inn et tall: "))

for i in range (n):
    print("#" * n)