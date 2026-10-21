Projeto Flask - Olá, Mundo!

Sobre o projeto

Esse projeto foi desenvolvido durante a aula de Python, onde começamos a conhecer o Flask e entender como ele funciona na criação de aplicações web.

Primeiro, acessamos o ambiente Python criado na aula anterior e instalamos o UV pelo terminal. Depois, utilizamos alguns comandos para configurar o projeto, instalar o Flask e começar a desenvolver nossa aplicação.

O que usamos

- Python: linguagem utilizada no projeto.
- UV: ferramenta para gerenciar o ambiente e as dependências do Python.
- Flask: utilizado para criar as rotas da aplicação.
- HTML: utilizado para estruturar a página exibida no navegador.
- Git e GitHub: para armazenar e compartilhar o projeto.

O que aprendemos

Durante a aula, criamos algumas rotas para entender como o Flask funciona. Começamos com a mensagem "Olá, Mundo!", depois aprendemos a receber nomes pela URL e exibir saudações personalizadas.

Também vimos como utilizar o "render_template()" para carregar um arquivo HTML separado do código Python. No arquivo "ola.html", criamos uma condição para mostrar o nome informado ou exibir uma mensagem padrão quando nenhum nome é passado.

Um exemplo do que fizemos foi criar uma rota simples:

@app.route("/")
def ola_mundo():
    return '<p>Olá, Mundo!</p>'

Com poucas linhas, conseguimos criar uma página que responde quando alguém acessa o endereço inicial da aplicação.

Comandos utilizados

Para verificar as versões das ferramentas:

uv --version
python --version

Para iniciar o projeto e preparar o ambiente:

uv init
uv venv
uv sync

Para instalar o Flask:

uv add flask

E, para executar a aplicação:

uv run flask run

Depois, acessamos "http://127.0.0.1:5000" no navegador para testar as rotas.

Publicando o projeto

Depois de testar a aplicação localmente, criamos um repositório no GitHub para guardar os arquivos e compartilhar o projeto.

Conclusão

Essa aula foi meu primeiro contato prático com o Flask. Aprendi a criar rotas, receber informações pela URL, trabalhar com arquivos HTML e utilizar o UV para preparar o ambiente do projeto. Também conheci um pouco mais sobre como guardar e compartilhar código usando o GitHub.

Projeto desenvolvido durante a aula para fins de aprendizado.