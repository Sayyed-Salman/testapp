from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):
    name = ObjectProperty(None)
    iceCream = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        iceCream = self.iceCream.text
        color = self.color.text

        #self.add_widget(
            #Label(text=f"Hello {name}, you like {iceCream} Ice Cream, and your favourite color is {color}!"))

        print(f"Hello {name}, you like {iceCream} Ice Cream, and your favourite color is {color}!")

        self.name.text = ""
        self.iceCream.text = ""
        self.color.text = ""


class Myapp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    Myapp().run()
