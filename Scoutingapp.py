import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #Initalize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

    # Set columns (how many you want)

        self.cols = 1

    # Create a second Gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # Add widgets
        self.top_grid.add_widget(Label(text="Points:"))
        # Add Input Box
        self.points = TextInput(multiline=True) #means there is only one line
        self.top_grid.add_widget(self.points)

        self.top_grid.add_widget(Label(text="Shots Scored:"))
        # Add Input Box
        self.shooting = TextInput(multiline=False)  # means there is only one line
        self.top_grid.add_widget(self.shooting)

        self.top_grid.add_widget(Label(text="Foul:"))
        #Add Input Box
        self.foul = TextInput(multiline=False) #means there is only one line
        self.top_grid.add_widget(self.foul)

        # Add the new top_grid to our app
        self.add_widget(self.top_grid)

        #Create a Submit button
        self.submit = Button(text="Submit", font_size = 32)
        # Bind the Button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        points = self.points.text
        shooting = self.shooting.text
        foul = self.foul.text # ".text" = textinput

        #print(f'You scored {points} points, you scored {shooting} shots, and had {foul} fouls')
        # Print it to the screen
        self.add_widget(Label(text=f'You scored {points} points, you scored {shooting} shots, and had {foul} fouls'))

        # Clear the input boxes
        self.points.text = ""
        self.shooting.text = ""
        self.foul.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()


