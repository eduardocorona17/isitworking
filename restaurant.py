class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        # self.name = 'Bear'
        # self.cuisine = 'Elemental'
        details = f"The restaurant's name is {self.name} and they serve {self.cuisine}. They have currently served {self.number_served} people." 
        if self.number_served:
            print(details)
        else:
            print(f"The restaurant's name is {self.name} and they serve {self.cuisine} cuisine.")
    
    def people_served(self):
        """Displays number of people served."""
        print(f"They have served {self.number_served} people today")
        
    def update_people_served(self, served):
        self.number_served = served 

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def increment_number_served(self, people):
        """Increments the number of people served by the restaurant."""
        self.number_served += people
        # print(f"So far they have now served {self.number_served} people.")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['Vanilla', 'Chocolate']

    def show_flavors(self):
        print(f"{self.name} serves the following flavors: ")
        for flavor in self.flavors:
            print(f"{flavor}")

stand = IceCreamStand('Joes', 'Creamery')

stand.show_flavors()
restaurant = Restaurant('Bear', 'Elemental')
rival_restaurant = Restaurant('ADS', 'American')
third_rest = Restaurant('SolBar', 'New American')
# print(f"The restaurant's name is {restaurant.name}.")
# print(f"They serve {restaurant.cuisine} styled cuisine.")
rival_restaurant.describe_restaurant()
third_rest.describe_restaurant()
restaurant.describe_restaurant()
restaurant.open_restaurant()
rest = Restaurant('Bouchon', 'French')
rest.describe_restaurant()
rest.people_served()
rest.update_people_served(47)
rest.increment_number_served(53)
rest.people_served()
rest.increment_number_served(117)
rest.people_served()

# class Users:
#     def __init__(self, first_name, last_name, location, age, username):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.location = location
#         self.age = age
#         self.username = username
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f"The following info is collected from the user:\n{self.first_name} {self.last_name}\n{self.location}\n{self.age}\n{self.username}")
    
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#         print(f"{self.username} logged in {self.login_attempts} times.")
    
#     def reset_logins(self):
#         self.login_attempts = 0
#         print(f"Attempts to log in have been reset to {self.login_attempts}")

# class Admin(Users):
#     def __init__(self, first_name, last_name, location, age, username):
#         super().__init__(first_name, last_name, location, age, username)
#         self.priviliges = ['Can add post.', 'Can ban user.', 'Can delete post.']
    
#     def show_priviliges(self):
#         """Shows Admins privileges."""
#         print(f"{self.username.title()} has the following priviliges: ")
#         for p in self.priviliges:
#             print(f"{p}")


# user = Users('Ed', 'Corona', 'Napa, CA', 32, 'Eduarthough')
# user.describe_user()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.reset_logins()
# ad = Admin('Ed', 'Co', 'Honolulu', 32, 'edudu')
# ad.show_priviliges()