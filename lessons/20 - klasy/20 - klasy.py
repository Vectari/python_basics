# User
# name
# mail
# age

class User:
  def __init__(self, name, mail, age):
    self.name = name
    self.mail = mail
    self.age = age

  def print_info(self):
    print(self.name)
    print(self.mail)
    print(self.age)

  def is_male(self):
    return self.name[-1:] != "a"


user = User("Mateusz", "mateusz@mail", 28)

user1 = User("Ola", "ola@mail", 22)

user.print_info()
print(user.is_male())
print()
user1.print_info()
print(user1.is_male())
