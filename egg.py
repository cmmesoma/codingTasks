class Wolf:
# Class variables
    classification = "canine"
    habitat = "forest"
    is_sleeping = False # Defaults to being awake initially
# Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Method that returns the sleep state of the wolf
    def show_sleep_state(self):
        if self.is_sleeping == False:
            return self.name + " is awake"
        else:
            return self.name + " is sleeping"
# Initialise a wolf object and print the initial sleep
# state which is awake
silver_tooth = Wolf("Silver Tooth", 6)
print(silver_tooth.show_sleep_state())
# Change sleep state to sleeping using dot notation and then print new state
silver_tooth.is_sleeping = True
print(silver_tooth.show_sleep_state())