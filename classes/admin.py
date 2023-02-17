from user import User

class Privileges:
    def __init__(self, privileges=("can add post", "can delete post", "can ban user")):
        self.privilages = privileges
   
    def show_privileges(self):
        for privilage in self.privilages:
            print(privilage)

class Admin(User):
    def __init__(self, f_name, l_name, **user_pro):
        super().__init__(f_name, l_name, **user_pro)
        self.privilage = Privileges()
