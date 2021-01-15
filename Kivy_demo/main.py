from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import json
from datetime import datetime

Builder.load_file("design.kv")

"""
    kivy

    py file need identifier which named classes with same names as screen names into kv file 

    in specified screen could call functions which defined in specified class 
"""


class LoginScreen(Screen):
    """ go to sign up page """
    def sign_up(self):
        self.manager.current = "sign_up_screen"


class SignUpScreen(Screen):
    """
        ids object is belong to TextInput
        .text can transform the object to string
    """
    def add_user(self, username, password):
        with open("Kivy_demo/users.json", "r") as f:
            users = json.load(f)

        users[username.text] = {'username': username.text, 'password': password.text, 'created': datetime.now().strftime("%Y-%m-%d %H:%M:%s")}
        
        with open("Kivy_demo/users.json", "w") as f:
            json.dump(users, f)

        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    """ go to login page, and switching pages will roll to right """
    def back_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class RootWidget(ScreenManager):
    """ reflect Rootwidge in kv file """
    pass


class MainApp(App):
    """
        Startup

        build() must be defined, and return the manager of screens

    """
    def build(self):
        return RootWidget()


if __name__ == "__main__":

    MainApp().run()