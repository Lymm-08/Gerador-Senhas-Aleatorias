# ============================
# 📂 Importações
# ============================
import tkinter as tk              # Biblioteca para criar interface gráfica
from tkinter import messagebox    # Caixa de mensagens (alertas, avisos, erros)
import pyperclip                  # Biblioteca para copiar texto para a área de transferência
from gerador import gerar_senha   # Função que gera a senha (vem do arquivo gerador.py)

# ============================
# 📂 Variáveis globais
# ============================
historico = []   # Lista para armazenar todas as senhas geradas

# ============================
# 📂 Função: gerar()
# ============================
def gerar(entry_tamanho, var_letras, var_numeros, var_simbolos, entry_resultado):
    """
    Gera uma senha com base nas opções escolhidas e mostra na interface.
    """
    try:
        tamanho = int(entry_tamanho.get())   # Pega o tamanho digitado
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido!")  # Caso não seja número
        return

    # Chama a função gerar_senha() do arquivo gerador.py
    senha = gerar_senha(tamanho, var_letras.get(), var_numeros.get(), var_simbolos.get())

    # Mostra a senha na caixa de texto
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, senha)

    # Adiciona a senha ao histórico
    historico.append(senha)

# ============================
# 📂 Função: salvar()
# ============================
def salvar(entry_resultado):
    """
    Salva a senha atual em um arquivo de texto.
    """
    senha = entry_resultado.get()
    if senha:
        with open("senhas.txt", "a") as f:
            f.write(senha + "\n")
        messagebox.showinfo("Sucesso", "Senha salva em 'senhas.txt'!")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha para salvar.")

# ============================
# 📂 Função: copiar()
# ============================
def copiar(entry_resultado):
    """
    Copia a senha atual para a área de transferência.
    """
    senha = entry_resultado.get()
    if senha:
        pyperclip.copy(senha)
        messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha para copiar.")

# ============================
# 📂 Função: mostrar_historico()
# ============================
def mostrar_historico():
    """
    Mostra todas as senhas geradas até agora.
    """
    if historico:
        messagebox.showinfo("Histórico", "\n".join(historico))
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha gerada ainda.")

# ============================
# 📂 Função: iniciar_gui()
# ============================
def iniciar_gui():
    """
    Cria e inicia a interface gráfica principal.
    """
    root = tk.Tk()
    root.title("Gerador de Senhas Aleatórias 🔐")
    root.geometry("400x300")

    # Entrada para tamanho da senha
    tk.Label(root, text="Tamanho da senha:").pack()
    entry_tamanho = tk.Entry(root)
    entry_tamanho.pack()

    # Checkboxes para opções de caracteres
    var_letras = tk.BooleanVar(value=True)
    var_numeros = tk.BooleanVar(value=True)
    var_simbolos = tk.BooleanVar(value=True)

    tk.Checkbutton(root, text="Incluir Letras", variable=var_letras).pack()
    tk.Checkbutton(root, text="Incluir Números", variable=var_numeros).pack()
    tk.Checkbutton(root, text="Incluir Símbolos", variable=var_simbolos).pack()

    # Caixa para mostrar senha gerada
    tk.Label(root, text="Senha gerada:").pack()
    entry_resultado = tk.Entry(root, width=40)
    entry_resultado.pack()

    # Botões de ação
    tk.Button(root, text="Gerar Senha",
              command=lambda: gerar(entry_tamanho, var_letras, var_numeros, var_simbolos, entry_resultado)).pack(pady=5)
    tk.Button(root, text="Salvar em Arquivo",
              command=lambda: salvar(entry_resultado)).pack(pady=5)
    tk.Button(root, text="Copiar Senha",
              command=lambda: copiar(entry_resultado)).pack(pady=5)
    tk.Button(root, text="Mostrar Histórico",
              command=mostrar_historico).pack(pady=5)

    # Inicia o loop da interface
    root.mainloop()