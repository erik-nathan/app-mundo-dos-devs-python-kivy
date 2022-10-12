from kivymd.uix.screen import MDScreen

class AuthenticationScreen(MDScreen):
    def callback(self):
        self.manager.current = 'menu'