names = ["Mateusz", "Tadek", "Stefan"]
names.append("Kuba")
names.extend(["Ola", "Tomek"])

# print(names)
# print(names[1])

# for name in names:
#   print(name)

# del names[1]
# print(names) 

names.remove("Mateusz")
print(names)
print(names.count("Tadek"))
print(len(names))
names.sort(reverse=True)
print(names)
