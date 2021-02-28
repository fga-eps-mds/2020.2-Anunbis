## Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
18/02|0.1|Abertura do Documento de Arquitetura|Rafael e Roberto|
28/02|0.2|Atualização do Documento de Arquitetura|Rodrigo e Thiago|
28/02|0.3|Adição do tópico Flask|Thiago e Rodrigo|


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
### 2.3 <a name="3_2">MySQL</a>
### 2.4 <a name="3_4">Modelo MVC</a>

## 3 <a name="3">Metas e Restrições de Arquitetura</a>

### 3.1 <a name="3_1">Metas</a>

<p align = "justify">&emsp;&emsp;O projeto deve ter acesso às funções básicas de plataformas web e mobile, para dessa maneira, possibilitar que os usuários compartilhem, entre si, suas experiências com os professores e disciplinas.</p>

### 3.2 <a name="3_2">Restrições</a>

<p align = "justify">&emsp;&emsp;A aplicação, por ser PWA, será executada em um navegador, que foi gerada por meio da framework React.js, que é implementada com o Javascript, CSS e HTML. Sobre a comunicação front-end e back-end, ela ocorre por meio de uma API RestFul implementada por uma microframework de python chamada Flask.
</p>



