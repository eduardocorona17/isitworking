class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        # self.name = 'Bear'
        # self.cuisine = 'Elemental'
        print(f"The restaurant's name is {self.name}.")
        print(f"They serve {self.cuisine} cuisine.")
    def open_restaurant(self):
        print(f"{self.name} is now open!")

restaurant = Restaurant('Bear', 'Elemental')
rival_restaurant = Restaurant('ADS', 'American')
third_rest = Restaurant('SolBar', 'New American')
# print(f"The restaurant's name is {restaurant.name}.")
# print(f"They serve {restaurant.cuisine} styled cuisine.")
rival_restaurant.describe_restaurant()
third_rest.describe_restaurant()
restaurant.describe_restaurant()
restaurant.open_restaurant()

class Users:
    def __init__(self, first_name, last_name, location, age, username):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.username = username

    def describe_user(self):
        print(f"The following info is collected from the user:\n{self.first_name} {self.last_name}\n{self.location}\n{self.age}\n{self.username}")
        
user = Users('Ed', 'Corona', 'Napa, CA', 32, 'Eduarthough')
user.describe_user()
