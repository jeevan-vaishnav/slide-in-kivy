from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.slider import Slider
# from kivy.properties import ObjectProparty

# load the kv file
Builder.load_file('kv.kv')


class MyLayout(Widget):
    def slide_it(self, *args):
        self.slide_text.text = str(int(args[1]))
        self.slide_text.font_size = str(int(args[1]))


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()
