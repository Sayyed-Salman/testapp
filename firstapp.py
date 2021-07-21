import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 2

        # Input Box
        self.add_widget(Label(text="Name:"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favourite Ice Cream:"))
        self.iceCream = TextInput(multiline=False)
        self.add_widget(self.iceCream)

        self.add_widget(Label(text="Favourite Color:"))
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        self.add_widget(Label(text="Write a Review: "))
        self.review = TextInput(multiline=True)
        self.add_widget(self.review)

        # Button

        self.submit = Button(text="Submit", font_size=33)
        # Bind the Button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        iceCream = self.iceCream.text
        color = self.color.text

        self.add_widget(
            Label(text=f"Hello {name}, you like {iceCream} Ice Cream, and your favourite color is {color}!"))

        self.name.text = ""
        self.iceCream.text = ""
        self.color.text = ""


class Myapp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    Myapp().run()
