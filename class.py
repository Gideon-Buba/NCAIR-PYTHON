class Person:
    def __init__(self, first_name, last_name, age, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone

guy = Person("Marvelous", "Aduku", 20, 80123456)

print(f"My name is {guy.first_name} {guy.last_name}, and I am {guy.age} years old and you can reach me by calling {guy.phone}")


# def full_name(first_name, last_name):
#     name = f"My full name is {first_name} {last_name}"
#     return name
#
#
# first_name = input("Input first name: ")
# last_name = input("Input last name: ")
#
# print(full_name(first_name, last_name))

