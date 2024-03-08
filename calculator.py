from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield import MDTextField

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDTextField:
        id: display
        font_size: '32sp'
        multiline: False
        halign: 'right'
        readonly: True
        padding_x: 20
        padding_y: 20

    MDGridLayout:
        cols: 4
        adaptive_size: True
        spacing: '5dp'
        padding: '5dp'
        
        MDFillRoundFlatButton:
            text: 'C'
            on_press: app.clear_display()

        MDFillRoundFlatButton:
            text: '±'
            on_press: app.toggle_sign()

        MDFillRoundFlatButton:
            text: '%'
            on_press: app.calculate_modulus()

        MDFillRoundFlatButton:
            text: '/'
            on_press: app.update_display('/')

        MDFillRoundFlatButton:
            text: '7'
            on_press: app.update_display('7')

        MDFillRoundFlatButton:
            text: '8'
            on_press: app.update_display('8')

        MDFillRoundFlatButton:
            text: '9'
            on_press: app.update_display('9')

        MDFillRoundFlatButton:
            text: '*'
            on_press: app.update_display('*')

        MDFillRoundFlatButton:
            text: '4'
            on_press: app.update_display('4')

        MDFillRoundFlatButton:
            text: '5'
            on_press: app.update_display('5')

        MDFillRoundFlatButton:
            text: '6'
            on_press: app.update_display('6')

        MDFillRoundFlatButton:
            text: '-'
            on_press: app.update_display('-')

        MDFillRoundFlatButton:
            text: '1'
            on_press: app.update_display('1')

        MDFillRoundFlatButton:
            text: '2'
            on_press: app.update_display('2')

        MDFillRoundFlatButton:
            text: '3'
            on_press: app.update_display('3')

        MDFillRoundFlatButton:
            text: '+'
            on_press: app.update_display('+')

        MDFillRoundFlatButton:
            text: '.'
            on_press: app.update_display('.')

        MDFillRoundFlatButton:
            text: '0'
            on_press: app.update_display('0')

        MDFillRoundFlatButton:
            text: '='
            on_press: app.calculate_result()
            icon: 'equal'
'''

class CalculatorApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def update_display(self, value):
        current_text = self.root.ids.display.text
        if current_text == 'Error':
            current_text = ''

        if value == 'C':
            self.root.ids.display.text = ''
        elif value == '±':
            self.toggle_sign()
        else:
            self.root.ids.display.text += value

    def clear_display(self):
        self.root.ids.display.text = ''

    def toggle_sign(self):
        current_text = self.root.ids.display.text
        if current_text and current_text[0] == '-':
            self.root.ids.display.text = current_text[1:]
        elif current_text:
            self.root.ids.display.text = '-' + current_text

    def calculate_modulus(self):
        try:
            result = str(eval(self.root.ids.display.text + '/100'))
            self.root.ids.display.text = result
        except Exception as e:
            self.root.ids.display.text = 'Error'

    def calculate_result(self):
        try:
            result = str(eval(self.root.ids.display.text))
            self.root.ids.display.text = result
        except Exception as e:
            self.root.ids.display.text = 'Error'


if __name__ == '__main__':
    CalculatorApp().run()
    