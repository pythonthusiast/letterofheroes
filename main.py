from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty

class Controller(FloatLayout):
	label_wid = ObjectProperty()
	info = StringProperty()

	def do_action(self):    	
		self.label_wid.text = 'My label after button press'
		self.info = 'New info text'    

class LetterOfHeroesApp(App):
	def build(self):
		return Controller(info="Letter of Heroes")

if __name__ == '__main__':
    LetterOfHeroesApp().run()