a = 27
b = 47
c = 83

siste_a = a % 10
siste_b = b % 10
siste_c = c % 10

if siste_a == siste_b:
    print("a =", a, "og b =", b, "har felles siste siffer:", siste_a)

if siste_a == siste_c:
    print("a =", a, "og c =", c, "har felles siste siffer:", siste_a)

if siste_b == siste_c:
    print("b =", b, "og c =", c, "har felles siste siffer:", siste_b)
