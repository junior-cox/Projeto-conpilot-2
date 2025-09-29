from datetime import datetime
import os

def atu():
    data=datetime.now()
    datadehoje=data.strftime("%d%m%y")#data de hoje
    if os.path.exists(datadehoje):
       print('-------esta ok --------')
       with open(datadehoje,'r') as arquivo:
          r=arquivo.read()
          return r
    else:
        return "nao a tarefa hoje"