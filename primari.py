import tkinter as Tk
import os
import atu
import seletor
from datetime import datetime

tarefa=atu.atu()

data=datetime.now()
datadehoje=data.strftime("%d.%m")#data de hoje 
print(tarefa)

arquivos="tarefas.txt" 
if os.path.exists(arquivos):
    print('-------esta ok --------')
def taredodia():
    tarefadatela.config(text=tarefa)
def prodia():
    print()
tela=Tk.Tk()
tela.geometry('500x500')
tela.resizable(False,False)
tela.title('tarefas')
tela.after(1000,taredodia)
# conf do da tela do app

tar = Tk.Label(tela, text='tarefas de hoje', font=("Arial", 14), fg="green")
tar.place(x=200,y=10)

dia = Tk.Label(tela, text=datadehoje, font=("Arial", 14), fg="green")
dia.place(x=10, y=470)

#aqui fica as terefas na tela

tarefadatela=Tk.Label(tela,text='nao tem tarefa hoje',font=("arial",20))
tarefadatela.place(x=10,y=60)


direita = Tk.Button(tela, text=">")
direita.place(x=300, y=467)

esquerda = Tk.Button(tela, text="<")
esquerda.place(x=200, y=467)

botao_adiciona = Tk.Button(tela, text="Adicionar Tarefa",command=seletor.selecione)
botao_adiciona.place(x=380, y=468)

tela.mainloop()
#obrigado por ler 