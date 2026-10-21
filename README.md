# Projeto Flask - Olá, Mundo!

## Sobre o projeto

Esse projeto foi feito durante a aula de Python, com o objetivo de conhecer um pouco do Flask e entender como funciona a criação de páginas web usando Python.

Começamos acessando o ambiente Python criado na aula anterior. Depois, instalamos o UV pelo terminal, usamos alguns comandos para configurar o projeto e instalamos o Flask.

## O que foi feito

Durante a aula, criamos algumas rotas para testar o funcionamento do Flask:

- `/` mostra uma mensagem de "Olá, Mundo!".
- `/pessoa?nome=SeuNome` recebe um nome pela URL e mostra uma saudação.
- `/usuario/SeuNome` exibe o nome informado no endereço.
- `/ola/` e `/ola/SeuNome` mostram uma página HTML usando templates.

Também criamos o arquivo `ola.html`, que permite exibir uma saudação personalizada ou uma mensagem padrão, dependendo do nome informado.

Depois de testar a aplicação usando o comando `uv run flask run`, criamos um repositório no GitHub para guardar e compartilhar os arquivos do projeto.

## Tecnologias utilizadas

- Python
- UV
- Flask
- HTML
- Git e GitHub

## Como executar

Depois de clonar o repositório e entrar na pasta do projeto, execute o seguinte comando no terminal:

```bash
uv run flask run
```

Em seguida, acesse o endereço indicado no terminal, geralmente `http://127.0.0.1:5000`.

## Conclusão

Essa atividade foi uma introdução ao Flask. Com ela, pude aprender na prática como criar rotas, receber informações pela URL, exibir páginas HTML e utilizar templates. Também tive contato com o UV para gerenciar o projeto e com o GitHub para armazenar o código.

Projeto desenvolvido durante a aula para fins de aprendizado.