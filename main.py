from tarefa import Tarefa
from persistencia import carregar_tarefas, salvar_tarefas

tarefa1 = Tarefa("titulo1","descricao1","15/08/2023",)

salvar_tarefas([tarefa1])

tarefas = carregar_tarefas()
print(tarefas[0].detalhes())