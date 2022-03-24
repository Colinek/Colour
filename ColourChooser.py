from guizero import App, Text, TextBox

app = App(title = 'Colour Chooser')

def update_colour():
    colour.bg = colour.value

colour = TextBox(app, text = "",
              width = 20,
              )
colour.when_key_released = update_colour

app.display()