## Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
18/02|0.1|Abertura do Documento de Arquitetura|Rafael e Roberto|
28/02|0.2|Atualização do Documento de Arquitetura|Rodrigo e Thiago|
28/02|0.3|Adição do tópico Flask|Thiago e Rodrigo|
28/02|0.4|Adição do tópico MySQL|Thiago e Rodrigo|
28/02|0.5|Adição do tópico Modelo MVC|Thiago e Rodrigo|
28/02|0.6|Adição do conteúdo do tópico Flask|Thiago e Rodrigo|


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
|**PWA**| Programming Web Aplication|

### 1.4 <a name="1_4">Visão Geral</a>
<p align="justify"> &emsp;&emsp; Este documento é dividido, atualmente, em 2 tópicos, descrevendo de maneira concisa o projeto. Esses tópicos são divididos em:
</p>

* Introdução: Fornece uma visão geral do documento inteiro;
* Metas e restrições da arquitetura: Descreve os requisitos e objetivos do software que possui algum impacto sobre a arquitetura.

## 2 <a name="2">Representação arquitetural</a>

### 2.1 <a name="3_1">React</a>
### 2.2 <a name="3_2">Flask</a>

<!-- <a href= "" ></a>   ## pra colocar link -->  

<p align = "justify"> &emsp;&emsp; Para este projeto, decidimos escolher a micro framework web Flask, implementada em Python para ficar responsável pelo back-end do projeto. Por ser um micro framework, o <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a> possui apenas o mínimo possível para a API funcionar.</p>

<p align = "justify"> &emsp;&emsp; Assim, se for necessário, é possível instalar pacotes extras para todo desenvolvimento da aplicação. Isso permite que um projeto implementado com o Flask só tenha o que realmente precisa, ao invés de termos inúmeras ferramentas e módulos sem nenhuma utilização no projeto. </p>

<p align = "justify"> &emsp;&emsp; Dentre estes pacotes extras há: o <a href="https://flask-sqlalchemy.palletsprojects.com/en/2.x/">SQLAlchemy</a>, para cuidar da comunicação com o banco de dados; <a href="https://flask-marshmallow.readthedocs.io/en/latest/">Mashmallow</a>, para cuidar da serialização; e o <a href="https://flask-migrate.readthedocs.io/en/latest/" >Migrate</a>, que cuida do versionamento do banco de dados pelo Python.</p>


### 2.3 <a name="3_2">MySQL</a>

<p align = "justify"> &emsp;&emsp;Para a persistência dos dados, o banco utilizado é o MySQL, pois utiliza a linguagem SQL, que é <a href="https://insights.stackoverflow.com/survey/2020#technology">o favorito do mercado</a>. No entanto, não há a necessidade de utilizar a linguagem SQL diretamente, pois o SQLAlchemy juntamente com o micro framework Flask realizam esse trabalho.</p>

<p align = "justify">&emsp;&emsp;Sendo assim, o SQLAlchemy é capaz de mediar todas as tarefas necessárias, como por exemplo, criar tabelas, relacionamentos, realizar  consultas, adicionar e remover informações, para o pleno funcionamento desse projeto.</p>

### 2.4 <a name="3_4">Modelo MVC</a>

## 3 <a name="3">Metas e Restrições de Arquitetura</a>

### 3.1 <a name="3_1">Metas</a>

<p align = "justify">&emsp;&emsp; O projeto deve ter acesso às funções básicas de plataformas web e mobile, para dessa maneira, possibilitar que os usuários compartilhem, entre si, suas experiências com os professores e disciplinas.</p>

### 3.2 <a name="3_2">Restrições</a>

<p align = "justify">&emsp;&emsp;A aplicação, por ser PWA, será executada em um navegador, que foi gerada por meio da framework React.js, que é implementada com o Javascript, CSS e HTML. Sobre a comunicação front-end e back-end, ela ocorre por meio de uma API RestFul implementada por uma microframework de python chamada Flask.
</p>



