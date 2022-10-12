from kivymd.uix.screen import MDScreen

class RegistrationScreen(MDScreen):
    def callback(self):
        self.manager.current = 'menu'
    pass
