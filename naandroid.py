from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
#create class клеточной разметки
class grid_L(GridLayout):
    #конструктор
    def __init__(self, **kwargs):
        # тоже конструктор
        super(grid_L, self).__init__(**kwargs)
        #поле для того чтобы задать количествр рядов. данное поле в родительском классе имеет значение 1, поэтому его нужно обязательно поменять
        self.cols = 2
        
        self.add_widget(Label(text='name: '))
        # мултилайн с значением False блокирует многострочие оставляя только одну строку, в случае True имеется адаптивные строки
        
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        
        self.add_widget(Label(text='favorit lesson: '))
        self.lesson = TextInput(multiline=False)
        self.add_widget(self.lesson)

        self.add_widget(Label(text='job?: '))
        self.job = TextInput(multiline=False)
        self.add_widget(self.job)
        
        #create submit button
        
        self.submit = Button(text= 'отправить', font_size = 32)
        #Bind button
        self.submit.bind(on_press= self.press)
        self.add_widget(self.submit)
        
    def press(self, instatce):
        name = self.name.text
        lesson = self.lesson.text
        job = self.job.text

        text =f"Hello {name}, yot favorit lesson {lesson}?, WOW, {job}"
        
        self.add_widget(Label(text=f"{text}"))

        
class Myapp(App):
    def build(self):
        return grid_L()
    
if __name__ == '__main__':
    Myapp().run()