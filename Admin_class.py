from User_module import Users

class Admin(Users):
    def __init__(self, first_name, last_name, location, age, username):
        super().__init__(first_name, last_name, location, age, username)
        self.priviliges = ['Can add post.', 'Can ban user.', 'Can delete post.']
    
    def show_priviliges(self):
        """Shows Admins privileges."""
        print(f"{self.username.title()} has the following priviliges: ")
        for p in self.priviliges:
            print(f"{p}")

eddie = Admin('E', 'C', 'Naps', 32, 'Duardo')
eddie.show_priviliges()