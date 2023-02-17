class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name} and cuisine name is {self.cuisine_type}.')

    def open_restaurant(self):
        print('The Restaurant is open.')

    def set_number_served(self):
        self.number_served = 56
        return self.number_served
    
    def increment_number_served(self, person_served):
        self.number_served += person_served
        return f'we served {self.number_served} customers today.'
