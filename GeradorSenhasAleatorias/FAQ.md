# ❓ FAQ – Gerador de Senhas Aleatórias 🔐

Este documento reúne perguntas e respostas comuns sobre o projeto, sua estrutura e funcionamento.

---

## 1. Qual o objetivo do projeto?
Facilitar a criação de senhas seguras e personalizadas, com uma interface simples e acessível.  
O usuário pode gerar senhas aleatórias escolhendo tamanho e tipos de caracteres (letras, números, símbolos).

---

## 2. Como está estruturado o código?
O projeto está dividido em três arquivos principais:
- **`gerador.py`** → contém a função que gera a senha.
- **`gui.py`** → implementa a interface gráfica com Tkinter.
- **`main.py`** → ponto de entrada que inicia a interface.

Além disso:
- **`README.md`** → documentação principal.
- **`requirements.txt`** → dependências do projeto.
- **`.gitignore`** → arquivos ignorados no Git.
- **`.venv/`** → ambiente virtual (não versionado).

---

## 3. Quais tecnologias foram usadas?
- **Python** como linguagem principal.  
- **Tkinter** para a interface gráfica.  
- **Pyperclip** para copiar senhas para a área de transferência.

---

## 4. Como o usuário interage com o programa?
Existem duas formas:
- **Interface Gráfica (GUI)** → o usuário escolhe opções em uma janela e clica em botões.  
- **Terminal (CLI)** → o usuário responde perguntas no console para gerar a senha.

---

## 5. Você usou controle de versão?
Sim. O projeto está preparado para Git e GitHub, com `.gitignore` configurado para evitar arquivos desnecessários ou sensíveis.

---

## 6. Como instalar e rodar?
1. Criar e ativar ambiente virtual:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1   # no PowerShell