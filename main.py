from kivymd.app import MDApp
from kivymd.uix.card import MDCard
#from kivymd.uix.floatlayout import FloatLayout
from kivy.lang import Builder 
from kivy.uix.screenmanager import Screen, ScreenManager

class GerenciadorTelas(ScreenManager):
    pass

class Tela(Screen):
    pass

class TelaCadastro(Screen):
    pass



#class SenhaCard(MDCard):
  #  def fechar(self):
   #     self.parent.remove_widget(self)


class TelaLogin(Screen):
   pass


class Login(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.primary_hue = '700'

        return Builder.load_file('main.kv')

        

Login().run()