
# 🌐 CW-IA

**CW-IA** é um projeto de inteligência artificial para previsão de risco de desastres, utilizando dados históricos e técnicas de machine learning. Ele combina um backend Python/Flask com um frontend simples em HTML para consulta de previsões.

## 📦 Pré-requisitos

Antes de rodar o projeto, certifique-se de ter:

- Python 3.11+
- VSCode (recomendado)
- Extensões do VSCode:
  - **Jupyter**
  - **Live Server**

## 📑 Instruções de Uso

### 📊 Treinar o modelo

Para gerar o modelo de previsão:

1. Abra o VSCode.
2. Certifique-se de ter a extensão **Jupyter** instalada.
3. Execute o notebook:

```
notebooks/GS12025.ipynb
```

Este notebook carrega os dados, treina o modelo e salva o arquivo `modelo.pkl` para uso no backend.

---

### 🚀 Rodar o Backend

Para iniciar o servidor backend:

1. Navegue até a pasta `app/`.
2. Execute o script `run.bat`:

```
app/run.bat
```

O backend será iniciado e ficará ouvindo as requisições.

---

### 🌐 Rodar o Frontend

Para visualizar a interface de consulta:

1. Abra o arquivo:

```
frontend/pages/home.html
```

2. Clique com o botão direito e escolha **Open with Live Server** (ou utilize a extensão **Live Server** no VSCode).

A página permitirá ao usuário informar os dados de um desastre e consultar a previsão de nível de risco.
---

## 📌 Observação

Não se esqueça de rodar o notebook sempre que atualizar os dados ou quiser treinar um novo modelo.

---

🚀 Projeto desenvolvido para fins acadêmicos.
