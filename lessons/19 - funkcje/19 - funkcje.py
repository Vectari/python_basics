# # def hello1():
# #   print("Hello1")


# # hello1()
# # hello1()
# # hello1()


# # name = input("imie?")
# # age = int(input("wiek?"))


# # def hello(name, age, last_name=None):
# #   print(f"Hello {name}. Wiek: {age}")

# #   if last_name is not None:
# #     print("Nazwisko: " + last_name)

# # hello(name="Tomek", age=20)
# # hello(name="Tomek", age=20, last_name="nazwisko")
# # hello(name, age)


# text = input("Podaj tekst: ")

# def strip_and_uppercase(text):
#   return str(text).strip().upper()
  

# result = strip_and_uppercase(text)

# print(result)

countries_information = {}
countries_information["Polska"] = ("Warszawa", 38)
countries_information["Niemcy"] = ("Berlin", 83)
countries_information["Francja"] = ("Paryż", 57)

country = input("Kraj:")

def country_info(country):

  print()
  print(f"Kraj:{country}")
  print("Stolica: " + countries_information[country][0])
  print("Liczba mieszkańców (mln): " + str(countries_information[country][1]))

country_info(country)
