from kivy.app import App

class TutorialApp(App):
    pass

if __name__ == "__main__":
    TutorialApp().run()

class RemoteConnect():
    def __init__(self, host, params):
        self.host = host
        self.params = params