## Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
28/02|0.1|Abertura do Documento de Metodologia|Rafael|
28/02|0.2|Descrição da metodologia Scrum|Rafael|
28/02|0.3|Descrição da metodologia XP|Roberto|
26/03|0.4|Descrição do Planning Poker|Rodrigo|



## 1. <a name="1">Introdução</a>

 <p align = "justify"> &emsp;&emsp; Essa documentação tem como finalidade fornecer uma descrição das metodologias adotadas na equipe para desenvolvimento do projeto. Sendo demonstrados inicialmente, um breve resumo sobre as metodologias usadas bem como as cerimônias/rituais realizados pela equipe. </p>


## 2. <a name="2">Metodologias utilizadas</a>

 <p align = "justify"> &emsp;&emsp; O time decidiu por utilizar uma abordagem híbrida de metodologias, com base no Scrum ,XP e o Planning Poker. A utilização de cerimônias/rituais e artefatos de diferentes metodologias proporciona a equipe um bom desenvolvimento em paralelo com diferentes práticas baseadas nas metodologias ágeis, dispondo de uma importante característica de resposta as mudanças dentro do processo de acordo com a necessidade do time.</p>

### 2.1 <a name="2.1">Scrum</a>
<p align = "justify"> &emsp;&emsp; Scrum é um framework utilizado para gestão dinâmica de projetos, surgiu em meados dos anos 90 e é amplamente utilizado no desenvolvimento de projetos que utilizam metodologias ágeis.  É um processo iterativo e incremental e possui 3 pilares centrais: <b>Transparência</b> dos processos, requisitos de entrega e status. <b>Inspeção</b> constante de tudo que está sendo feito. <b>Adaptação</b> tanto do processo, quanto do produto às mudanças.
</p>
<p align = "justify"> &emsp;&emsp; O Scrum possui algumas práticas fundamentais que são utilizadas no projeto. Sendo essas práticas divididas em <b>Papéis</b>, <b>Artefatos</b>, <b>Cerimônias</b> e <b>Ferramentas</b> que serão explicados posteriormente. Dos papéis foram utilizados o Scrum Master, Product Owner e o Development Team, sendo todos participantes do time de desenvolvimento e outros dois votados para incremento dos papéis restantes. No caso dos artefatos estão sendo utilizados o Product Backlog, Sprint Backlog,  Sprints e Sprint Review. Também estão sendo feitas todas as cerimônias de sprint planning onde é planejado o que será feito na próxima sprint, daily scrum que são as reuniões diárias realizadas no discord, sprint review que revisa o que aconteceu na sprint passada e retrospectiva que aponta o feedback do processo da sprint.
</p>

#### 2.1.1 <a name="2.1.1">Papéis do Scrum:</a>

* <b>ScrumMaster:</b> 
	É uma espécie de guardião do Scrum, coordena as rotinas e as atividades do grupo mantendo vivos os princípios e práticas do Scrum no dia-a-dia. É como um mentor, um facilitador para o trabalho que remove os impedimentos e refina os itens da próxima Sprint junto ao Product Owner.

* <b>Product Owner:</b>
	Guardião do Cliente, faz a ponte entre cliente-projeto e possui os poderes de liderança sobre o produto, realiza um escopo/base suficiente (decidindo quais recursos serão construídos, qual a ordem de prioridade de produção no Product Backlog) para haver um bom trabalho durante as sprints.

* <b>Dev Team:</b> 
Equipe desenvolvedora do projeto. É o team que define como as coisas serão feitas e quais/quantas tarefas são possíveis de entregar. O team se auto organiza para atingir as metas estabelecidas pelo Product Owner.

#### 2.1.2 <a name="2.1.2">Cerimônias e artefatos:</a>

* <b>Rotina:</b> 
</br>Sprint
</br>Planning -> Desenvolvimento -> Review -> Retrospective
</br>Daily
* <b>Planning:</b>
Reunião realizada antes do início de uma Sprint, onde é construído o Sprint Backlog. 
* <b>Desenvolvimento:</b> 
Desenvolver o que foi planejado no planning, sujeitando as mudanças;
* <b>Review:</b> 
Reunião que acontece após o término de cada Sprint para validar e adaptar o produto que está sendo construído. É nesse momento em que o Product Owner sugere mudanças e alterações que serão inseridas no product backlog por ordem de prioridade.
* <b>Retrospective:</b> 
Reunião final, em que todos podem e devem expor seu feedback do processo, verificando necessidades de adaptação a partir do que aconteceu de positivo e de negativo.
* <b>Daily:</b> 
Reuniões rápidas e constantes que atualizam a equipe sobre o que foi feito, o que tem que fazer e os problemas atuais, necessária transparência sobre.

#### 2.1.3 <a name="2.1.3">Ferramentas:</a>

* <b>Kanban board:</b> 
Quadro onde é possível visualizar o fluxo de trabalho que está sendo feito. Sendo realizado através de um software (ZenHub) que representam as histórias e funcionalidades do product backlog. São listados os itens que precisam ser executados, que estão sendo executados e que estão prontos. Também são listados os impedimentos e outras informações.

### 2.2 <a name="2.2">Extreme Programming - XP</a>
<p align = "justify"> &emsp;&emsp; Extreme Programming (XP) é uma metodologia ágil para pequenas e médias equipes que desenvolvem software baseado em requisitos vagos e que se modificam rapidamente. É um método que tem foco em feedback constante, abordagem incremental e comunicação.</p>
<p align = "justify"> &emsp;&emsp; O XP tem quatro <b>valores</b> muito importantes que ajudam o desenvolvimento ágil de um projeto e a <b>integração</b> da equipe, visto que esses dois fatores são muito importantes atualmente, pois a constante globalização exige entregas cada vez mais rápidas e, com isso, as equipes são constantemente mais exigidas. </p>
<p align = "justify"> &emsp;&emsp; Além disso, o XP também possui funções bem definidas para seus membros. Entretanto, nós já iremos usar os papéis do scrum. Por fim, a prática do Extreme Programming traz consigo várias técnicas das quais algumas serão usadas nesse projeto, como por exemplo, o pareamento.</p>

#### 2.2.1 <a name="2.2.1">Valores do XP</a>
* <b>Comunicação:</b> A má comunicação é motivo de insucesso em quase todo tipo de projeto, inclusive nos projetos de software. 
 <br/>

* <b>Simplicidade:</b> Manter a simplicidade é difícil, entretanto, possibilita que tudo esteja no controle. É um dos princípios do XP advindos do JIT.
<br>

* <b>Feedback:</b> Fator altamente importante nos dias atuais, pois permite que os erros e dificuldades sejam descobertos e tratados.
<br>

* <b>Coragem:</b> Este é o último valor do XP, mas não menos importante, pois é necessário ter coragem para testar novas ideias, substituir antigas, mudar o código, corrigir erros.
 <br>

#### 2.2.2 <a name="2.2.2">Pŕaticas do XP</a>
* <b>Pareamento:</b> Prática de programar a dois, de uma maneira que tenha 4 olhos olhando para o mesmo código evitando erros ou bugs.

### 2.3 <a name="2.3">Planning Poker</a>

<p align = "justify"> &emsp;&emsp; 
O planning poker é uma prática ágil gamificada para o grupo decidir o quão difícil é uma tarefa. Então, sempre que é necessário decidir tarefas para a sprint, é calculado o quanto de esforço deverá se colocado em cada tarefa, assim podemos medir melhor o nosso desempenho e o que somos capazes de fazer.
</p>

#### 2.3.1 <a name="2.3.1">Como funciona</a>
<p align = "justify"> &emsp;&emsp; 
	Primeiro é selecionada uma tarefa na qual está sendo planejado realizar, em seguida todos os integrantes do grupo devem escolher um número entre 1, 2, 3, 5, 8, 13, 21, 40, 100 ou ?.
</p>

<b>Classificação:</b><br>
<b>1, 2, 3:</b> A tarefa é fácil; <br>
<b>5:</b> A tarefa é de médio esforço; <br>
<b>8, 13:</b> A tarefa é difícil; <br>
<b>21, 40:</b> A tarefa é muito difícil; <br>
<b>100, ?:</b> É muito difícil mesmo, nem sei como estimar; <br>

<p align = "justify"> &emsp;&emsp; 
Após a escolha, todos os integrantes apresentam as cartas ao mesmo tempo.
Se os participantes tiverem escolhido valores diferentes, aqueles que escolheram os valores mais extremos deverão apresentar suas opiniões em relação a tarefa. Após debatido o assunto todos devem escolher novamente uma carta.
</p>

<p align = "justify"> &emsp;&emsp; 
Esse processo se segue até os números escolhidos tenham chegado a um valor em comum, se por acaso tiverem chegado a valores parecidos, porém não iguais, então o mais alto é escolhido.
</p>

<p align = "justify"> &emsp;&emsp; 
Se por acaso os valores continuam muito distantes, então a tarefa deve ser deixada em pausa e todos os integrantes devem procurar entender melhor sobre o assunto, e assim chegar a um consenso em uma próxima reunião.
</p>

