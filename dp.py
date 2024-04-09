"""1.Singleton Pattern"""
import sqlite3


class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect("database.db")
        return cls._instance

    def get_connection(self):
        return self.conn


# Usage:
# Instead of directly connecting to the database:
# conn = sqlite3.connect('database.db')
# Use the Singleton instance:
# db = DatabaseManager().get_connection()

"""2.Observer Pattern"""


# Define an Observer class
class Observer:
    def update(self):
        pass


# Define a Subject class
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


# Usage:
# In your Flask application, Subject can be a model or controller class.
# Observers could be various components that need to be notified on certain events.

"""3.Strategy Pattern"""


# Define a Strategy interface
class SearchStrategy:
    def search(self):
        pass


# Define concrete strategy classes
class BloodGroupSearch(SearchStrategy):
    def search(self):
        # Implement blood group search logic
        pass


class DonorNameSearch(SearchStrategy):
    def search(self):
        # Implement donor name search logic
        pass


# Usage:
# In your Flask route, instantiate the strategy based on the user's choice (blood group or donor name)
# Use the strategy to perform the search.


"""4.Template Method Pattern"""


# Define a template class
class UserFormTemplate:
    def process_form(self):
        self.validate_input()
        self.insert_data()

    def validate_input(self):
        # Common validation logic
        pass

    def insert_data(self):
        # Common data insertion logic
        pass


# Create subclasses for specific forms
class RegistrationForm(UserFormTemplate):
    def insert_data(self):
        # Specific data insertion logic for registration form
        pass


class ProfileUpdateForm(UserFormTemplate):
    def insert_data(self):
        # Specific data insertion logic for profile update form
        pass


"""5.Fascade Pattern"""


# Define a Facade class
class BloodBankFacade:
    def __init__(self):
        self.user_manager = UserManager()
        self.blood_manager = BloodManager()

    def add_new_user(self, data):
        return self.user_manager.add_user(data)

    def add_blood_entry(self, data):
        return self.blood_manager.add_blood_entry(data)


# Usage:
# Instead of interacting directly with the UserManager and BloodManager,
# use the BloodBankFacade to perform user or blood-related operations.


"""6.Command Pattern"""


# Define command interface
class Command:
    def execute(self):
        pass


# Define concrete command classes
class BloodDonationCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.donate_blood()


# Define receiver class
class BloodReceiver:
    def donate_blood(self):
        # Logic for blood donation
        pass


# Usage:
# Instantiate and execute commands based on different requests or operations.


"""7.abstract factory"""


# Define abstract factory
class UserFactory:
    def create_user(self):
        pass


class BloodFactory:
    def create_blood_entry(self):
        pass


# Define concrete factories
class ConcreteUserFactory(UserFactory):
    def create_user(self):
        return User()


class ConcreteBloodFactory(BloodFactory):
    def create_blood_entry(self):
        return BloodEntry()


# Usage:
# Use the factories to create objects without specifying their concrete classes.


"""8.Flyweight Pattern"""


# Define a Flyweight factory
class BloodTypeFactory:
    _blood_types = {}

    def get_blood_type(self, blood_group):
        if blood_group not in self._blood_types:
            self._blood_types[blood_group] = BloodType(blood_group)
        return self._blood_types[blood_group]


# Define a Flyweight class
class BloodType:
    def __init__(self, blood_group):
        self.blood_group = blood_group


# Usage:
# Use the BloodTypeFactory to create and reuse BloodType objects based on blood group.
