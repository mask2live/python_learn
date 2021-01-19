from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

from Files.hoverable import HoverBehavior

import json, random
from datetime import datetime

Builder.load_file("design.kv")

"""
    kivy

    py file need identifier which named classes with same names as screen names into kv file 

    in specified screen could call functions which defined in specified class 
"""


class LoginScreen(Screen):

    def sign_up(self):
        """ go to sign up page """
        self.manager.current = "sign_up_screen"
    
    def login(self, username, password):
        """
            login
            check username and password wether correct with json file
            if something wrong, it will display the tip
            if go through,  we need clean content of password and tip panels and switch to login_screen_success page
        """
        with open("Kivy_demo/users.json", 'r') as f:
            users = json.load(f)
        
        if username in users and users[username]['password'] == password:
            self.ids.login_wrong.text = ""
            self.ids.password.text = ""
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong username or password"


    def go_to_forgot(self):
        self.manager.current = "forgot_password_screen"

class SignUpScreen(Screen):
    """
        ids object is belong to TextInput
        .text can transform the object to string
    """
    def add_user(self, username, password):
        """
            add user
            if username or password is empty, this method would be stopped
            if username is already existed in json file, this method would be stopped
            write the user info into json file
            cancel or submit succeed, all entries will be clear
            switch to sign_up_screen_success page after submit succeed
        """
        with open("Kivy_demo/users.json", "r") as f:
            users = json.load(f)
        
        if username.text == "" or password.text == "":
            self.ids.signup_wrong.text = "username or password can not be empty"
            return
        if username.text in users:
            self.ids.signup_wrong.text = "this username is already existed."
            return
        
        users[username.text] = {'username': username.text, 'password': password.text, 'created': datetime.now().strftime("%Y-%m-%d %H:%M:%s")}
        
        with open("Kivy_demo/users.json", "w") as f:
            json.dump(users, f)


        self.ids.username.text = ""
        self.ids.password.text = ""
        self.ids.signup_wrong.text = ""
        self.manager.current = "sign_up_screen_success"

    def back_to_login(self):
        """ switch to login_screen page """
        self.ids.username.text = ""
        self.ids.password.text = ""
        self.ids.signup_wrong.text = ""
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class SignUpScreenSuccess(Screen):
    """ go to login page, and switching pages will roll to right """
    def back_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):

    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, inputs):
        """
            quote
            according input to get relative content from quotes dir and output one line randomly
            if dir has no relative content, output what input is
        """
        try:
            with open(f"Kivy_demo/quotes/{inputs.lower()}.txt", "r") as f:
                content = f.readlines()
                self.ids.quotestatement.text = random.choice(content)
        except FileNotFoundError as e:
            self.ids.quotestatement.text = self.ids.tryinput.text
            # pass
        
class ImageButton(HoverBehavior, Image, ButtonBehavior):
    pass


class ForgotPasswdScreen(Screen):

    def confirm_username(self, username, confirm):
        if username != confirm:
            self.ids.forgot_tip.text = "Inconsistent username"
            return

        with open("Kivy_demo/users.json", "r") as f:
            users = json.load(f)
        
        if username not in users:
            self.ids.forgot_tip.text = "This username not exist"
            return

        self.manager.current = "reset_password_screen"


class ResetPasswdScreen(Screen):
    def reset(self, username, passwd, passwd_confirm):
        if passwd != passwd_confirm:
            self.ids.reset_tip.text = "Inconsistent password"
            return
        if passwd == "" or passwd_confirm == "":
            self.ids.reset_tip.text = "Invalid password"
            return
        
        with open("Kivy_demo/users.json", "r") as f:
            users = json.load(f)

        users[username]["password"] = passwd
    
        with open("Kivy_demo/users.json", "w") as f:
            json.dump(users, f)
        
        self.ids.reset_tip.text = ""
        self.ids.username.text = ""
        self.ids.passwd.text = ""
        self.ids.passwd_confirm.text = ""

        self.manager.current = "reset_success_screen"

class ResetPasswdSuccessScreen(Screen):
    def back_login(self):
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