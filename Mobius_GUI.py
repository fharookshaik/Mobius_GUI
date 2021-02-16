from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from mobius import Mobius

class MainWindow(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_btn_click(self):
        try:
            if self.ids.input.text != '':
                num = int(self.ids.input.text)
                print('Captured Number : ',num)
                self.ids.input.text = ''
                op = Mobius(num)
                self.ids.output.text = 'Output:\n\nMobius Value of {} : {} \nExplaination: {}'.format(num,op['val'], op['exp'])


            else:
                print("Input can't be empty")
                self.ids.output.text = "Input can't be empty."
        except Exception as e:
            self.ids.output.text = 'Unexpected Error. Re-run the program.'    

class MobiusApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    MobiusApp().run()