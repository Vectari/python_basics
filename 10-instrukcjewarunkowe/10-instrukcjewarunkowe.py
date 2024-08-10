age = int(input("Ile masz lat?"))
light = input("Jakie jest światło? (zielone, żółte, czerwone)")

print("---------------------")

if age >= 18:
    print("pełnoletni")
else:
    print("niepełnoletni")
    
if light == "zielone":
    print("jedziesz")
elif light == "żółte":
    print("zaraz jedziesz")
elif light == "czerwone":
    print("stop")
else:
    print("zły kolor")