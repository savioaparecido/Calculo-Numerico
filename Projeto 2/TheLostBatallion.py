import tkinter as tk
import numpy as np

class Janela:
    def __init__(self, Tk):
        Tk.resizable(width = False, height = False)
        self.top = tk.Toplevel(Tk)
        self.top.lift()
        self.top.resizable(width= False, height = False)
        self.top.title('The Lost Battalion')
        self.msg1 = tk.Message(self.top, text='Seja Bem-Vindo ao Simulador de Projétil The Lost Battalion!',
                               font=('Times New Roman', 14))
        self.msg1.pack()
        self.msg2 = tk.Message(self.top, text='Utilizando Cálculo Numérico, este programa calcula,'
                                              'com dois pontos de entrada mais a origem, um '
                                              'polinômio interpolador. Este polinômio, comparado a '
                                              'equação da trajetória, determina o ângulo e a velocidade '
                                              'inicial do projétil', font=('Times New Roman', 12))
        self.msg2.pack()
        self.bttop = tk.Button(self.top, text='Vamos Começar?', font=('Times New Roman', 12, 'bold'),
                               command=self.top.destroy)
        self.bttop.pack()
        self.frame1 = tk.Frame(Tk)
        self.frame1.pack(pady = 5)
        self.frame2 = tk.Frame(Tk)
        self.frame2.pack(pady = 5)
        self.frame3 = tk.Frame(Tk)
        self.frame3.pack(pady = 5)
        self.frame4 = tk.Frame(Tk)
        self.frame4.pack(pady = 5)
        self.frame5 = tk.Frame(Tk)
        self.frame5.pack(pady = 5)
        self.frame6 = tk.Frame(Tk)
        self.frame6.pack(pady = 5)
        self.frame7 = tk.Frame(Tk)
        self.frame7.pack(pady = 5)
        self.frame8 = tk.Frame(Tk)
        self.frame8.pack(pady = 5)
        self.frame9 = tk.Frame(Tk)
        self.frame9.pack(pady = 5)
        self.frame10 = tk.Frame(Tk)
        self.frame10.pack(pady = 5)
        self.frame11 = tk.Frame(Tk)
        self.frame11.pack(pady = 5)

        self.label1 = tk.Label(self.frame1, text = 'The Lost Battalion \nSimulador de Foguetes utilizando Cálculo Numérico',
                               font = ('Times New Roman', 16, 'bold'), height = 3)
        self.label1.pack()

        self.label2 = tk.Label(self.frame2, text = 'Informe as coordenadas de dois pontos da trajetória do projétil:',
                               font = ('Times New Roman', 14))
        self.label2.pack()

        self.label3 = tk.Label(self.frame3, text = 'Abscissa (X): ', font = ('Times New Roman', 12))
        self.label4 = tk.Label(self.frame4, text = 'Ordenada (Y): ', font = ('Times New Roman', 12))
        self.label3.pack(side = tk.LEFT, padx = 5)
        self.label4.pack(side = tk.LEFT, padx = 5)
        self.entry1x = tk.Entry(self.frame3, width = 5, font = ('Times New Roman', 12))
        self.entry1x.pack(side = tk.LEFT, padx = 5)
        self.entry1x.focus_force()
        self.entry2x = tk.Entry(self.frame3, width = 5, font = ('Times New Roman', 12))
        self.entry2x.pack(side = tk.LEFT, padx = 5)
        self.entry1y = tk.Entry(self.frame4, width = 5, font = ('Times New Roman', 12))
        self.entry1y.pack(side = tk.LEFT, padx = 5)
        self.entry2y = tk.Entry(self.frame4, width = 5, font = ('Times New Roman', 12))
        self.entry2y.pack(side = tk.LEFT, padx = 5)

        self.bt1 = tk.Button(self.frame5, text = 'Calcular', font = ('Times New Roman', 14), fg = 'white', bg = 'red',
                             command = self.calcular)
        self.bt1.pack(side = tk.LEFT, pady = 5)

    def calcular(self):
        self.x1 = float(self.entry1x.get())
        self.x2 = float(self.entry2x.get())
        self.y1 = float(self.entry1y.get())
        self.y2 = float(self.entry2y.get())

        if self.x1 <= 0:
            pass
        elif (self.x2 <= 0) or (self.x2 == self.x1):
            pass
        elif self.y1 <= 0:
            pass
        elif (self.y2 <= 0) or (self.y2 == self.y1):
            pass
        else:
            self.a = self.y1/self.x1
            self.b = (self.y2-self.y1)/(self.x2-self.x1)

            self.c = (self.b - self.a)/self.x2

            self.a2 = self.c
            self.a1 = self.a - (self.c*self.x1)

            self.ang = np.arctan(self.a1)
            self.numerador = -9.81
            self.denominador = 2*self.a2*((np.cos(self.ang))**2)
            self.vo = np.sqrt(self.numerador/self.denominador)
            self.label5 = tk.Label(self.frame6, text = f'O Polinômio Interpolador da Trajetória é : {self.a2:.2f}x²+({self.a1:.2f})x',
                                   font = ('Times New Roman', 14))
            self.label5.pack()
            self.label6 = tk.Label(self.frame7, text = f'O ângulo da trajetória é de: {np.degrees(self.ang):.2f}°',
                                   font = ('Times New Roman', 14))
            self.label7 = tk.Label(self.frame8, text = f'A velocidade inicial do foguete é de: {self.vo:.2f} m/s',
                                   font = ('Times New Roman', 14))
            self.label6.pack()
            self.label7.pack()

            self.label8 = tk.Label(self.frame9, text = 'Informe um ponto x qualquer da trajetória:', font = ('Times New Roman', 14))
            self.label8.pack(side = tk.LEFT)
            self.entryx = tk.Entry(self.frame9, font = ('Times New Roman', 12))
            self.entryx.pack(side = tk.LEFT)
            self.bt2 = tk.Button(self.frame10, text = 'Calcular', font = ('Times New Roman', 14), fg = 'white', bg = 'red',
                                 command = self.calcular2)
            self.bt2.pack(pady = 5)
            self.bt1['command'] = self.bloquear

    def calcular2(self):
        self.x = float(self.entryx.get())
        if (self.x < 0) or (self.x > (-self.a1/self.a2)):
            pass
        else:
            self.y = (self.a2*((self.x)**2)) + (self.a1*self.x)
            self.label9 = tk.Label(self.frame11, text = f'A altitude no ponto {self.x} m é de {self.y} m',
                                   font = ('Times New Roman', 14))
            self.label9.pack()
            self.bt2['command'] = self.bloquear
    def bloquear(self):
        pass
raiz = tk.Tk()
raiz.lower()
janela = Janela(raiz)
raiz.title('The Lost Battalion - Simulador de Projéteis')
raiz.mainloop()