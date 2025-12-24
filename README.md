# 🔐 Sistema de Login e Cadastro em Python

Este projeto é um **sistema de autenticação em Python**, executado via terminal, que permite **cadastro de usuários, login e recuperação de senha**, utilizando **arquivo JSON como base de dados**.

Foi desenvolvido com foco em **lógica de programação**, **validação de dados** e **persistência simples**, sendo ideal para compor um **portfólio no GitHub**.

---

## 🚀 Funcionalidades

- ✅ Cadastro de usuários  
- 🔑 Login com usuário e senha  
- 🔁 Recuperação de senha com código de verificação  
- 📧 Validação de e-mail com domínios permitidos  
- 💾 Persistência de dados em arquivo JSON  
- 🔒 Máscara de senha no terminal  
- ❌ Prevenção de usuários e e-mails duplicados  

---

## 🗂️ Estrutura do Projeto

```
📁 projeto-login
 ├── main.py
 ├── banco.json
 └── README.md
```

- `main.py` → código principal do sistema  
- `banco.json` → arquivo onde os usuários são armazenados  
- `README.md` → documentação do projeto  

---

## 🧠 Como funciona

- Os usuários são salvos no arquivo `banco.json`
- Cada usuário possui:
  - usuário
  - e-mail
  - senha
- O sistema valida:
  - domínio de e-mail
  - tamanho mínimo de usuário e senha
  - duplicidade de dados
- Na recuperação de senha, um **código aleatório de 6 dígitos** é gerado para validação

⚠️ *O envio do código por e-mail é apenas simulado (modo debug).*

---

## 🖥️ Menu Principal

```
1 ➜ Fazer Login
2 ➜ Fazer Cadastro
3 ➜ Esqueci a Senha
0 ➜ Sair
```

---

## ▶️ Como executar o projeto

1. Certifique-se de ter o **Python 3** instalado  
2. Clone o repositório ou baixe os arquivos  
3. Execute no terminal:

```
python main.py
```

O arquivo `banco.json` será criado automaticamente se não existir.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- JSON
- Manipulação de arquivos
- Estruturas de decisão e repetição
- Funções
- Validação de dados

---

## 📌 Possíveis melhorias futuras

- 🔐 Criptografia de senhas (hash)
- 📧 Envio real de e-mail
- 🧑‍💻 Sistema de perfil do usuário
- 🗄️ Integração com banco de dados
- 🌐 Interface gráfica ou web

---

## 👨‍💻 Autor

**Erlon Andrade**  
Estudante de Análise e Desenvolvimento de Sistemas  
Projeto desenvolvido para fins educacionais e portfólio.
