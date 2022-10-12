from kivymd.uix.screen import MDScreen

class LoginScreen(MDScreen):
    def callback(self):
        self.manager.current = 'menu'

    def ValidationLogin(self):
        # print(teste)
        # teste = self.manager.get_screen('login')
        login = self.ids["'login'"].text
        password = self.ids["'password'"].text
        print(login)
        print(password)
        if login == 'admin' and password == 'admin':
            self.ids["'login'"].text = ''
            self.ids["'password'"].text = ''
            self.manager.current = 'authentication'
        else:
            self.ids["'login'"].text = ''
            self.ids["'password'"].text = ''