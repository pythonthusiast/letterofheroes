from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label

class Controller(Widget):
	def __init__(self):
		Widget.__init__(self)
		label = Label(text="Howdy!")
		self.add_widget(label)

class LetterOfHeroesApp(App):
	def build(self):
		return Controller()

if __name__ == '__main__':
    LetterOfHeroesApp().run()