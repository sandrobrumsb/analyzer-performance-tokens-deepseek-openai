# 🤖 📁 Projeto: Analisador de performance de chamadas de APIs DeepSeek & OpenAI.
---

### ⚖️ `Projeto que calcula e compara os custos de uma requisição entre as APIs DEEPSEEK e OPENAI.`

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
git clone https://github.com/sandrobrumsb/analyzer-performance-tokens-deepseek-openai.git
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
