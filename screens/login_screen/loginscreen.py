from kivymd.uix.screen import MDScreen

class LoginScreen(MDScreen):
    def callback(self):
        self.manager.current = 'menu'
    pass
