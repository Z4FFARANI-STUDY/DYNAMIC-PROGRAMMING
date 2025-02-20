def calcular_formas(forma):
    match forma:
        case "cilindro":
            r = float(input("Raio: "))
            h = float(input("Altura: "))
            return f"Área: {((2 * 3.1415) * r * h) + ((2 * 3.1415) * (r**2))} | Volume: {3.14 * (r**2) * h}"
        case "retangulo":
            b = float(input("Base: "))
            h = float(input("Altura: "))
            l = float(input("Largura: "))
            return f"Área: {b * h} | Volume: {b * h * l}"

print(calcular_formas("retangulo"))