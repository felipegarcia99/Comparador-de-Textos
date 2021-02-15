from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.uix.screenmanager import *
import random

Config.set('graphics', 'width', '1080')
Config.set('graphics', 'height', '600')

# root = Builder.load_file('COMPARADOR_DE_TEXTOS.kv')

a = open('COMPARADOR_DE_TEXTOS.kv', 'r')
kv_string = a.read()
a.close()

root = Builder.load_string(kv_string)


texto1_geral = StringProperty()
texto2_geral = StringProperty()

texto1_geral_modificado = StringProperty('')
texto2_geral_modificado = StringProperty('')

contador_diferencas = 0

change_tela2 = False
comparacao_textos = None


class BLayout(BoxLayout, Screen):
    texto_label_titulo = StringProperty('Insira os textos que você deseja comparar:')
    text_caixa1 = StringProperty()
    text_caixa2 = StringProperty()
    hint_caixa1 = StringProperty()
    hint_caixa2 = StringProperty()

    def __init__(self, **kwargs):
        # super(BoxLayout, self).__init__(**kwargs)
        super().__init__(**kwargs)
        self.hint_caixa1 = self.hint_aleatorio()
        self.hint_caixa2 = self.hint_aleatorio()

    def print_txt(self):
        a = self.text_caixa1
        b = self.text_caixa2
        global texto1_geral
        global texto2_geral
        texto1_geral = a
        texto2_geral = b
        '''print(a)
        print('texto1_geral: ', texto1_geral)  # FUNCIONA!!!!
        print(b)
        print('texto2_geral: ', texto2_geral)'''
        # print(type(self.text_caixa1))
        # print(type(texto1_geral))

    def hint_aleatorio(self):
        hint1 = 'Ex.: abcde'
        hint2 = 'Ex.: A amizade desenvolve a felicidade e reduz o sofrimento, duplicando a nossa alegria e dividindo a nossa dor.'
        hint3 = 'Ex.: Acreditar é essencial, mas ter atitude é o que faz a diferença.'

        list = [hint1, hint2, hint3]
        select = random.choice(list)
        return select

    def abrir_PopupAnalise(self):
        pop = PopupAnalise()
        pop.open()


    class Botao_comparar(Button):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def on_press(self):
            global change_tela2
            change_tela2 = True
            global texto1_geral, texto2_geral
            global comparacao_textos

            if texto1_geral == texto2_geral:
                # TEXTOS IGUAIS
                comparacao_textos = True
            else:
                # TEXTOS DIFERENTES
                comparacao_textos = False


            if comparacao_textos == False:
                a = texto1_geral.split()
                b = texto2_geral.split()

                # print(a)
                # print(b)

                cont3 = 0
                ch = ''
                a4 = []
                for i in a:
                    ch = a[cont3]
                    for j in ch:
                        a4.append(j)
                    ch = ''
                    cont3 = cont3 + 1
                    a4.append(' ')
                # print(a4)

                cont3 = 0
                ch = ''
                b4 = []
                for i in b:
                    ch = b[cont3]
                    for j in ch:
                        b4.append(j)
                    ch = ''
                    cont3 = cont3 + 1
                    b4.append(' ')
                # print(b4)


                global texto1_geral_modificado, texto2_geral_modificado, contador_diferencas
                str1 = ''
                str2 = ''
                cont_dif = 0

                # cor_1_vermelho = '[color=FF6347]'  # Tomato
                cor_1_vermelho = '[color=FF8C00]'  # DarkOrange
                # cor_2_azul = '[color=0000CD]'  # MediumBlue
                cor_2_azul = '[color=00BFFF]'  # DeepSkyBlue
                cor_final = '[/color]'

                # print(len(a4))
                # print(len(b4))
                if len(a4) > len(b4):
                    for i in range(len(b4) + 1, len(a4) + 1):
                        b4.append('')

                    # print(len(b4))

                    for i in range(len(a4)):
                        if a4[i] == b4[i]:
                            # COR NORMAL
                            str1 = str1 + a4[i]
                            str2 = str2 + b4[i]

                        else:
                            # COR DIFERENTE
                            str1 = str1 + cor_1_vermelho + a4[i] + cor_final
                            str2 = str2 + cor_2_azul + b4[i] + cor_final
                            cont_dif = cont_dif + 1
                        # print(i)

                elif len(a4) < len(b4):
                    for i in range(len(a4) + 1, len(b4) + 1):
                        a4.append('')

                    for i in range(len(b4)):
                        if a4[i] == b4[i]:
                            # COR NORMAL
                            str1 = str1 + a4[i]
                            str2 = str2 + b4[i]

                        else:
                            # COR DIFERENTE
                            str1 = str1 + cor_1_vermelho + a4[i] + cor_final
                            str2 = str2 + cor_2_azul + b4[i] + cor_final
                            cont_dif = cont_dif + 1

                else:
                    for i in range(len(a4)):
                        if a4[i] == b4[i]:
                            # COR NORMAL
                            str1 = str1 + a4[i]
                            str2 = str2 + b4[i]

                        else:
                            # COR DIFERENTE
                            str1 = str1 + cor_1_vermelho + a4[i] + cor_final
                            str2 = str2 + cor_2_azul + b4[i] + cor_final
                            cont_dif = cont_dif + 1

                # print(str1)
                # print(str2)
                texto1_geral_modificado = str1
                texto2_geral_modificado = str2
                contador_diferencas = cont_dif

            else:
                texto1_geral_modificado = texto1_geral
                texto2_geral_modificado = texto2_geral



    class Label_Autoria(Label):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.text = 'Autor: Felipe Garcia \nGraduando em Eng. da Computação'


# Bl = BLayout()

class LabeisLayout(BoxLayout, Screen):
    texto_Label1 = StringProperty()
    texto_Label2 = StringProperty()

    def __init__(self, **kwargs):
        # super(BoxLayout, self).__init__(**kwargs)
        super().__init__(**kwargs)
        # self.texto_Label1 = BLayout.text_caixa1
        # self.texto_Label1 = Bl.text_caixa1
        # self.texto_Label1 = texto1_geral

    def print_txt2(self):
        self.texto_Label1 = texto1_geral
        self.texto_Label2 = texto2_geral
        '''print(self.texto_Label1)
        print(self.texto_Label2)'''

    '''def on_pre_enter(self, *args):
        # self.texto_Label1 = texto1_geral
        global change_tela2
        change_tela2 = True'''

    class Label_texto_1(Label):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            Clock.schedule_interval(lambda dt: self.mudar_label(), 0.5)
            # print('self.size', self.size)

        def mudar_label(self):
            global change_tela2
            if change_tela2 == True:
                # self.text = texto1_geral
                self.text = texto1_geral_modificado

    class Label_texto_2(Label):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            Clock.schedule_interval(lambda dt: self.mudar_label(), 0.5)

        def mudar_label(self):
            global change_tela2
            if change_tela2 == True:
                # self.text = texto2_geral
                self.text = texto2_geral_modificado


class PopupAnalise(Popup):
    # texto_popup_titulo = StringProperty('Análise Concluida')
    texto_popup_titulo = StringProperty()
    texto_popup_corpo = StringProperty()

    def __init__(self, **kwargs):
        super(Popup, self).__init__(**kwargs)
        Clock.schedule_interval(lambda dt: self.checar_igualdade_textos(), 0.5)

    def checar_igualdade_textos(self):
        global comparacao_textos
        if comparacao_textos == True:
            self.texto_popup_titulo = 'Textos iguais'
            self.texto_popup_corpo = 'Nao foram encontradas diferenças'
        elif comparacao_textos == False:
            self.texto_popup_titulo = 'Textos diferentes'
            if contador_diferencas == 1:
                self.texto_popup_corpo = 'Foi encontrada ' + '[color=FF00FF]' + str(contador_diferencas) + '[/color]' + ' diferença'
            else:
                self.texto_popup_corpo = 'Foram encontradas ' + '[color=FF00FF]' + str(contador_diferencas) + '[/color]' + ' diferenças'


'''class PopupCopia1(Popup):
    pass


class PopupCopia2(Popup):
    pass'''


Sm = ScreenManager()
Sm.add_widget(BLayout(name='tela1'))
Sm.add_widget(LabeisLayout(name='tela2'))
# Sm.transition = NoTransition()
# Sm.transition = SwapTransition()
Sm.transition = FadeTransition()


class teste16(App):
    def build(self):
        self.icon = 'Ícone_comparador_textos2.png'
        self.title = 'Comparador de Textos'
        return Sm


if __name__ == '__main__':
    teste16().run()
