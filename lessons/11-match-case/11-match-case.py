light = input("Jakie jest światło? (zielone, żółte, czerwone)")

print("---------------------")

match light:
    case "zielone":
        print("jedziesz")
    case "żółte":
        print("zaraz jedziesz")
    case "czerwone":
        print("stop")
    case _:
        print("zły kolor")
