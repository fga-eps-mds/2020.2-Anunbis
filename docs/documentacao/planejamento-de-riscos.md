## Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
08/03|0.1|Abertura do Documento |Rafael|

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
|**Muito Baixa**|0 a 10|1|
|**Baixa**| 11 a 30|2|
|**Média**| 31 a 50|3|
|**Alta**| 51 a 65|4|
|**Muito Alta**| 65 a 100| 5|

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
|**Muito Baixa**|1|2|	3|	4|	5|
|**Baixa**| 2|4	|6	|8	|10|
|**Média**| 3|6|	9	|12|	15|
|**Alta**| 4| 8	|12	|16|	20|
|**Muito Alta**| 5| 	10|	15	|20	|25|

Sendo:

* Prioridades de 1 a 5: Muito Baixa
* Prioridade de 6 a 10: Baixa
* Prioridade de 11 a 15: Média
* Prioridade de 16 a 20: Alta
* Prioridade de 21 a 25: Muito Alta
