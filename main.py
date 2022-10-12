import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory

# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "screens/login_screen/loginscreen.kv"),
        os.path.join(os.getcwd(), "screens/menu_screen/menuscreen.kv"),
        os.path.join(os.getcwd(), "screens/registration_screen/registrationscreen.kv")
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "screens.screenmanager",
        "MenuScreen": "screens.menu_screen.menuscreen",
        "LoginScreen": "screens.login_screen.loginscreen",
        "RegistrationScreen": "screens.registration_screen.registrationscreen"
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        self.theme_cls.primary_palette = "Purple"
        return Factory.MainScreenManager()

# finally, run the app
if __name__ == "__main__":
    LiveApp().run()
