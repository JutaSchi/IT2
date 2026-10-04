spillere = [
["Astra", 42, 1200],
["Blaze", 15, 3500],
["Cypher", 88, 450],
["Drift", 60, 2100],
]


spillere.sort(key=lambda rad: rad[1], reverse=True)
for spiller in spillere:
	print(f"Spiller: {spiller[0]}, Nivå: {spiller[1]}")

mest_gull=max(spillere, key=lambda rad:rad[2])



#Maksimum og Minimum:
#Finn og skriv ut navn og gull til spilleren som har flest gull.
#Finn og skriv ut navn og nivå til spilleren med lavest nivå.


mest_gull = max(spillere, key=lambda x:x[2])
lavest_nivaa = min(spillere, key=lambda x:x[1])
 
print(f"\n{mest_gull[0]} har mest gull. Med {mest_gull[2]} gull.\n")
print(f"{lavest_nivaa[0]} har lavest nivå. Med {lavest_nivaa[1]} nivåer.")

print("3")
totalt_gull = sum(map(lambda rad: rad[2], spillere))
print ({totalt_gull})
