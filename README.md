# 🤖 Anotações e Comparações de Análises de APIs DeepSeek & OpenAI.
---

## 📁 Projeto:

### ⚖️ `analyzer_performance_tokens_deepseek_openai.py`

**O que ele faz:**  
Compara o comportamento entre as APIs da **DeepSeek** e **OpenAI**, medindo:

- Tokens de entrada (prompt) e saída (resposta)
- Total de tokens utilizados
- Tempo de execução da requisição
- Custo estimado da requisição para cada API

> 💡 Útil para tomada de decisão sobre **eficiência de custo e performance** entre diferentes provedores de LLMs.

---

## 🚀 Como rodar os scripts

Siga os passos abaixo para executar qualquer um dos projetos deste repositório:

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
```
### 2. Instale as 📚 Bibliotecas:
```bash
pip install -r requirements.txt
```
### 3. 📦 Crie o Arquivo `.env`:

- Arquivo `.env` com suas chaves de API:
  ```env
  OPENAI_API_KEY=your_openai_key_here
  DEEPSEEK_API_KEY=your_deepseek_key_here
---