# Solicitar potência e voltagem ao usuário
p = float(input("Informe a potência (P) em watts: "))
v = float(input("Informe a voltagem (V) em volts: "))

i = p / v

print(f"A corrente (I) é: {i} amperes.")

print()

# Solicitar resistência e corrente ao usuário
r = float(input("Informe a resistência (R) em ohms: "))
i = float(input("Informe a corrente (I) em amperes: "))

v = i * r

print(f"A voltagem (V) é: {v} volts.")

print()

# Solicitar resistência e corrente ao usuário
r = float(input("Informe a resistência (R) em ohms: "))
i = float(input("Informe a corrente (I) em amperes: "))

p = r * (i ** 2)

print(f"A potência (P) é: {p} watts.")