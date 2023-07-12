# Create two Mixins:
UsernameLengthMixin
UsernameAlphanumericMixin


# The mixin should include a method called validate() that takes a value as an argument and checks if it meets certain criteria.


# Create a User class with a method called set_username().
# Then combine the User class with your Mixin in the following new classes:
UserWithLengthValidation 
UserWithAlphanumericValidation


# This method should take a username as an argument, validate it using the validate() method from the mixin, and set it as the username attribute of the User class.
# Hint:
# You don't need to use the super() keyword.




class User():
    def __init__(self, name) -> None:
        self.name = name
        
    def set_username(self):
        return self.name



class UsernameLengthMixin(User):
   def validate():


class UsernameAlphanumericMixin(User):
   def validate():



class UserWithLengthValidation(...., User):
    pass