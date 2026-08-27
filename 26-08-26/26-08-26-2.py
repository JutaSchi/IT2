import math

r = 4

h_sylinder = 8
h_kjegle = 4

v_kule = (4 / 3) * math.pi * r**3

v_sylinder = math.pi * r**2 * h_sylinder

v_kjegle = math.pi * r**2 * h_kjegle / 3

v_total = v_kule + v_sylinder + v_kjegle

print(f"Volum av kulen: {v_kule:.2f} cm³")
print(f"Volum av sylinderen: {v_sylinder:.2f} cm³")
print(f"Volum av kjeglen: {v_kjegle:.2f} cm³")
print(f"Totalvolum: {v_total:.2f} cm³")
print(f"Totalvolum: {v_total / 1000:.2f} liter")

