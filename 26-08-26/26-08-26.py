import math

r = 31.83
l = 100
fart_kmh = 50

bane_lengde = 2 * l + 2 * math.pi * r

fart_ms = fart_kmh / 3.6

avstand_10_runder = bane_lengde * 10
tid_sekunder = avstand_10_runder / fart_ms

print("Banens lengde:", bane_lengde, "m")
print("Gjennomsnittsfart:", fart_ms, "m/s")
print("Tid for 10 runder:", tid_sekunder, "sekunder")
