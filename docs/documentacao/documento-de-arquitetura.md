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
|**PWA**| Progressive Web Aplication|

### 1.4 <a name="1_4">Visão Geral</a>
<p align="justify"> &emsp;&emsp; Este documento é dividido, atualmente, em 4 tópicos, descrevendo de maneira concisa o projeto. Esses tópicos são divididos em:
</p>

* Introdução: Fornece uma visão geral do documento inteiro;
* Representação arquitetural: Descreve as tecnologias que serão utilizadas no projeto, bem como o porquê da escolha dessas tecnologias.
* Metas e restrições da arquitetura: Descreve os requisitos e objetivos do software que possui algum impacto sobre a arquitetura.
* Referências: Emprega as fontes utilizadas nas pesquisas para relacionar as publicações que foram consultadas e citadas.

## 2 <a name="2">Representação arquitetural</a>

### 2.1 <a name="3_1">React</a>

<p align = "justify"> &emsp;&emsp; Para representarmos a camada view no MVC, decidimos usar a biblioteca <a href="https://pt-br.reactjs.org/docs/getting-started.html">ReactJS</a> como front-end do projeto, realizando a parte onde se tem a interação do usuário com a página.</p>

<p align = "justify"> &emsp;&emsp; Essa bibliteca JavaScript torna a criação de interfaces de usuário uma tarefa fácil, renderizando de forma eficiente apenas os componentes necessários, caso os dados mudem.</p>

<p align = "justify"> &emsp;&emsp; Os <a href="https://pt-br.reactjs.org/docs/react-component.html">componentes</a> são a base do ReactJS, são como elementos HTML personalizados, reutilizáveis, permitem dividir a interface do usuário em partes independentes e pensar em cada parte isoladamente. O React também agiliza como os dados são armazenados e tratados, usando o <a href="https://pt-br.reactjs.org/docs/state-and-lifecycle.html">estado</a> e os <a href="https://pt-br.reactjs.org/docs/render-props.html">props</a>.</p>

### 2.2 <a name="3_2">Flask</a>

<!-- <a href= "" ></a>   ## pra colocar link -->  

### 2.3 <a name="3_2">MySQL</a>

<p align = "justify"> &emsp;&emsp;Para a persistência dos dados, o banco utilizado é o MySQL, pois utiliza a linguagem SQL, que é <a href="https://insights.stackoverflow.com/survey/2020#technology">o favorito do mercado</a>. No entanto, não há a necessidade de utilizar a linguagem SQL diretamente, pois o SQLAlchemy juntamente com o micro framework Flask realizam esse trabalho.</p>

<p align = "justify">&emsp;&emsp;Sendo assim, o SQLAlchemy é capaz de mediar todas as tarefas necessárias, como por exemplo, criar tabelas, relacionamentos, realizar  consultas, adicionar e remover informações, para o pleno funcionamento desse projeto.</p>

### 2.4 <a name="3_4">Modelo MVC</a>
<p align="justify">&emsp;&emsp;É um modelo para a organização do software do projeto, sendo ele um padrão de arquitetura de software que contribui para melhorar a performance do programa, tornando-o mais produtivo. Essa arquitetura é baseada na separação do código entre Modelo, controle e visão. Sendo assim, esse modelo é utilizado no back-end da aplicação. </p>

<p align="justify">&emsp;&emsp; O pacote ‘modelo’ é responsável por gerenciar os dados, determinando suas funções, lógicas e o padrão de organização que será apresentado ao banco de dados. </p>
<p align="justify">&emsp;&emsp;O pacote ‘controle’ é responsável por ser o intermediador das requisições realizadas pelo pacote ‘visão’ e o ‘modelo’, processando os dados e repassando para seus respectivos destinos.</p>
<p align="justify">&emsp;&emsp;O pacote ‘Visão’ apresenta as informações ao usuário, sendo o local por onde o usuário irá interagir. Nessa camada é onde botões, mensagens e interações com o usuário são elaboradas, onde são capturadas e disponibilizadas informações para o usuário.</p>

<p align="justify">&emsp;&emsp;Essa arquitetura gera inúmeros benefícios ao projeto, a camada de controle por exemplo, serve como um filtro de segurança, pois impede que informações incorretas cheguem até a camada modelo. Contribui com a organização, pois possui fácil leitura e eventuais erros são mais fáceis de serem localizados. Além de que, essa arquitetura de camadas permite que vários programadores trabalhem ao mesmo tempo em diferentes camadas, contribuindo para o desenvolvimento do projeto.</p>

<div style="display:block;text-align:center"><a style="text-align:center" href="https://edisciplinas.usp.br/pluginfile.php/4632609/mod_resource/content/1/5%20Arquitetura%20MVC.pdf"><img src="/2020.2-Anunbis/images/arquiteturaMVCBackEnd.png" alt="representação da arquitetura MVC no back-end"></a></div>

## 3 <a name="3">Metas e Restrições de Arquitetura</a>

### 3.1 <a name="3_1">Metas</a>

<p align = "justify">&emsp;&emsp; O projeto deve ter acesso às funções básicas de plataformas web e mobile, para dessa maneira, possibilitar que os usuários compartilhem, entre si, suas experiências com os professores e disciplinas.</p>

### 3.2 <a name="3_2">Restrições</a>

<p align = "justify">&emsp;&emsp;A aplicação, por ser PWA, será executada em um navegador, que foi gerada por meio da framework React.js, que é implementada com o Javascript, CSS e HTML. Sobre a comunicação front-end e back-end, ela ocorre por meio de uma API RestFul implementada por uma microframework de python chamada Flask.
</p>

## 4 <a name"4">Visão dos Casos de Uso</a>
### 4.1 <a name="4_1">Diagrama dos Casos de Uso</a>
<div style="display:block;text-align:center"><img src="/images/casosDeUso.png" alt="Diagrama dos casos de Uso"></div>

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
<p align = "justify">&emsp;&emsp;A comunicação do usuário com a aplicação será feito pela camada view do MVC. Os eventos do front-end serão interpretados pela biblioteca do <a href="https://pt-br.reactjs.org/docs/getting-started.html">ReactJS</a>, essa mesma biblioteca se comunicará com o back-end, que será executada com flask e mysql.</p>

<p align = "justify">&emsp;&emsp;No banco de dados, serão armazenados os dados dos usuários, dos professores e das disciplinas. Ao procurar por um professor, uma requisição será feita no back-end, e caso algum professor correspondente seja encontrado, será devolvido ao usuário o docente, sua pontuação e seus feedbacks. Essa troca de informação também será igual para os professores usuários.</p>

## 6 <a name="6">Referências</a>

Wilian, João. Flask: o que é e como codar com esse micro framework Python. **GeekHunter**, 2020. Disponivel em: <a href="https://blog.geekhunter.com.br/flask-framework-python/">Flask: o que é e como codar com esse micro framework Python</a>


COzer, Carolina. O que é SQL e para que ele serve?. **Tecmundo**, 2019. Disponível em : <a href= "https://www.tecmundo.com.br/software/146482-sql-que-ele-serve.htm">  O que é SQL e para que ele serve?</a> 

PRAVALER, Carreira. SQL – o que é e como funciona na prática?. **PRAVALER**, 2020. Disponivel em: <a href="https://www.pravaler.com.br/sql-o-que-e-e-como-funciona-na-pratica/">SQL – o que é e como funciona na prática?</a>
 SQL – o que é e como funciona na prática?

Medeiros, Higor. Introdução ao Padrão MVC. **DEVMEDIA**, 2013. Disponivel em: <a href="https://www.devmedia.com.br/introducao-ao-padrao-mvc/29308">Introdução ao Padrão MVC</a>
