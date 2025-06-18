<div align="center">
  <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/server.svg" alt="Ícone de servidor" width="80"/>
  <h1>ZenMotion - Backend</h1>
  <p>API RESTful robusta que serve como o cérebro e a base de dados para a plataforma ZenMotion.</p>

  <p>
    <img src="https://img.shields.io/badge/Tecnologia-Python-blue?logo=python" alt="Python">
    <img src="https://img.shields.io/badge/Framework-Django-darkgreen?logo=django" alt="Django">
    <img src="https://img.shields.io/badge/API-REST-orange" alt="API REST">
    <img src="https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite" alt="SQLite">
    <img src="https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow" alt="Status">
  </p>
</div>

---

## 🎯 Sobre o Projeto

Este repositório contém o código-fonte do **backend** da plataforma **ZenMotion**. Ele foi desenvolvido em Python utilizando o framework Django e o Django REST Framework para criar uma API RESTful segura e eficiente.

Esta API é responsável por toda a lógica de negócio, incluindo:
* Gerenciamento e autenticação de usuários (via JWT).
* Operações de CRUD (Criar, Ler, Atualizar, Deletar) para refeições, exercícios e metas.
* Armazenamento e recuperação de todos os dados do aplicativo.

Este backend foi projetado para ser consumido pelo [frontend do ZenMotion](https://github.com/zenmotion/backend).

---

## 👨‍💻 Autores

**[Daniel Lucas dos Santos Corte - 202403517949]** - [daniellcorte@gmail.com](mailto:daniellcorte@gmail.com) <br>
**[Julio Alexsandro Monteiro da Silva - 202403945487]** - [daniellcorte@gmail.com](mailto:daniellcorte@gmail.com)

---

## 🚀 Tecnologias Utilizadas

* **Python 3**
* **Django 5**
* **Django REST Framework**
* **djangorestframework-simplejwt** (Para autenticação com JSON Web Tokens)
* **django-cors-headers** (Para permitir requisições do frontend)
* **SQLite3** (Banco de dados padrão para desenvolvimento)

---

## 🏁 Começando

Siga estas instruções para configurar e executar o servidor da API em sua máquina local.

### Pré-requisitos

* [**Python**](https://www.python.org/downloads/) instalado em seu sistema.

### Instalação e Execução

1.  **Clone este repositório:**
    ```bash
    git clone https://github.com/zenmotion/backend.git
    cd backend
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente virtual
    py -m venv env

    # Ativar o ambiente virtual (Windows)
    .\env\Scripts\activate
    ```
    *No Linux/macOS, o comando de ativação é `source env/bin/activate`.*

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    *Este passo é essencial para criar as tabelas no banco de dados.*
    ```bash
    py manage.py migrate
    ```

5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    py manage.py runserver
    ```

🎉 **Pronto!** O servidor da API do ZenMotion estará rodando em `http://127.0.0.1:8000/`.


