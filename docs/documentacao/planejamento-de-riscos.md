## Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
08/03|0.1|Abertura do Documento |Rafael|
08/03|0.2|Criação da Tabela de Riscos |Rafael|

## 1 <a name="1">Introdução</a>

<p align="justify"> &emsp;&emsp;O Plano de Gerenciamento de Riscos tem por objetivo a identificação, análise e planejamento de medidas para os possíveis riscos que o projeto pode enfrentar. Após planejado, possibilita a tomada de ações de tratamento de maneira mais trivial.</p>

## 2 <a name="2">Estrutura Analítica de Riscos (EAR)</a>

<p align="justify"> &emsp;&emsp; É uma ferramenta responsável por agrupar as possíveis causas dos riscos facilitando reconhecimentos, tratamentos e o processo de mitigação de riscos. Busca especificação mostrando as principais categorias de risco, garantindo ganho de tempo na identificação. </p>

### 2.1 <a name="2.1">Categoria dos riscos</a>

* **Técnico**: São os riscos associados à tecnologia, requisitos, qualidade e complexidade.
* **Externo**: São os riscos relativos ao cliente, mercado ou ambiente.
* **Organizacional**: São os riscos relacionados à priorização, dependências e recursos do projeto.
* **Gerência**: São os riscos relativos à estimativa, planejamento, controle e comunicação.

## 3 <a name="3">Análise Quantitativa</a>

### 3.1 <a name="3.1">Probabilidade</a>

|Probabilidade|Intervalo|Peso|
|:--|:----:|:----:|
|**Muito Baixa**|1 a 10|1|
|**Baixa**|11 a 30|2|
|**Média**|31 a 50|3|
|**Alta**|51 a 65|4|
|**Muito Alta**|66 a 99|5|

### 3.2 <a name="3.2">Impacto</a>

|Impacto|Descrição|Peso|
|:--|:-----:|:------:|
|**Muito Baixo**|Impacto pouco expressivo no desenvolvimento do projeto|1|
|**Baixo**| Pouco impacto no desenvolvimento do projeto|2|
|**Médio**| Possui certo impacto porém é facilmente recuperado|3|
|**Alto**| Há grande impacto no desenvolvimento do projeto|4|
|**Muito Alto**| O impacto inviabiliza o desenvolvimento projeto| 5|

### 3.3 <a name="3.3">Prioridade</a>

<p align="justify"> &emsp;&emsp; Se baseando com os valores do impacto e de probabilidade calcula-se a prioridade dos riscos. O que determina a urgência e prioridade dos riscos. </p>

|Probabilidade/Impacto|Muito Baixa|Baixo|Média|Alta|Muito Alta|
|:--|:-----:|:------:|:------:|:------:|:------:|
|**Muito Baixa**|1|2|3|4|5|
|**Baixa**|2|4|6|8|10|
|**Média**|3|6|9|12|15|
|**Alta**|4|8|12|16|20|
|**Muito Alta**|5|10|15|20|25|

Sendo:

* Prioridade de 1 a 5: Muito Baixa
* Prioridade de 6 a 10: Baixa
* Prioridade de 11 a 15: Média
* Prioridade de 16 a 20: Alta
* Prioridade de 21 a 25: Muito Alta

## 4 <a name="4">Identificação dos Riscos</a>
<p align="justify"> &emsp;&emsp; Para a identificação de riscos, adotou-se a comparação análoga - utilizando experiências anteriores e similares para facilitar a concepção e identificação de riscos comuns a esse tipo de projeto.</p>

### 4.1 <a name="4.1">Tabela de Riscos levantados</a>

|Risco| Descrição|	Ação Preventiva|	Ação Reativa|Categoria	|Probabilidade	|Impacto|	Prioridade|
|:----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|**R01**|Dificuldades da equipe com as novas tecnologias inseridas|Criação de tarefas de estudo|Solicitar ajuda de membros com maior conhecimento|Técnico|4|5|21|
|**R02**|Baixa produtividade dos integrantes do time|Motivação do time e reuniões constantes para maior integração|	Conversas específicas com o membro desmotivado para contornar o problema|Gerência|3|4|14|
|**R03**|Conflito entre entregas das disciplinas|Organização das tarefas para não haver choque de entrega|Redistribuir tarefas diminuindo o tamanho da sprint|Externo|5|4|10|
|**R04**|Falta dos membros durante Daily e reunião de planejamento|Definir datas, horários e plataformas que sejam acessíveis a todos|Verificar o motivo da falta e tratá-lo com urgência|Gerência|4|5|13|
|**R05**|Desistência da disciplina.|Estimular a máxima participação dos membros da equipe|Redistribuir melhor tarefas e estimular a interação|Gerência|1|5|8|
|**R06**|Falta de um grupo de EPS para gerenciar o grupo e não ter uma boa gestão|Não há ação a ser feita|Consultar pessoas mais experientes em casos de dúvidas e aprender metodologias de gerência|Organizacional|3|4|20|
|**R07**|Alteração no escopo|Documentar e refinar de forma constante os requisitos|	Planejar corretamente a sprint e se manter atualizado quanto às novas funcionalidades que serão adicionadas ao projeto|Gerência|5|4|18|
|**R08**|Alteração no cronograma da disciplina|Não há nenhuma ação a ser feita|Redefinir cronograma do time|Externo|1|4|6|
|**R09**|Alguns dos membros contrair Covid-19 ou outra doença|Seguir as recomendações do Ministério da Saúde|Distribuir as tarefas do enfermo para outras pessoas do time|Externo|3|4|22|
|**R10**|Alteração das tecnologias|Definição concisa do escopo do projeto|Planejar corretamente a sprint e se manter atualizado quanto às novas funcionalidades|Técnico|4|5|18|
|**R11**|Falta de cliente real|	Utilização de ferramentas que ajudem a levantar requisitos|	Utilização de dados levantados por usuários que sejam o público alvo do projeto|Externo|5|2|8|
|**R12**|Atraso nas entregas das sprints|Planejamento viável e conciso|Redistribuição das tarefas que precisam ser entregues|Gerência|3|3|12|

## 5 <a name="5">Referências</a>

* RODRIGUES, Eli. EAR para projetos de software. Disponível em <https://www.elirodrigues.com/2013/09/21/gerenciamento-de-riscos-ear-para-projetos-de-software/>. Acesso em 9 mar 2021.

* FREITAS, Renata. Aplique o Plano de Gerenciamento de Riscos no seu negócio. Disponível em: <https://www.glicfas.com.br/plano-de-gerenciamento-de-riscos/>. Acesso em 8 mar 2021.

* FREITAS, Renata. Aplique o Plano de Gerenciamento de Riscos no seu negócio. Disponível em: <https://www.glicfas.com.br/estrutura-analitica-de-riscos-2/>. Acesso em 8 mar 2021.

* SIQUEIRA, Lucas; OLIVEIRA, Caio. Plano de Gerenciamento de Riscos do grupo +Monitoria. Disponível em: <https://fga-eps-mds.github.io/2019.1-MaisMonitoria/docs/plano-riscos>. Acesso em 8 mar 2021.

* JOÃO, Lucas. Plano de Gerenciamento de Riscos do grupo ArBC. Disponível em: <https://jlucassr.github.io/ArBC-Pages/Plano-Gerenciamento-Riscos/>. Acesso em 9 mar 2021.

* DIAS, Emily. Plano de Gerenciamento de Riscos do grupo VC_Usuario. Disponível em: <https://fga-eps-mds.github.io/2020.1-VC_Usuario/#/docs/Plano_riscos?id=riscos-levantados>. Acesso em 9 mar 2021.

