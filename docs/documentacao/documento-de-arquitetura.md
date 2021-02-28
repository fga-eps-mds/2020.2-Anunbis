## Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
18/02|0.1|Abertura do Documento de Arquitetura|Rafael e Roberto|
28/02|0.2|Atualização do Documento de Arquitetura|Rodrigo e Thiago|
28/02|0.3|Adição do tópico Flask|Rodrigo e Thiago|
28/02|0.4|Adição do tópico MySQL|Rodrigo e Thiago|
28/02|0.5|Adição do tópico Modelo MVC|Rodrigo e Thiago|


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
<p align="justify">&emsp;&emsp;É um modelo para a organização do software do projeto, sendo ele um padrão de arquitetura de software que contribui para melhorar a performance do programa, tornando-o mais produtivo. Essa arquitetura é baseada na separação do código entre Modelo, controle e visão. Sendo assim, esse modelo é utilizado no back-end da aplicação. </p>

<p align="justify">&emsp;&emsp; O pacote ‘modelo’ é responsável por gerenciar os dados, determinando suas funções, lógicas e o padrão de organização que será apresentado ao banco de dados. </p>
<p align="justify">&emsp;&emsp;O pacote ‘controle’ é responsável por ser o intermediador das requisições realizadas pelo pacote ‘visão’ e o ‘modelo’, processando os dados e repassando para seus respectivos destinos.</p>
<p align="justify">&emsp;&emsp;O pacote ‘Visão’ apresenta as informações ao usuário, sendo o local por onde o usuário irá interagir. Nessa camada é onde botões, mensagens e interações com o usuário são elaboradas, onde são capturadas e disponibilizadas informações para o usuário.</p>

<p align="justify">&emsp;&emsp;Essa arquitetura gera inúmeros benefícios ao projeto, a camada de controle por exemplo, serve como um filtro de segurança, pois impede que informações incorretas cheguem até a camada modelo. Contribui com a organização, pois possui fácil leitura e eventuais erros são mais fáceis de serem localizados. Além de que, essa arquitetura de camadas permite que vários programadores trabalhem ao mesmo tempo em diferentes camadas, contribuindo para o desenvolvimento do projeto.</p>

<div style="display:block;text-align:center"><a style="text-align:center" href="https://edisciplinas.usp.br/pluginfile.php/4632609/mod_resource/content/1/5%20Arquitetura%20MVC.pdf"><img src="/images/arquiteturaMVCBackEnd.png" alt="representação da arquitetura MVC no back-end"></a></div>

## 3 <a name="3">Metas e Restrições de Arquitetura</a>

### 3.1 <a name="3_1">Metas</a>

<p align = "justify">&emsp;&emsp; O projeto deve ter acesso às funções básicas de plataformas web e mobile, para dessa maneira, possibilitar que os usuários compartilhem, entre si, suas experiências com os professores e disciplinas.</p>

### 3.2 <a name="3_2">Restrições</a>

<p align = "justify">&emsp;&emsp;A aplicação, por ser PWA, será executada em um navegador, que foi gerada por meio da framework React.js, que é implementada com o Javascript, CSS e HTML. Sobre a comunicação front-end e back-end, ela ocorre por meio de uma API RestFul implementada por uma microframework de python chamada Flask.
</p>


### 4 <a name="4_1">Referências</a>

Wilian, João. Flask: o que é e como codar com esse micro framework Python. **GeekHunter**, 2020. Disponivel em: <a href="https://blog.geekhunter.com.br/flask-framework-python/">Flask: o que é e como codar com esse micro framework Python</a>


COzer, Carolina. O que é SQL e para que ele serve?. **Tecmundo**, 2019. Disponível em : <a href= "https://www.tecmundo.com.br/software/146482-sql-que-ele-serve.htm">  O que é SQL e para que ele serve?</a> 

PRAVALER, Carreira. SQL – o que é e como funciona na prática?. **PRAVALER**, 2020. Disponivel em: <a href="https://www.pravaler.com.br/sql-o-que-e-e-como-funciona-na-pratica/">SQL – o que é e como funciona na prática?</a>
 SQL – o que é e como funciona na prática?

Medeiros, Higor. Introdução ao Padrão MVC. **DEVMEDIA**, 2013. Disponivel em: <a href="https://www.devmedia.com.br/introducao-ao-padrao-mvc/29308">Introdução ao Padrão MVC</a>