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
