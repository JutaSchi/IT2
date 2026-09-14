#Lag en ordbok som følger dette mønsteret: krypter = { "a": "c", "b": "d", "c": "e", … }. 
# (Alle nøklene gir en bokstav som ligger to bokstaver etter i alfabetet.) For bokstavene 
# ø og å kan du bruke verdiene "a" og "b".
alfabet = "abcdefghijklmnopqrstuvwxyz"

krypter = {}

for i, bokstav in enumerate(alfabet):
    krypter[bokstav] = alfabet[(i + 2) % 26]

krypter["ø"] = "a"
krypter["å"] = "b"

print(krypter)