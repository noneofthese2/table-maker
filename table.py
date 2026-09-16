from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class TableApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.number = TextInput(
            hint_text="Enter a number",
            input_filter="int"
        )

        button = Button(
            text="Show Table"
        )

        self.result = Label(
            text="Enter a number above"
        )

        button.bind(on_press=self.show_table)

        layout.add_widget(self.number)
        layout.add_widget(button)
        layout.add_widget(self.result)

        return layout

    def show_table(self, instance):
        number = int(self.number.text)

        table = ""

        for i in range(1, 11):
            table += f"{number} x {i} = {number * i}\n"

        self.result.text = table


TableApp().run()
