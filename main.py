from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class AuthApp(App):
    def build(self):
        gl = GridLayout()
        btn = Button(text='Привет')

        gl.add_widget(btn)
        return gl

if __name__ == "__main__":
    AuthApp().run()