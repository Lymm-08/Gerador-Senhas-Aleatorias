```markdown
# Gerador de Senhas Aleatórias 🔐

Projeto em Python para gerar senhas aleatórias personalizadas.  
Agora com **interface gráfica (Tkinter)** e também opção de uso no **terminal (CLI)**.

---

## ✨ Funcionalidades
- Escolher tamanho da senha
- Incluir letras, números e símbolos
- Salvar senhas em arquivo `.txt`
- Histórico de senhas geradas
- Copiar senha para área de transferência

---

## 🚀 Como rodar

### 1. Criar e ativar ambiente virtual
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # no PowerShell
```

### 2. Instalar dependências
```bash
pip install pyperclip
```

### 3. Executar programa
```bash
python main.py
```
## 🎞️ Demonstração

![Demonstração do programa](imagens/demo.gif.gif)
---

## 📊 Exemplo de uso (Interface Gráfica)
1. Digite o tamanho da senha.  
2. Marque se quer letras, números e símbolos.  
3. Clique em **Gerar Senha**.  
4. Use os botões para salvar, copiar ou ver histórico.  

---

## 📟 Exemplo de uso (Terminal/CLI)
```
=== Gerador de Senhas Aleatórias ===
Digite o tamanho da senha: 12
Incluir letras? (s/n): s
Incluir números? (s/n): s
Incluir símbolos? (s/n): n

Sua senha gerada é:
a9BfK2LmQwXz
```

---

## 🔮 Próximos Passos
- Melhorar interface gráfica (cores, estilos, responsividade).
- Adicionar opção de escolher onde salvar o arquivo.
- Criar versão com PyQt para interface mais avançada.
- Implementar exportação de senhas em diferentes formatos (JSON, CSV).
```