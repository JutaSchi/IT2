print("1")
tall1 = float(input("Skriv inn tall 1: "))
tall2 = float(input("Skriv inn tall 2: "))
tall3 = float(input("Skriv inn tall 3: "))

#er like?
if tall1 == tall2 and tall2 == tall3:
    print("Alle tallene er like.")
else:
    print("Tallene er ikke like.")


#2
print("2")

tall = int(input("Skriv inn et heltall: "))

if tall % 2 == 0:
    print("Tallet er et partall.")
else:
    print("Tallet er et oddetall.")


# 3
print("3")

tall1 = float(input("Skriv inn tall 1: "))
tall2 = float(input("Skriv inn tall 2: "))
tall3 = float(input("Skriv inn tall 3: "))

if tall1 >= tall2 and tall1 >= tall3:
    print("Det største tallet er", tall1)
elif tall2 >= tall1 and tall2 >= tall3:
    print("Det største tallet er", tall2)
else:
    print("Det største tallet er", tall3)
