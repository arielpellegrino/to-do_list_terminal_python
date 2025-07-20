import pickle
import os

def salvar_tarefas(tarefas, nome_arquivo="tarefas.pkl"):
    diretorio = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)
    with open(caminho_arquivo, "wb") as arquivo:
        pickle.dump(tarefas, arquivo)
    print(f"Tarefas salvas em '{caminho_arquivo}' com sucesso!")

def carregar_tarefas(nome_arquivo="tarefas.pkl"):
    diretorio = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)
    try:
        with open(caminho_arquivo, "rb") as arquivo:
            tarefas = pickle.load(arquivo)
            print(f"Tarefas carregadas de '{caminho_arquivo}' com sucesso")
            return tarefas
    except FileNotFoundError:
        print(f"Arquivo '{caminho_arquivo}' não encontrado. Nenhuma tarefa foi carregada")
        return []
    except EOFError:
        print(f"O arquivo '{caminho_arquivo}' está vazio. Nenhuma tarefa foi carregada.")
        return []