class User:
    def __init__(self, f_name, l_name, **user_pro):
        self.f_name = f_name
        self.l_name = l_name
        self.user_pro = user_pro
        self.user_pro['first_name'] = f_name
        self.user_pro['last_name'] = l_name

    def describe_user(self):
        print(self.user_pro)

    def greet_user(self):
        print(f'Good day {self.f_name} {self.l_name}.')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

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