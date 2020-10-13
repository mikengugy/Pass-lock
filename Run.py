#!/usr/bin/env python3.6
from password_locker import User, Credentials

def create_user(user_name,password,email):
    '''
    Function to create a new user
    '''

    new_user = User(user_name,password,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''

    user.save_user()

def display_users():
    '''
    Function to return all the saved users
    '''
    return User.display_users()

def login_user(user_name,password):
    '''
    Function to see if user exist and allow them to login
    '''

    check_user_exist = Credentials.check_user_exist(user_name,password)
    return check_user_exist

def create_credential(account_name,account_username,account_password):
    '''
    Function to create a new credential
    '''

    new_credential = Credentials(account_name,account_username,account_password)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''

    credential.save_credential()

def display_credential():
    '''
    Function to return all saved credentials
    '''

    return Credentials.display_credential()

def del_credential(credential):
    '''
    Function to delete a credential
    '''

    credential.delete_credential()

def generate_password():
    '''
    Function that generates random password.
    '''

    password_gen = Credentials.generate_password()

    return password_gen


