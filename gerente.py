def coletar(data,hora,tarefa):
      data=data
      with open(data,'a') as f:
         f.write(tarefa+hora) 
         return print(tarefa+hora)
