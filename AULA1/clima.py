def recomendacao(clima):
    match clima:
        case "ensolarado":
            return "dia de futebol e churrasco!"
        case "chuvoso":
            return "dia de filme e série!"
        case "nublado":
            return "dia de ler um livro!"
        case "nevando":
            return "ótimo dia para tomar um café ou chocolate!"
        case _:
            return "?"

print(recomendacao("nevando"))
