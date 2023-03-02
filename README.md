# join-mapping
job interview

### COM DOCKER
apenas rodar o comando abaixo:

``cp contrib/env-sample .env``

`docker-compose up`

### Criando ambiente virtual

``python -m venv .venv``

### Criar o ``.env`` de forma programática

No terminal (cmd) percorra até a raiz do projeto e digite o comando abaixo:

``python contrib/env_gen.py``

após será criado o ``.env`` na raiz do seu projeto

altere o DATABASE_URL com as credenciais do seu banco postgres ou deixe comentado para usar o sqlite

 #### linux (alternativa)
 
 ``cp contrib/env-sample .env``
    
``source .venv/bin/activate``

#### windows (alterantiva)

`` você deve copiar o arquivo env-sample e colar na raiz do projeto com o nome de .env ``

``.venv\Scripts\Activate ``

#### Instalando dependências

`` pip install -r requirements.txt``

#### aplicando migrações e rodando projeto

``python manage.py makemigrations``

``python manage.py migrate``

``python manage.py runserver``

#### Agradeço desde já a oportunidade, com o tempo hábil foi o melhor que pude fazer :)
