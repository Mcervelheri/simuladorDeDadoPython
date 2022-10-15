import random
import PySimpleGUI as sg

class simuladorDeDado:
    def __init__(self):
        self.valorMínimo = 1
        self.valorMáximo = 6
        self.mensagem = 'você gostaria de gerar um novo valor para o dado? '
        self.layout = [
            [sg.Image(filename='semDado.png',key='output')],
            [sg.Text('Jogar o dado?',key='text')],
            [sg.Button('sim'),sg.Button('não')]
        ]


    
    def iniciar(self):
        self.janela = sg.Window('Simulador de dado',layout=self.layout)
        self.eventos, self.valores = self.janela.Read()  # type: ignore
        try:
            while self.eventos == 'sim' or self.eventos == 's':
                self.gerarValorDoDado()
                self.eventos, self.valores = self.janela.Read()  # type: ignore
            if self.eventos == 'não' or self.eventos == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('ocorreu um erro!!!')

    def gerarValorDoDado(self):
        resultado = int(random.randint(self.valorMínimo,self.valorMáximo))
        dados = ['dado1.png', 'dado2.png', 'dado3.png', 'dado4.png', 'dado5.png', 'dado6.png']
        print(resultado)
        self.janela['output'].update(filename=dados[resultado-1])
        self.janela['text'].update('Jogar dado novamente?')  # type: ignore

simulador = simuladorDeDado()
simulador.iniciar()
