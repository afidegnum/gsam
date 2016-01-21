from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

class MyScreenManager(ScreenManager):
    pass

class IntroScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class MailScreen(Screen):
    pass

class PrjcScreen(Screen):
    pass

class ChatScreen(Screen):
    pass

class GsaMain(BoxLayout):
    pass


class GsamApp(App):
    def build(self):
        return MyScreenManager()

GsamApp().run()