phone_book = {
  "Mateusz": 123123123,
  "Mariusz": 666666666,
  "Tomek": 321233244
}

print(phone_book.get("Mateusz"))
print(phone_book["Mateusz"])

phone_book["Tomek"] = 200200200
print(phone_book)

phone_book.pop("Mariusz")
print(phone_book)

for element in phone_book:
  print(element)
for element in phone_book.values():
  print(element)
for element in phone_book.items():
  print(element)


for element in phone_book.items():
  print(element[0] + ": " + str(element[1]))
#LUB
for name, phone_number in phone_book.items():
  print(name + ": " + str(phone_number))
