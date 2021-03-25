## Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
18/02|0.1|Abertura do Documento de Arquitetura|Rafael e Roberto|
28/02|0.2|Atualização do Documento de Arquitetura|Rodrigo e Thiago|
28/02|0.3|Adição do tópico Flask|Rodrigo e Thiago|
28/02|0.4|Adição do tópico MySQL|Rodrigo e Thiago|
28/02|0.5|Adição do tópico Modelo MVC|Rodrigo e Thiago|
02/03|0.6|Adição do tópico React|Victor|
05/03|0.7|Adição do tópico Visão dos Casos de Uso|Roberto|
05/03|0.8|Adição do tópico Visão Lógica|Roberto|
06/03|0.9|Adição do diagrama arquitetural|Thiago|
19/03|1.0|Adição do tópico Visão da Implementação|Thiago|
20/03|1.1|Atualizando tópico das metas|Rodrigo|
22/03|1.2|Atualizando Modelagem de dados|Thiago|
24/03|1.3|Adição dos diagramas de pacotes|Rafael e Roberto|

## 1 <a name="1">Introdução</a>

### 1.1 <a name="1_1">Finalidade</a>

 <p align = "justify"> &emsp;&emsp; Essa documentação tem como finalidade fornecer uma visão geral da arquitetura do projeto Anunbis, demonstrando inicialmente, suas metas e objetivos. Para assim exclarecer as decisões de desenvolvimento que foram tomadas ao longo do projeto. </p>

### 1.2 <a name="1_2">Escopo</a>

<p align="justify"> &emsp;&emsp; Com esse documento, é possível entender de maneira mais clara e objetiva toda a arquitetura do projeto, permitindo ao leitor a compreensão de todo o sistema, bem como as abordagens usadas para o desenvolvimento do mesmo.</p>

### 1.3 <a name="1_3">Definições, Acrônimos e Abreviações</a>

|Abreviação|Significado
|:-|:-|
|**MDS**| Métodos de Desenvolvimento de Software|
|**EPS**| Engenharia de Produto de Software|

### 1.4 <a name="1_4">Visão Geral</a>
<p align="justify"> &emsp;&emsp; Este documento é dividido, atualmente, em 7 tópicos, descrevendo de maneira concisa o projeto. Esses tópicos são divididos em:
</p>

* Introdução: Fornece uma visão geral do documento inteiro;
* Representação arquitetural: Descreve as tecnologias que serão utilizadas no projeto, bem como o porquê da escolha dessas tecnologias.
* Metas e restrições da arquitetura: Descreve os requisitos e objetivos do software que possui algum impacto sobre a arquitetura.
* Visão dos Casos de Uso: Descreve as funcionalidades que o usuario poderá efetuar.
* Visão Lógica: Descreve as interações entre as camadas e as tecnologias.
* Visão da Implementação: Descreve as implementações das camadas e tecnologias.
* Referências: Emprega as fontes utilizadas nas pesquisas para relacionar as publicações que foram consultadas e citadas.

## 2 <a name="2">Representação arquitetural</a>

<p align = "justify"> &emsp;&emsp;Este projeto utiliza diversas tecnologias que se relacionam para fazer uma aplicação web. A figura abaixo mostra um diagrama com a representação arquitetural do programa.</p>

<div style="display:block;text-align:center"><a style="text-align:center" href="https://edisciplinas.usp.br/pluginfile.php/4632609/mod_resource/content/1/5%20Arquitetura%20MVC.pdf"><img src="/2020.2-Anunbis/images/diagramaArquitetura.png" alt="representação da arquitetura no projeto"></a></div>

<p align = "justify"> &emsp;&emsp;Ele se baseia em requisições e respostas Http para se relacionar. O usuario, com seu navegador, entra no site gerado pelo React e, a partir dai, pode realizar varias ações, como cadastrar, postar e comentar. O react lida com essas ações e, se precisar, se conecta com o Flask. O Flask, por sua vez, cuida da lógica de negócio, manuseamento de dados e faz a conexão com o Mysql para a persistência desses dados.</p>

### 2.1 <a name="3_1">React</a>

<p align = "justify"> &emsp;&emsp; Para representarmos a camada de contato com o usuário, decidimos usar a biblioteca <a href="https://pt-br.reactjs.org/docs/getting-started.html">ReactJS</a> como front-end do projeto, realizando a parte onde se tem a interação do usuário com a página. Essa biblioteca JavaScript torna a criação de interfaces de usuário uma tarefa fácil, renderizando de forma eficiente apenas os componentes necessários, caso os dados mudem.</p>

<p align = "justify"> &emsp;&emsp; Os <a href="https://pt-br.reactjs.org/docs/react-component.html">componentes</a> são a base do ReactJS, são como elementos HTML personalizados, reutilizáveis, permitem dividir a interface do usuário em partes independentes e pensar em cada parte isoladamente. O React também agiliza como os dados são armazenados e tratados, usando o <a href="https://pt-br.reactjs.org/docs/state-and-lifecycle.html">estado</a> e os <a href="https://pt-br.reactjs.org/docs/render-props.html">props</a>.</p>

### 2.2 <a name="3_2">Flask</a>

<!-- <a href= "" ></a>   ## pra colocar link -->  

<p align = "justify"> &emsp;&emsp; Para este projeto, decidimos escolher a micro framework web Flask, implementada em Python para ficar responsável pelo back-end do projeto. Por ser um micro framework, o <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a> possui apenas o mínimo possível para a API funcionar.</p>

<p align = "justify"> &emsp;&emsp; Assim, se for necessário, é possível instalar pacotes extras para todo desenvolvimento da aplicação. Isso permite que um projeto implementado com o Flask só tenha o que realmente precisa, ao invés de termos inúmeras ferramentas e módulos sem nenhuma utilização no projeto. Dentre estes pacotes extras há: o <a href="https://flask-sqlalchemy.palletsprojects.com/en/2.x/">SQLAlchemy</a>, para cuidar da comunicação com o banco de dados; <a href="https://flask-marshmallow.readthedocs.io/en/latest/">Mashmallow</a>, para cuidar da serialização.</p>
 <!-- e o <a href="https://flask-migrate.readthedocs.io/en/latest/" >Migrate</a>, que cuida do versionamento do banco de dados pelo Python. -->

### 2.3 <a name="3_2">MySQL</a>

<p align = "justify"> &emsp;&emsp;Para a persistência dos dados, o banco utilizado é o MySQL, pois utiliza a linguagem SQL e é <a 
href="https://insights.stackoverflow.com/survey/2020#technology">o favorito do mercado</a>. Além disso, pelo fato de ser relacional, será bastante util em fazer as relações entre as entidades.</p>
<!-- No entanto, não há a necessidade de utilizar a linguagem SQL diretamente, pois o SQLAlchemy juntamente com o micro framework Flask realizam esse trabalho. -->

<!-- <p align = "justify">&emsp;&emsp;Sendo assim, o SQLAlchemy é capaz de mediar todas as tarefas necessárias, como por exemplo, criar tabelas, relacionamentos, realizar  consultas, adicionar e remover informações, para o pleno funcionamento desse projeto.</p> -->

### 2.4 <a name="3_4">Modelo MVC</a>
<p align="justify">&emsp;&emsp;É um modelo para a organização do software do projeto, sendo ele um padrão de arquitetura de software que contribui para melhorar a performance do programa, tornando-o mais produtivo. Essa arquitetura é baseada na separação do código entre Modelo, controle e visão. Sendo assim, esse modelo é utilizado no back-end da aplicação. </p>

<p align="justify">&emsp;&emsp; O pacote ‘modelo’ é responsável por gerenciar os dados, determinando suas funções, lógicas e o padrão de organização que será apresentado ao banco de dados. </p>
<p align="justify">&emsp;&emsp;O pacote ‘controle’ é responsável por ser o intermediador das requisições realizadas pelo pacote ‘visão’ e o ‘modelo’, processando os dados e repassando para seus respectivos destinos.</p>
<p align="justify">&emsp;&emsp;O pacote ‘Visão’ apresenta as informações ao usuário, sendo o local por onde o usuário irá interagir. Nessa camada é onde interações com o usuário são elaboradas, são capturadas, validadas e disponibilizadas. Tudo isso por meio do JSON.</p>

<p align="justify">&emsp;&emsp;Essa arquitetura gera inúmeros benefícios ao projeto, a camada de controle, por exemplo, serve como um filtro de segurança, pois impede que informações incorretas cheguem até a camada modelo. Contribui com a organização, pois possui fácil leitura e eventuais erros são mais fáceis de serem localizados. Além disso, essa arquitetura de camadas permite que vários programadores trabalhem ao mesmo tempo em diferentes camadas, contribuindo para o desenvolvimento do projeto.</p>

<div style="display:block;text-align:center"><a style="text-align:center" href="https://edisciplinas.usp.br/pluginfile.php/4632609/mod_resource/content/1/5%20Arquitetura%20MVC.pdf"><img src="/2020.2-Anunbis/images/arquiteturaMVCBackEnd.png" alt="representação da arquitetura MVC no back-end"></a></div>

## 3 <a name="3">Metas e Restrições de Arquitetura</a>

### 3.1 <a name="3_1">Metas</a>

<p align = "justify">&emsp;&emsp; O projeto deve ter acesso às funções básicas de plataformas web, para dessa maneira, possibilitar que os usuários compartilhem, entre si, suas experiências com os professores e disciplinas. O objetivo é ajudar os estudantes a escolherem suas disciplinas, e os professores receberem feedback para melhorarem suas metodologias.</p>

### 3.2 <a name="3_2">Restrições</a>

<p align = "justify">&emsp;&emsp;A aplicação será executada em um navegador, que foi gerada por meio da framework React.js, que é implementada com o Javascript, CSS e HTML. Sobre a comunicação front-end e back-end, ela ocorre por meio de uma API RestFul implementada por um microframework de python chamado Flask.
</p>

## 4 <a name="4">Visão dos Casos de Uso</a>
### 4.1 <a name="4_1">Diagrama dos Casos de Uso</a>
<div style="display:block;text-align:center"><img src="/2020.2-Anunbis/images/casosDeUso.png" alt="Diagrama dos casos de Uso"></div>

### 4.2 <a name="4_2">Atores dos Casos de Uso</a>

|Ator|Descrição|
|:-|:-|
|**Discente**| O discente poderá avaliar professores pontuando-os, fazendo comentários e apoiando/discordando de outros feedbacks. Poderá também visualizar o rank de professores e acompanhar os comentários de outros alunos por meio da pesquisa por matéria/docente. |
|**Docente**| O docente poderá visualizar as avaliações que os estudantes fizeram a ele. Isso ocorrerá por meio da visualização de comentários e da sua pontuação média.|

### 4.3 <a name="4_3">Descrição dos Casos de Uso</a>
|Caso de Uso|Descrição|
|:-|:-|
|US01 - Pontuar Professor| Dar uma nota ao professor avaliado. |
|US02 - Fazer Comentário| Dar um feedback de determinado docente.|
|US03 - Avaliar outros Comentários| Concordar ou Discordar dos feedbacks de um professor.|
|US04 - Avaliar Professor| Fazer um feedback geral de um docente.|
|US05 - Visualizar Rank de Docentes| Ver quais os docentes melhores pontuados por disciplina.|
|US06 - Visualizar Comentários de Outros Alunos| Ver feedbacks dos outros discentes para aquele professor.|
|US07 - Pesquisar Disciplina ou Professor| Procurar a disciplina/professor da UnB que o aluno deseja.|
|US08 - Visualizar Comentários| Professor visualizar os comentários dos alunos.|
|US09 - Visualizar Média de Pontuação| O docente pode ver sua pontuação média no sistema.|
|US10 - Visualizar Avaliações dos Alunos|O docente pode ver as avaliações gerais dos alunos.|

## 5 <a name="5">Visão Lógica</a>
<p align = "justify">&emsp;&emsp;A comunicação do usuário com a aplicação será feito pela camada view do MVC. Os eventos do front-end serão interpretados pela biblioteca do <a href="https://pt-br.reactjs.org/docs/getting-started.html">ReactJS</a>, essa mesma biblioteca se comunicará com o back-end, que será executada com Flask e Mysql.</p>

<p align = "justify">&emsp;&emsp;No banco de dados, serão armazenados os dados dos usuários, dos professores e das disciplinas. Ao procurar por um professor, uma requisição será feita no back-end, e caso algum professor correspondente seja encontrado, será devolvido ao usuário o docente, sua pontuação e seus feedbacks. Essa troca de informação também será igual para os professores usuários.</p>

### 5.1 <a name="5_1">Diagrama de Pacotes</a>

#### 5.1.1 <a name="5_1_1">Front-End</a>
<div style="display:block;text-align:center"><img src="/2020.2-Anunbis/images/Diagrama_Pacotes_FrontEnd.png" alt="Diagrama de pacotes Front-End"/></div>

#### 5.1.2 <a name="5_1_1">Back-End</a>
<div style="display:block;text-align:center"><img src="/2020.2-Anunbis/images/Diagrama_Pacotes_BackEnd.png" alt="Diagrama de pacotes Back-End"/></div>


## 6 <a name="6">Visão da Implementação</a>

### 6.1 <a name="6_1">Modelagem dos dados</a>
#### 6.1.1 <a name="6_1_1">Entidades</a>

* Estudante
* Professor
* Curso
* Disciplina
* Avaliação
* Denúncia

#### 6.1.2 <a name="6_1_2">Atributos</a>

* Um **Estudante**, para que possa ser cadastrado, tem uma **matrícula**, **nome**, **email** e uma **senha**.
* Um **Professor** tem uma **matrícula**, **identificação**, **nome**, **email** e uma **senha**.
* Um **Curso** tem um **nome**.
* Uma **Disciplina** tem um **nome** e um **codigo**.
* Uma **Avaliação**, para ser cadastrada, tem uma **identificação**, **conteúdo**, **data de postagem**, se é **anônima** ou não e uma **nota** sobre o professor.
* Uma **Denúncia** tem uma **identificação**, **conteúdo** e um **tipo**, que pode ser uma denuncia grave, incoerente, ofensiva e outras.

#### 6.1.3 <a name="6_1_3">Relacionamentos</a>

* Um **estudante** pertence a um **curso**, já um **curso** pode ter varios **estudantes**. **Cardinalidade: N:1**

* Uma **estudante** pode fazer várias **avaliações**, mas uma **avaliação** só pode ter um **autor**, que é um **estudante**. **Cardinalidade: 1:N**

* Um **estudante** pode **concordar** ou **discordar** de várias **avaliações**, e uma **avaliação** pode ter varios **alunos** que **concordam** ou **discordam**. **Cardinalidade: N:N**

* Um **estudante** pode **denunciar** várias **avaliações**. **Cardinalidade: 1:N**

* Um **professor** pode ministrar várias **disciplinas** e uma **disciplina** tem vários **professores**. **Cardinalidade: N:N** 

* Um **curso** pode ter várias **disciplinas** e uma **disciplina** pode pertencer a mais de um **curso**. **Cardinalidade: N:N**

* Uma **avaliação** pode sofrer várias **denuncias**. **Cardinalidade: 1:N**

* Uma **avaliação** se refere a um **professor**, e um **professor** pode ter várias **avaliações**. **Cardinalidade: N:1**

* Uma **avaliação** se refere a uma **disciplina**. **Cardinalidade: 1:1**

#### 6.1.4 <a name="6_1_4">Diagrama Entidade Relacionamento</a>

<div style="display:block;text-align:center"><img src="/2020.2-Anunbis/images/diagramaEntidadeRelacionamento.png" alt="Diagrama Entidade Relacionamento"/></div>

#### 6.1.4 <a name="6_1_4">Diagrama do Banco de Dados</a>

<div style="display:block;text-align:center"><img src="/2020.2-Anunbis/images/diagramaLogicoDados.png" alt="Diagrama Logico dos Dados"/></div>

## 7 <a name="7">Referências</a>

Wilian, João. Flask: o que é e como codar com esse micro framework Python. **GeekHunter**, 2020. Disponivel em: <a href="https://blog.geekhunter.com.br/flask-framework-python/">Flask: o que é e como codar com esse micro framework Python</a>

COzer, Carolina. O que é SQL e para que ele serve?. **Tecmundo**, 2019. Disponível em : <a href= "https://www.tecmundo.com.br/software/146482-sql-que-ele-serve.htm">  O que é SQL e para que ele serve?</a> 

PRAVALER, Carreira. SQL – o que é e como funciona na prática?. **PRAVALER**, 2020. Disponivel em: <a href="https://www.pravaler.com.br/sql-o-que-e-e-como-funciona-na-pratica/">SQL – o que é e como funciona na prática?</a>
 SQL – o que é e como funciona na prática?

Medeiros, Higor. Introdução ao Padrão MVC. **DEVMEDIA**, 2013. Disponivel em: <a href="https://www.devmedia.com.br/introducao-ao-padrao-mvc/29308">Introdução ao Padrão MVC</a>
