import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self,**kwargs):
        super(childApp,self).__init__()
        self.cols=2

        self.add_widget(Label(text='Nom et Prenom'))
        self.nom=TextInput()
        self.add_widget(self.nom)

        self.add_widget(Label(text='Genre'))
        self.sexe=TextInput()
        self.add_widget(self.sexe)

        self.add_widget(Label(text='Age'))
        self.age=TextInput()
        self.add_widget(self.age)

        self.add_widget(Label(text='Adresse'))
        self.adresse=TextInput()
        self.add_widget(self.adresse) 

        self.add_widget(Label(text='Metier'))
        self.metier=TextInput()
        self.add_widget(self.metier) 

        self.press=Button(text='Save')
        self.press.bind(on_press=self.save)
        self.add_widget(self.press)

    def save(self, instance):
         print('Nom et Prenom :' +self.nom.text)
         print('Genre:' +self.sexe.text)
         print('Age :' +self.age.text)
         print('Adresse:' +self.adresse.text)
         print('Metier :' +self.metier.text)
         print('')
class parentApp(App):
 def build(self):
    return childApp()
if __name__ =='__main__':
   parentApp().run()
