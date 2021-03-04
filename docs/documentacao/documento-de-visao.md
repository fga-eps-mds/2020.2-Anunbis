## Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
17/02|0.1|Abertura do Documento de Visão| Equipe|
04/03|0.2|Adição dos itens 5, 6 e 7| Roberto|


## 1 <a name="1">Introdução</a>

### 1.1 <a name ="1_1">Propósito</a>

<p align="justify"> &emsp;&emsp; Este documento tem por objetivo estabelecer um posicionamento sobre a aplicação, suas características e seu desenvolvimento em questão. Também expondo as suas funcionalidades e definindo seus requisitos em termos de necessidade para usuários finais.</p>

### 1.2 <a name="1_2">Escopo</a>

<p align="justify"> &emsp;&emsp; Um dos motivos que define o sucesso acadêmico de um estudante da Universidade de Brasília são seus professores, pois, dependendo deles, o aluno terá uma experiência diferente em relação à disciplina. Alguns professores cobram mais e outros cobram menos, de fato o aprendizado de um estudante não depende apenas dele mesmo e sim de um conjunto de fatores incluindo o seu professor. Sendo a finalidade desse projeto, disponibilizar uma forma confiável de escolher seus próprios professores.</p>

### 1.3 <a name=1_3>Definições, acrônimos e abreviações</a>

* FGA - Faculdade do Gama (UnB)
* UnB - Universidade de Brasília
* MDS - Métodos de Desenvolvimento de Software

### 1.4 <a name="1_4">Visão geral</a>
<p align="justify"> &emsp;&emsp; Este documento é dividido em 5 tópicos descrevendo os detalhes das características do software proposto.
Sendo dividido em:</p>

* **Introdução:** no qual é introduzido os detalhes gerais sobre a visão do projeto;
* **Posicionamento:** descrevendo o problema e a oportunidade de negócio;
* **Descrição dos envolvidos:** esta seção descreve o perfil das partes interessadas no projeto;
* **Visão Geral:** Esta seção fornece uma visualização de alto nível das capacidades do produto, interfaces para outros aplicativos e configurações dos sistemas;
* **Recursos:** breve descrição dos recursos do produto;

___

## 2 <a name="2">Posicionamento</a>
<p align="justify">&emsp;&emsp; A maior parte dos estudantes entram na universidade com um grande anseio por conhecimento, porém com o tempo esse desejo acaba sendo anulado por professores que não possuem uma boa didática ou não se dedicam a ajudar o estudante.</p>

### 2.1 <a name="2_1">Oportunidade de Negócio</a>

<p align="justify">&emsp;&emsp; O projeto dá ao aluno a opção de escolher o professor e como efeito a metodologia de ensino de cada matéria, baseado na análise de quem já tenha tido alguma experiência com esse docente. A aplicação visa disponibilizar de maneira rápida, fácil, respeitável e democrática, um feedback àqueles que se dedicam a ensinar.</p>

### 2.2 <a name="2_2">Descrição do problema</a>

|**Questão**|**Informações do Produto**|
|:-|:-|
|**O Problema é**|Falta de conhecimento prévio dos professores e das disciplinas.|
|**Que afeta**|A comunidade acadêmica. |
|**Cujo impacto é**|O aluno não encontrar uma metodologia de ensino compatível com si mesmo.|
|**Uma boa solução seria**|Uma aplicação que compartilha as experiências dos alunos com as disciplinas e professores entre si.|

### 2.3 <a name="2_3">Descrição da Posição do Produto</a>

<p align="justify">&emsp;&emsp;A aplicação, quando desenvolvida, se posicionará no mercado como uma aplicação web que pode ser usada facilmente em navegadores mobile proporcionando uma experiência muito parecida a de um app nativo. Isso proporciona que os alunos troquem experiências de suas disciplinas realizadas de forma eficiente e rápida, possibilitando que os alunos encontrem metodologias de ensino compatíveis com si mesmo.</p>


## 3 <a name="3">Descrição dos Envolvidos</a>

|**Nome**|**Descrição**|
|:-|:-|
| Estudantes da UnB| Estudantes procurando um bom professor ou metodologia. |
|Professores da UnB| Professores com desejo de melhorar a própria avaliação. |

## 4 <a name="4">Visão Geral</a>
<p align="justify"> &emsp;&emsp; A aplicação tem como objetivo criar um ambiente específico para que haja uma troca de informações entre os alunos da UnB a respeito dos professores e suas metodologias de ensino, tornando viável que qualquer aluno possa escrever suas próprias avaliações de maneira anônima e ler as avaliações feitas por outros alunos.
</p>

## 5 <a name="5">Recursos do Produto</a>

### 5.1 <a name="5.1">Recursos dos Discentes</a>

<p align="justify"> &emsp;&emsp; Os alunos poderão se cadastrar na aplicação. Quando cadastrados e logados, poderão ter acesso aos seguintes recursos:</p>

* Visualizar/Fazer pontuação dos professores;
* Visualizar/Fazer comentários contendo feedbacks dos professores;
* Visualizar quantidade de alunos que concordam e discordam desses comentários;
* Concordar ou discordar de um comentário de outro discente;
* Pesquisar os melhores professores, por pontuação, para suas disciplinas;
* Visualizar quantidade de avaliações realizadas por eles mesmos.

### 5.2 <a name="5.2">Recursos dos Docentes</a>

<p align="justify"> &emsp;&emsp; Os professores poderão também se cadastrar na aplicação. Quando cadastrados e logados, terão acesso às seguintes funcionalidades:</p>

* Visualizar os feedbacks dos outros alunos em relação às suas metodologias;
* Visualizar a sua pontuação na aplicação.

## 6 <a name="6">Restrições</a>

### 6.1 <a name="6.1">Restrições de Implementação</a>

<p align="justify">&emsp;&emsp;O sistema será implementado usando ReactJS, flask e python, e será desenvolvido de forma remota devido à pandemia.</p>

### 6.2 <a name="6.2">Restrições Externas</a>
<p align="justify">&emsp;&emsp;O grupo não tem muita experiência com as tecnologias utilizadas.</p>

### 6.3 <a name="6.3">Restrições de Design</a>
<p align="justify"> &emsp;&emsp;Toda experiência com a aplicação deve ser limpa e natural. O usuário não deve ter dificuldades de entender o que ele pode fazer, e como encontrar determinada funcionalidade. Além disso, a aplicação será destinada aos usuários web.</p>

### 6.4 <a name="6.4">Restriçõs de Uso</a>
<p align="justify"> &emsp;&emsp;É necessário que os usuários (a comunidade acadêmica) tenha acesso à um computador ou smartphone com acesso à internet para usar todos os recursos da aplicação.</p>

## 7 <a name="7">Requisitos do Produto</a>

### 7.1 <a name="7.1">Lista de categorias dos requisitos do produto:</a>

|**Prioridade**|**Descrição**|
|:-|:-|
| Alta| Requisito indispensável para o funcionamento do sistema|
| Média| Requisito importante, mas a sua não implementação não compromete o funcionamento da aplicação |
| Baixa| Requisito não usado com muita frequência e não é tão necessário para a satisfação do usuário com o projeto |

