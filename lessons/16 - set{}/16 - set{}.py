names = {"Mateusz", "Mariusz", "Dominik", "Kamil"}
names2 = {"Mateusz", "Ola", "Klaudia", "Czesław"}
names3 = set()

print(type(names3))

# names.add("Radek")
# names.remove("Kamil")


# print(names)


# for name in names:
#   print(name)


# names.update({"Ola", "Ala"})
# # LUB
# names.update(["Ola2", "Ala2"])


# for name in names:
#   print(name)


#SUMA ZBIORÓW
print(names | names2)
# LUB
print(names.union(names2))

#część wspólna
print(names.intersection(names2))
#LUB
print(names & names2)

#różnica
print(names.difference(names2))
#lub
print(names - names2)
