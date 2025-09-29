import tkinter as TK
import gerente

def selecione():
  tdir=TK.Tk()
  tdir.geometry('300x300')
  tdir.title('adicione sua tarefa')
  tdir.resizable(False,False) 

  tar = TK.Label(tdir, text='adiciome sua tarefa aqui', font=("Arial", 14), fg="green")
  tar.place(x=50,y=0)#titulo

  can1=TK.Entry(tdir,width='30')
  can1.place(x=70,y=55)
  
  
  tarefa = TK.Label(tdir, text='tarefa', font=("Arial", 14), fg="green")
  tarefa.place(x=10,y=50)

  escolha1 = TK.StringVar(value="D")
  opcoes1 = ["01", "02", "03","04", "05","06","07","08","09","10","11","12","13","14","15","16", "17", "18","19", "20","21","22","23","24","25","26","27","28","29","30","31"]
  can21 = TK.OptionMenu(tdir,escolha1,*opcoes1)
  can21.place(x=70,y=105)
    
  escolha2 = TK.StringVar(value="M")
  opcoes2 = ["01", "02", "03","04", "05","06","07","08","09","10","11","12"]
  can22 = TK.OptionMenu(tdir, escolha2, *opcoes2)
  can22.place(x=130,y=105)

  escolha3 = TK.StringVar(value="A")
  opcoes3 = ["25", "26", "27"]
  can33 = TK.OptionMenu(tdir, escolha3, *opcoes3)
  can33.place(x=195,y=105)

  diata =TK.Label(tdir,text="data",font=("arial",14),fg="green")
  diata.place(x=10,y=100)
#============================
  can3=TK.Entry(tdir,width='30')
  can3.place(x=70,y=155)

  horat = TK.Label(tdir, text='hora', font=("Arial", 14), fg="green")
  horat.place(x=10,y=150)

  def envira():
     parametro3=can1.get()
     esco1=escolha1.get()
     esco2=escolha2.get()
     esco3=escolha3.get()
     hora=can3.get()
     data=esco1+esco2+esco3
     gerente.coletar(data,hora,parametro3)
     tdir.destroy

  bb=TK.Button(tdir,text='inserir',command=envira)
  bb.place(x=150,y=200)
  tdir.mainloop()