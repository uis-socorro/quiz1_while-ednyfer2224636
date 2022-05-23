c1 = float(input("Ingrese el valor del capital de Pedro: "))
c2 = float(input("Ingrese el valor del capital Juan: "))
c3 = float(input("Ingrese el valor del capital necesario para el negocio: "))
m = 0

dn = float(c1 + c2)

while dn < c3:
    c1 = (c1 + (c1 * 0.03))
    c2 = (c2 + (c2 * 0.04))
    dn = c1 + c2
    m = m + 1

print("En ", str(m), " meses, Pedro y Juan podrán hacer el negocio")

