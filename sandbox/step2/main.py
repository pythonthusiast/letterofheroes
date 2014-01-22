from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class Controller(Widget):
	def __init__(self):
		Widget.__init__(self)
		btnHello = Button()
		btnHello.text = "Greet"
		btnHello.bind(on_press = self.btnHello_pressed)
		self.add_widget(btnHello)

	def btnHello_pressed(self, event):
		popup = Popup(title = "Letter of Heroes", 
				content = Label(text = "Howdy Pythonistas!"), 
				size = (200,2	00), 
				size_hint=(None, None),
				auto_dismiss=True)
		popup.open()

class LetterOfHeroesApp(App):
	def build(self):
		return Controller()

if __name__ == '__main__':
    LetterOfHeroesApp().run()