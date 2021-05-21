
<div align="center">
    <img src="https://github.com/fga-eps-mds/2020.2-Anunbis/blob/develop/docs/images/logo.png" height="500px" width="350px"></img>
</div>

<h1>
    <div align="center">
        <b style="font-family: Arial;">
            <span style="color:#1D2935">AN</span><span style="color:#FFD54F">UNB</span><span style="color:#1D2935">IS</span>
        </b>
    </div>
</h1>

<p align="center">
    <a href="https://codeclimate.com/github/fga-eps-mds/2020.2-Anunbis/maintainability">
        <img src="https://api.codeclimate.com/v1/badges/a7c9be364b00a8f5c84b/maintainability" />
    </a>
    <a href="https://codecov.io/gh/fga-eps-mds/2020.2-Anunbis">
        <img src="https://codecov.io/gh/fga-eps-mds/2020.2-Anunbis/branch/develop/graph/badge.svg?token=FSRH8CLJ6G"/>
    </a>
    <a href="http://isitmaintained.com/project/fga-eps-mds/2020.2-Anunbis">
        <img alt="Average time to resolve an issue" src="http://isitmaintained.com/badge/resolution/fga-eps-mds/2020.2-Anunbis.svg"></a>
    <a href="http://isitmaintained.com/project/fga-eps-mds/2020.2-Anunbis">
        <img alt="Percentage of issues still open" src="http://isitmaintained.com/badge/open/fga-eps-mds/2020.2-Anunbis.svg"></a>
    <a href="https://www.gnu.org/licenses/gpl-3.0">
        <img alt="License: GPL v3" src="https://img.shields.io/badge/License-GPLv3-blue.svg"></a>
</p>

<p align="center">
    <a href="https://github.com/fga-eps-mds/2020.2-Anunbis-Frontend"><strong>Repositório do Front-End</strong></a>
</p>
<p align="center">
    <a href="https://fga-eps-mds.github.io/2020.2-Anunbis/"><strong>Wiki do Projeto</strong></a>
</p>
<p align="center">
    <a href="https://fga-eps-mds.github.io/2020.2-Anunbis/como_contribuir/"><strong>Como Contribuir</strong></a>
</p>
    
## Principais Funcionalidades

<p align="center">
    <b>
        Encontra Professor(a)
    </b>
</p>
<div align="center">
    <img src="https://user-images.githubusercontent.com/54921791/119206474-a5c2a600-ba71-11eb-8831-b420fd59a77a.png" width="500" height="500" />
</div>

<p align="center">
    <b>
        Avaliar Professor(a)
    </b>
</p>
<div align="center">
    <img src="https://user-images.githubusercontent.com/54921791/119206907-d0f9c500-ba72-11eb-83d2-ddba9f8d70ee.png" width="500" height="600" />
</div>

<p align="center">
    <b>
        Concordar ou Discordar de Avaliações
    </b>
</p>
<div align="center">
    <img src="https://user-images.githubusercontent.com/54921791/119206983-174f2400-ba73-11eb-876f-c9ed4e73d529.png" width="500" height="350" />
</div>
<p align="center">
    <b>
        Ver Avaliações Feitas por Alunos
    </b>
</p>
<div align="center">
    <img src="https://user-images.githubusercontent.com/54921791/119207181-c55ace00-ba73-11eb-84d8-52e6a665eff6.png" width="500" height="600" />
</div>
<p align="center">
    <b>
        Ver Estatisticas Sobre o Desempenho
    </b>
</p>
<div align="center">
    <img src="https://user-images.githubusercontent.com/54921791/119207269-094dd300-ba74-11eb-9422-af2cbddabf65.png" width="500" height="300" />
</div>

    
## Visão Geral

<p align="justify"> &emsp;&emsp; Um dos motivos que define o sucesso acadêmico de um estudante da Universidade de Brasília são seus professores, pois, dependendo deles, o aluno terá uma experiência diferente em relação à disciplina. </p>

<p align = "justify"> &emsp;&emsp; Pensando em melhorar a experiência dos alunos com seus professores, o Anunbis permite que estudantes da UnB avaliem os professores com aos quais já estudaram, disponibilizando esse feedback aos outros discentes e também aos docentes. Dessa forma, tanto os professores quanto os alunos podem tomar as melhores decisões. </p>

O back-end é baseado em [Flask](https://flask.palletsprojects.com/en/1.1.x/).

O front-end é baseado em [React-Js](https://reactjs.org/). 

## Guia de instalação
Para o pleno funcionamento de todas as funções é necessária a instalação de ambos back-end e front-end.

Essa aplicação tem seu ambiente configurado através de conteiners [Docker](https://www.docker.com), portanto, tem como pré-requisitos a instalação do [Docker](https://www.docker.com/get-started) e [Docker-compose](https://docs.docker.com/compose/install/). Para gerenciar os comandos, é necessario ter o [Make GNU](https://www.gnu.org/software/make/).

Também é necessário ter o [Git](https://git-scm.com) instalado para clonar o repositório.

### Back-end

Clonar o repositório:

* `git clone https://github.com/fga-eps-mds/2020.2-Anunbis.git`

Execução do conteiner:

* `docker-compose up`

Acesso  a aplicação:

* `localhost:5000`

Outros comandos:

* `make install` Instala as dependências da aplicação.
* `make up` Executa a aplicação.
* `make seed` Alimenta o banco de dados.
* `make down` Reseta a aplicação.
* `make test` Executa todos os testes.
* `make lint` Formata os arquivos Python para atender a [PEP8](https://www.python.org/dev/peps/pep-0008/).

### Front-end

Clonar o repositório:

* `git clone https://github.com/fga-eps-mds/2020.2-Anunbis-Frontend.git`

Execução do conteiner:

* `docker-compose up`
    
Acesso a aplicação:

* `localhost:3000`

## Releases

### Release 1

[Slides](https://www.canva.com/design/DAEaGAyzAZw/Gg7EyfuyvqhOsFKevdloYQ/view?utm_content=DAEaGAyzAZw&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton)

[Vídeo](https://www.youtube.com/watch?v=FL6XEwcVBhA)

### Release 2
[Slides](https://www.canva.com/design/DAEe5GeecbQ/pj290HIPGtk0VkJHGQHesA/view?utm_content=DAEe5GeecbQ&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton)

[Vídeo](https://drive.google.com/drive/folders/1ZXRgm4K9r3HePXX2FrBa0lDOPfqwmyI-?usp=sharing)
## Equipe
<table>
    <tr>
     <!-- Eduardo   -->
        <td align="center"><a href="https://github.com/oEduardoAfonso"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/54921791?s=400&u=12d7cd0e0fdb7e4540dd786c4cc936167d8b7666&v=4" width="100px;" alt=""/><br /><sub><b>Eduardo Afonso</b><br><b>Desenvolvedor</b></sub></a><br /></td>
     <!-- Rafael -->
        <td align="center"><a href="https://github.com/RcleydsonR">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/74625814?s=460&u=c3b77eaa289d931e139e184d494e0151956372a8&v=4"width="100px;" alt=""/>
        <br /><sub><b>Rafael Cleydson</b><br><b>Scrum Master/ Dev</b></sub></a><br /></td>
         <!-- Roberto  -->
        <td align="center"><a href="https://github.com/mangabeiras"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/54643519?s=400&u=e818422fc51e3e58e20e2bfc28bcdcd96a3acf62&v=4" width="100px;" alt=""/><br /><sub><b>Roberto Gabriel</b><br><b>Desenvolvedor</sub></a><br /></td>
     <!-- Rodrigo     -->
        <td align="center"><a href=https://github.com/Balbinoo><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/54644626?s=400&u=8d36fb668cd69ccd23d5827ae9e1b86a937eefa1&v=4" width="100px;" alt=""/><br /><sub><b>Rodrigo Balbino</b><br><b>Product Owner/ Dev</b></sub></a><br /></td>
    <!-- Thiago  -->
        <td align="center"><a href=https://github.com/thiagohdaqw><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/54081877?s=400&u=c1add0666adbf836efe972df83a854185477c2cc&v=4" width="100px;" alt=""/><br /><sub><b>Thiago Paiva</b><br><b>DevOps/ Dev</sub></a><br/></td>
     <!-- Victor -->
        <td align="center"><a href=https://github.com/victorhugo21><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/54643372?s=400&u=662c17b015a365ca35b5b4ea519c0fd64fd00184&v=4" width="100px;" alt=""/><br /><sub><b>Victor Hugo</b><br><b>Desenvolvedor</sub></a><br/></td>
        </tr>
    </table>
