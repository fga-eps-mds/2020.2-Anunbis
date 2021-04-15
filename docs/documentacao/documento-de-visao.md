## Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
17/02|0.1|Abertura do Documento de Visão| Equipe|
04/03|0.2|Adição dos itens 5, 6 e 7| Roberto|
26/03|0.2|Atualizando contéudo da página| Rodrigo|
13/04|0.3|Refatorando Descrição dos usuários e envolvidos| Equipe|
13/04|0.4|Revisão da Introdução e Posicionamento| Equipe|
14/04|0.5|Revisão da Visão Geral do Produto| Rafael e Victor|
14/04|0.6|Revisando Recursos do produto| Rafael e Victor|


## 1. <a name="1">Introdução</a>

### 1.1 <a name ="1_1">Propósito</a>

<p align="justify"> &emsp;&emsp; Este documento tem por objetivo estabelecer um posicionamento sobre a aplicação, suas características e seu desenvolvimento em questão. Também definindo seus requisitos em termos de necessidade para usuários finais.</p>

### 1.2 <a name="1_2">Escopo</a>

<p align="justify"> &emsp;&emsp; Um dos fatores que definem o sucesso acadêmico de um estudante da Universidade de Brasília são seus professores, pois, dependendo deles, o aluno terá uma experiência diferente em relação à disciplina. Alguns professores cobram mais e outros menos, de fato o aprendizado de um estudante não depende apenas dele mesmo e sim de um conjunto de aspectos incluindo o seu professor. </p>

<p align="justify"> &emsp;&emsp; Sendo o foco desse projeto, ajudar os alunos e os professores. Os alunos serão capazes de escolher professores com metodologias de ensino mais compatíveis com os próprios objetivos, e os professores receberão um fluxo de feedback contínuo em relação á sua forma de ensino. Assim ambos entrarão em um ciclo colaborativo que irá beneficiar todos na UnB. </p>

### 1.3 <a name=1_3>Definições, acrônimos e abreviações</a>

Tópico destinado as definições, acrônimos e abreviações dos termos usados neste documento, visando facilitar o compreendimento do público interessado no projeto

|Siglas, Acrônimos|Definição|
--|--
|**FGA**| Faculdade do Gama 
|**UnB**| Universidade de Brasília
|**MDS**| Métodos de Desenvolvimento de Software
|**CPA**| Comissão própria de AutoAvaliação

## 2. <a name="2">Posicionamento</a>
<p align="justify">&emsp;&emsp; A maior parte dos estudantes entram na universidade com um grande anseio por conhecimento, porém com o tempo, esse desejo acaba sendo anulado por professores que não possuem uma boa didática, ou não se dedicam a ajudar o estudante, ou apenas docentes que possuem uma metodologia que não é compatível à alguns dos alunos.</p>

<p align="justify">&emsp;&emsp; Além de que, por outro lado, muitos professores querem ajudar os estudantes o máximo possível, porém não possuem informações bem definidas de como evoluir suas metodologias, tendo que se apoiar a formas empíricas de tentativa e erro, para assim, tentar descobrir o que melhor funciona na disciplina que ministra. </p>

<p align="justify">&emsp;&emsp; Neste sentido, este programa visa produzir um ambiente no qual ambas as partes possam se beneficiar. </p>


### 2.1 <a name="2_1">Oportunidade de negócio</a>

<p align="justify">&emsp;&emsp; O projeto dá ao aluno a opção de escolher com mais segurança o professor com o qual deseja aprender naquele semestre, baseando-se na análise de quem já teve alguma experiência com esse docente. Do mesmo modo que, o professor passa a receber todos os semestres um feedback em relação a sua forma de ensino, podendo assim melhorar os pontos que forem sendo apontados pelos seus antigos alunos.</p>

### 2.2 <a name="2_2">Descrição do problema</a>

|*Questão*|*Informações do Produto*|
|:-|:-|
|*O Problema é*|Aluno com falta de conhecimento prévio sobre os professores e as disciplinas/ Professor com dificuldade em evoluir a própria metodologia de ensino.|
|*Que afeta*|A comunidade acadêmica. |
|*Cujo impacto é*|O aluno não encontrar uma metodologia de ensino compatível com si mesmo/ O professor não conseguir melhorar sua forma de ensino.|
|*Uma boa solução seria*|Uma aplicação que permita os alunos compartilharem entre si as experiências com as disciplinas e professores/ Uma aplicação que permite os professores receberem feedback sobre sua forma de ensino.|

### 2.3 <a name="2_3">Descrição da Posição do Produto</a>

<p align="justify">&emsp;&emsp;A aplicação, quando desenvolvida, se posicionará como uma aplicação web que pode ser usada facilmente em navegadores mobile proporcionando uma experiência muito parecida a de um app nativo. Isso proporciona que os alunos troquem experiências de suas disciplinas realizadas de forma eficiente e rápida, possibilitando que os alunos encontrem metodologias de ensino compatíveis com si mesmo.</p>

## 3. <a name="3">Descrição dos Usuários e Envolvidos</a>

### 3.1 <a name="3.1">Descrição dos Usuários</a>
|**Nome**|**Descrição**|
|:-|:-|
| Estudantes da UnB| Estudantes buscando prévio conhecimento sobre disciplinas/professores. |
|Professores da UnB| Professores com desejo de melhorar a própria metodologia e entender como sua aula impacta os alunos. |

### 3.2 <a name="3.2">Descrição dos Envolvidos</a>
|**Nome**|**Descrição**|**Responsabilidade**|
|:-:|:-:|:-:|
| Equipe de MDS (Desenvolvedores)| Estudantes da Disciplina MDS da UnB FGA |Criar e manter documentos;<br /> Desenvolver e testar o software; <br /> Tomar decisões a respeito do produto.|
|Avaliadores| Professores e monitores das disciplinas de MDS. |Avaliar e conceder feedback sobre a qualidade do projeto desenvolvido pelos alunos de MDS|

### 3.3 <a name="3.3">Principais Necessidades dos Usuários</a>
|**Usuário**|**Necessidade**|**Solução Atual**|**Solução Proposta**|
|:-:|:-:|:-:|:-:|
| Estudantes da UnB| Escolher uma metodologia de ensino que melhor se adequa e fornecer feedback para os professores | Avaliação institucional; Grupo no facebook feito por alunos; Conversas informais com colegas | Website para submeter avaliações e comentários sobre a experiência do aluno com a metologia do professsor avaliado |
|Professores da UnB| Interesse de professores com desejo de melhorar a própria metodologia e entender como sua aula impacta os alunos. |  Avaliação institucional; Conversas e/ou questionários informais sobre a disciplina | Website para visualizar avaliações e comentários sobre a experiência de alunos com a metodologia do professsor avaliado |

### 3.4 <a name="3.4">Perfis dos Envolvidos</a>
#### 3.4.1 <a name="3.4.1">Equipe de Desenvolvimento de Software</a>
|**Representantes**|**Tipo**|**Responsabilidade**|**Critério de Sucesso**|**Envolvimento**|
|:---:|:-:|:-:|:-:|:-:|
|Eduardo Afonso Dutra Silva; Rafael C. da S. Ramos; Roberto M. Santana; Rodrigo B. A. de Brito; Thiago S. de Paiva; Victor H. Carvalho|Estudantes da disciplina de MDS da FGA|Criar e manter documentos; Desenvolver e testar o software; Tomar decisões a respeito do produto.|Concluir o projeto proposto dentro do periodo estipulado atendendo à todos os requisitos|Alto

#### 3.4.2 <a name="3.4.2">Avaliadores e Monitores</a>
|**Representantes**|**Tipo**|**Responsabilidade**|**Critério de Sucesso**|**Envolvimento**|
|:---:|:-:|:-:|:-:|:-:|
| Carla Rocha e Sérgio Cipriano | Professora e monitor de MDS na UnB FGA | Avaliar o projeto e desenvolvedores do produto | Lecionar sobre matérias e ferramentas para o desenvolvimento e contribuição em projetos de software Open Source |Baixo

### 3.5 <a name="3.5">Perfis dos Usuários</a>
#### 3.5.1 <a name="3.5.1">Estudantes da UnB</a>
|**Representantes**|**tipo**|**Responsabilidade**|**Critério de sucesso**|**Envolvimento**|
|:-:|:-:|:-:|:-:|:-:|
| Interessados em ajudar outros estudantes, além de visualizar avaliações | Estudantes matriculados na UnB | Disponibilizar por meio de comentários e notas um feedback para os professores da UnB e auxiliar os alunos a escolher a melhor metodologia para ele | Conseguir ajudar os professores a tentarem melhorar seus métodos de ensino e alunos a escolherem docentes com técnicas que possam se adaptar melhor | Alto 

#### 3.5.2 <a name="3.5.2">Professores da UnB</a>
|**Representantes**|**tipo**|**Responsabilidade**|**Critério de sucesso**|**Envolvimento**|
|:-:|:-:|:-:|:-:|:-:|
| Interessados em receber feedbacks sobre seu trabalho e melhorá-lo | Professores da UnB | Visualizar avaliações e comentários sobre sua metodologia e tentar melhorá-la | Conseguir a cada semestre um maior número de aprovação por parte dos estudantes e consequentemente melhores avaliações | Médio 


### 3.6 <a name="3.6">Alternativas e Concorrências</a>
#### 3.6.1 <a name="3.6.1">Grupos do Facebook</a>
<p align="justify"> &emsp;&emsp; Utilizando a plataforma do facebook os estudantes são capazes de criar grupos para debater sobre suas experiências com os professores. Porém, além de existirem vários grupos diferentes com a mesma temática, todos eles necessitam que um membro daquele grupo aceite o pedido do usuário que deseja entrar no grupo, e só assim o usuário tem acesso ao conteúdo. Entretanto, por existirem diversos grupos com a mesma temática, as informações acabam se tornando escassas ou defasadas em cada grupo, necessitando de uma busca profunda para encontrar qualquer informação. O que também não ajuda os professores, pois também possuem dificuldade encontrar informações sobre suas metodologias ou até de ter acesso a esses grupos. </p>

#### 3.6.2 <a name="3.6.2">Avaliação Institucional</a>
<p align="justify"> &emsp;&emsp; As avaliações instucionais é uma ferramenta da própria UnB conduzida pela CPA para fornecer o feedback aos professores ao final de determinado semestre, porém, os alunos não têm acesso a tais avaliações mesmo elas sendo bem elaboradas devido as diferentes perguntas que acabam forçando os discentes a fazerem uma boa avaliação visando uma maior crítica construtiva aos professores. Então a príncipio parece ser um ambiente fechado, buscamos refatorar esse ambiente para trazer fácil acesso aos alunos e professores interessados nas avaliações, de maneira a mitigar ao máximo os comentários ofensivos e que não agregam valor a avaliação. </p>

## 4. <a name="4">Visão Geral do Produto</a>
### 4.1 <a name="4.1">Perspectivas</a>

<p align="justify"> &emsp;&emsp; A aplicação tem como objetivo criar um ambiente específico para que haja uma troca de informações entre os alunos da UnB a respeito dos professores e suas metodologias de ensino, tornando viável que qualquer aluno possa escrever suas próprias avaliações de maneira anônima ou não, e ler as avaliações feitas por outros alunos. Além de possibilitar que os professores tenham acesso a esses comentários, o que ajuda o professor a planejar melhor sua disciplina, melhorando sua metodologia e constribuindo na melhora da qualidade de ensino na UnB.
</p>

### 4.2 <a name="4.2">Resumo das capacidades</a>
|**Benefícios**|**Recurso de Suporte**|
|:-:|:-:|
| Facilidade em visualizar e cadastrar avaliações de professores/disciplinas.| A aplicação possui uma interface de fácil uso para visualizar essas avaliações, também conduz de maneira coerente e amigável o usuário para que ele realize boas avaliações.|  
|Disponibilização de feedbacks construtivos para os professores|A aplicação se encarrega de  disponibilizar uma interface de uso prático onde os professores podem visualizar feedbacks sobre seu ensino, bem como relatórios gerenciais que buscam otimizar as interpretações desses feedbacks.|

### 4.3 <a name="4.3">Funções do Produto</a>
<p align="justify"> &emsp;&emsp; 
O produto tem a função de ser um elo dos docentes com os discentes da UnB, facilitando uma resposta do aluno às técnicas e metodologia aplicada pelos seus professores, tornando mais fácil para esses profissionais uma adapção de sua maneira de ensino que melhor se adequa aos estudantes. Dentre as funcionalidades da aplicação estão, cadastro, login, avaliação, feed de postagens, gerenciamento de conta, entre outras.
</p>

### 4.4 <a name="4.4">Suposições e Dependências</a>
* Os usuários deverão ter um computador, celular ou tablet com acesso à internet para conseguir ter acesso à aplicação.
* A aplicação será usada por alunos e professores da UnB, para melhorar o ensino e aprendizagem do corpo docente/discente da universidade.
* A aplicação facilitará a realização e visualização de feedbacks aos professores, feitos por alunos.
## 5. <a name="5">Recursos do Produto</a>

### 5.1 <a name="5.1">Recursos dos Discentes</a>

<p align="justify"> &emsp;&emsp; Os alunos poderão se cadastrar na aplicação. Quando cadastrados e logados, poderão ter acesso aos seguintes recursos:</p>
 
* Fazer avaliação dos professores;
* Visualizar avaliações feitas sobre outros professores;
* Concordar ou discordar do comentário de outros discentes;
* Visualizar a quantidade de alunos que concordam e discordam desses comentários;
* Pesquisar os professores por ranking;
* Visualizar relatórios de avaliações;
* Denunciar avaliações ofensivas de outros alunos;

### 5.2 <a name="5.2">Recursos dos Docentes</a>

<p align="justify"> &emsp;&emsp; Os professores poderão também se cadastrar na aplicação. Quando cadastrados e logados, terão acesso às seguintes funcionalidades:</p>

* Visualizar o feedback dos estudantes;
* Visualizar a sua pontuação na aplicação;
* Denunciar avaliações ofensivas feitas por alunos;
* Visualizar relatórios de avaliações;
### 5.3 <a name="5.3">Disponibilizar informações do projeto</a>
<p align="justify"> &emsp;&emsp;
Antes de ter acesso às páginas de cadastro e login, possíveis usuários ou contribuidores devem poder visualizar as informações gerais do projeto, suas ideias e objetivos, além dos meios de contato dos gerênciadores do projeto, como também o repositório do mesmo no github e toda a documentação da aplicação, pois por se tratar de um projeto de software Open Source esses dados são de extrema importância para a comunidade.
</p>


## 6. <a name="6">Restrições</a>

### 6.1 <a name="6.1">Restrições de Implementação</a>

<p align="justify">&emsp;&emsp;O sistema será implementado usando ReactJS, Flask e Python, e será desenvolvido de forma remota devido à pandemia.</p>

### 6.2 <a name="6.2">Restrições Externas</a>
<p align="justify">&emsp;&emsp;O grupo não tem muita experiência com as tecnologias utilizadas.</p>

### 6.3 <a name="6.3">Restrições de Design</a>
<p align="justify"> &emsp;&emsp;Toda experiência com a aplicação deve ser limpa e natural. O usuário não deve ter dificuldades de entender o que ele pode fazer, e como encontrar determinada funcionalidade. Além disso, a aplicação será destinada aos usuários web.</p>

### 6.4 <a name="6.4">Restriçõs de Uso</a>
<p align="justify"> &emsp;&emsp;É necessário que os usuários (a comunidade acadêmica) tenham acesso à um computador ou smartphone com acesso à internet para usar todos os recursos da aplicação.</p>

## 7. <a name="7">Requisitos do Produto</a>

### 7.1 <a name="7.1">Lista de categorias dos requisitos do produto:</a>

|**Prioridade**|**Descrição**|
|:-|:-|
| Alta| Requisito indispensável para o funcionamento do sistema|
| Média| Requisito importante, mas a sua não implementação não compromete o funcionamento da aplicação |
| Baixa| Requisito não usado com muita frequência e não é tão necessário para a satisfação do usuário com o projeto |

### 7.2 <a name="7.2">Lista de Requisitos:</a>

|**Identificador**|**Requisito**|**Prioridade**|
|:-|:-|:-|
| RF01| Permitir que o usuário crie uma conta, edite, faça login e a delete| Alta|
| RF02| Permitir que o usuário pesquise professores| Alta|
| RF03| Permitir que o usuário discente crie uma avalição e a delete| Alta|
| RF04| Permitir que o aluno concorde ou discorde do comentário de outro aluno| Alta|
| RF05| Exibir pontuação média e rank dos professores para todos os usuários | Alta|
| RF06| Permitir que os discentes façam avaliações anônimas | Média|
| RF07| Exibir quantidade de avaliações que o usuário discente já realizou| Média|
| RF08| A aplicação deve ter a experiência de uso simples e fluída, de linguagem fácil intuitiva| Alta|
| RF09| Permitir o usuário a denunciar um comentário| Média|
| RF10| Permitir que o docente veja as avaliações sobre si mesmo| Média|  
| RF11| Exibir ao aluno a quantidade de pessoas que concordam e discordam dos seus comentários| Baixa|  

## 8. Referências

CARVALHO, Durval; et al. Documento de Visão - Acacia. Disponível em: <https://fga-eps-mds.github.io/2019.2-Acacia/#/vision_documents>. Acesso em: 04 mar 2021.

FÉLIX, Bruno; et al. Documento de Visão - Vamos Cuidar. Disponível em: <https://fga-eps-mds.github.io/2020.1-VC_Usuario/#/docs/Documento_de_Visao>. Acesso em: 04 mar 2021.

LUCAS, Jõao; et al. Documento de Visão - ArBC. Disponível em: <https://jlucassr.github.io/ArBC-Pages/mds/Documento_de_visao/>. Acesso em: 04 mar 2021.