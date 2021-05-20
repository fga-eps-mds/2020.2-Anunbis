## Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
08/03|0.1|Abertura do Documento |Rafael|
08/03|0.2|Criação da Tabela de Riscos |Rafael|
03/05|0.3|Alteração da tabela e inserção do tópico de burndown de riscos| Rafael e Roberto
03/05|0.4|Adição da tabela de burndown de riscos| Rafael e Roberto


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

## 4 <a name="4">Identificação dos Riscos</a>
<p align="justify"> &emsp;&emsp; Para a identificação de riscos, adotou-se a comparação análoga - utilizando experiências anteriores e similares para facilitar a concepção e identificação de riscos comuns a esse tipo de projeto. Sendo esses riscos passíveis de alteração durante o decorrer do projeto.</p>

### 4.1 <a name="4.1">Tabela de Riscos levantados</a>

|Risco| Descrição|Ação Preventiva|Ação Reativa|Categoria	|
|:----:|:-----:|:-----:|:-----:|:-----:|
|**R01**|Dificuldades da equipe com as novas tecnologias inseridas|Criação de tarefas de estudo|Solicitar ajuda de membros com maior conhecimento|Técnico|
|**R02**|Baixa produtividade dos integrantes do time|Motivação do time e reuniões constantes para maior integração|	Conversas específicas com o membro desmotivado para contornar o problema|Gerência|
|**R03**|Conflito entre entregas das disciplinas|Organização das tarefas para não haver choque de entrega|Redistribuir tarefas diminuindo o tamanho da sprint|Externo|
|**R04**|Falta dos membros durante Daily e reunião de planejamento|Definir datas, horários e plataformas que sejam acessíveis a todos|Verificar o motivo da falta e tratá-lo com urgência|Gerência|
|**R05**|Desistência da disciplina.|Estimular a máxima participação dos membros da equipe|Redistribuir melhor tarefas e estimular a interação|Gerência|
|**R06**|Falta de um grupo de EPS para gerenciar o grupo e não ter uma boa gestão|Não há ação a ser feita|Consultar pessoas mais experientes em casos de dúvidas e aprender metodologias de gerência|Organizacional|
|**R07**|Alteração no escopo|Documentar e refinar de forma constante os requisitos|	Planejar corretamente a sprint e se manter atualizado quanto às novas funcionalidades que serão adicionadas ao projeto|Gerência|
|**R08**|Alteração no cronograma da disciplina|Não há nenhuma ação a ser feita|Redefinir cronograma do time|Externo|
|**R09**|Alguns dos membros contrair Covid-19 ou outra doença|Seguir as recomendações do Ministério da Saúde|Distribuir as tarefas do enfermo para outras pessoas do time|Externo|
|**R10**|Alteração das tecnologias|Definição concisa do escopo do projeto|Planejar corretamente a sprint e se manter atualizado quanto às novas funcionalidades|Técnico|
|**R11**|Falta de cliente real|	Utilização de ferramentas que ajudem a levantar requisitos|	Utilização de dados levantados por usuários que sejam o público alvo do projeto|Externo|
|**R12**|Atraso nas entregas das sprints|Planejamento viável e conciso|Redistribuição das tarefas que precisam ser entregues|Gerência|

## 5 <a name="5">Burndown de Riscos</a>

<p align="justify"> &emsp;&emsp; Para o burndown de riscos, adotamos uma planilha compartilhada para servir como referência de cálculo de <u>Probabilidade</u> e <u>Impacto</u> para cada sprint do projeto. A intenção é gerar um gráfico baseado nesses dados que sejam de fácil entendimento para uma melhor análise de como esses riscos se comportam ao decorrer do projeto, e como o grupo está lidando com eles.</p>

A tabela com os riscos se encontra abaixo:

<iframe width="600" height="400" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQmkncJgu0YbqaXA8M-tPzSmEj5juXb-Tr1xBS9Z3ljDYItNyTJSyDyuC9cjgl4u8ggpbBpKNGxvstX/pubchart?oid=600106509&amp;format=interactive"></iframe>

Os dados foram retirados da [planilha de gerenciamento de riscos](https://docs.google.com/spreadsheets/d/12WXr3bNG4Uke4vPLeR_h7lxr0sZETEj1ElInSU8CiWs/edit?usp=sharing).

## 6 <a name="6">Referências</a>

* RODRIGUES, Eli. EAR para projetos de software. Disponível em <https://www.elirodrigues.com/2013/09/21/gerenciamento-de-riscos-ear-para-projetos-de-software/>. Acesso em 9 mar 2021.

* FREITAS, Renata. Aplique o Plano de Gerenciamento de Riscos no seu negócio. Disponível em: <https://www.glicfas.com.br/plano-de-gerenciamento-de-riscos/>. Acesso em 8 mar 2021.

* FREITAS, Renata. Aplique o Plano de Gerenciamento de Riscos no seu negócio. Disponível em: <https://www.glicfas.com.br/estrutura-analitica-de-riscos-2/>. Acesso em 8 mar 2021.

* SIQUEIRA, Lucas; OLIVEIRA, Caio. Plano de Gerenciamento de Riscos do grupo +Monitoria. Disponível em: <https://fga-eps-mds.github.io/2019.1-MaisMonitoria/docs/plano-riscos>. Acesso em 8 mar 2021.

* JOÃO, Lucas. Plano de Gerenciamento de Riscos do grupo ArBC. Disponível em: <https://jlucassr.github.io/ArBC-Pages/Plano-Gerenciamento-Riscos/>. Acesso em 9 mar 2021.

* DIAS, Emily. Plano de Gerenciamento de Riscos do grupo VC_Usuario. Disponível em: <https://fga-eps-mds.github.io/2020.1-VC_Usuario/#/docs/Plano_riscos?id=riscos-levantados>. Acesso em 9 mar 2021.

