import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

print(kivy.__version__)



class ImagrApp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    ImagrApp().run()
