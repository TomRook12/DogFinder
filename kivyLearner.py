import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialise infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="Name: "))
        # Add Input Box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favourite Pizza: "))
        # Add Input Box
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favourite Colour: "))
        # Add Input Box
        self.colour = TextInput(multiline=False)
        self.add_widget(self.colour)

        # Create a submit button
        self.submit = Button(text="Submit", font_size=32)
        #Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name = self.name.text
        pizza = self.pizza.text
        colour = self.colour.text

        self.add_widget(Label(text=f"Hello {name}, you like {pizza} pizza, and your favourite colour is {colour}"))

        #Clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.colour.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()