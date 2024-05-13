from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class Calculator(App):
    def build(self):
        self.equation = ""
        layout = BoxLayout(orientation='vertical')

        # Adicionando o rótulo para exibir a equação
        self.label = Label(text=self.equation, size_hint=(1, 0.75))
        layout.add_widget(self.label)

        # Criando o layout da grade para os botões
        button_layout = GridLayout(cols=4, size_hint=(1, 2))

        # Definindo os textos dos botões e adicionando os botões ao layout da grade
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', 'X',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        for button in buttons:
            btn = Button(text=button)
            btn.bind(on_press=self.on_button_press)  # Ligando o evento de pressionar botão
            button_layout.add_widget(btn)

        # Adicionando o layout dos botões ao layout principal
        layout.add_widget(button_layout)
        return layout 

    def on_button_press(self, instance):
        button_text = instance.text

        if button_text == '=':
            try:
                result = str(eval(self.equation))
                self.equation = result
            except Exception as e:
                self.equation = "Error"
        elif button_text == 'C':
            self.equation = ""
        else:
            self.equation += button_text

        self.label.text = self.equation

if __name__ == '__main__':
    Calculator().run()
