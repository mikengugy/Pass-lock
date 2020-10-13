import string
import random

class User:
    '''
    class that generates new instances of users.
    '''

    user_list = []

    def __init__(self,user_name,password,email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved contact from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        '''
        method that return the contact list
        '''
        return cls.user_list



