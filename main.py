from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
import os

class Controller(StackLayout):
	xhint = NumericProperty(.15)
	yhint = NumericProperty(.15)
	letters = {}
	letters['a'] = 'Avengers'
	letters['b'] = 'Batman'
	letters['c'] = 'Cyclops'
	letters['d'] = 'Dare Devil'
	letters['e'] = 'Elastic Man'
	letters['f'] = 'Flash'
	letters['g'] = 'Green Lantern'
	letters['h'] = 'Hulk'
	letters['i'] = 'Iron Man'
	letters['j'] = 'Justice League'
	letters['k'] = 'Kapten Amerika'
	letters['l'] = 'Lucius Fox'

	letters['m'] = 'Martian Manhunter'
	letters['n'] = 'Nightwing'
	letters['o'] = 'Owlman'
	letters['p'] = 'Phantom'
	letters['q'] = 'Quick Silver'
	letters['r'] = 'Robin'
	letters['s'] = 'Superman'
	letters['t'] = 'Thor'
	letters['u'] = 'Ultraman'
	letters['v'] = 'Voltus 5'
	letters['w'] = 'Wolverine'
	letters['x'] = 'X-Men'
	letters['y'] = 'Yoda'
	letters['z'] = 'Zodd'

	def do_pressletter(self, letter):
		popup = Popup(title= self.letters[letter],
					content=Image(source="img/" + letter + ".png"),
					size_hint=(None, None), size=(Window.width - 20, Window.height - 50),
					auto_dismiss=True)
		filename = 'snd/' + letter + '.ogg'
		if not os.path.exists(filename):
			filename = 'snd/default.ogg'
		sound = SoundLoader.load(filename)
		sound.play()
		popup.open()

class LetterOfHeroesApp(App):
	def build(self):
		return Controller()

if __name__ == '__main__':
    LetterOfHeroesApp().run()