# Política de commits

## Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
03/03|0.1|Abertura do documento com template inicial|Rafael e Roberto|
05/03|0.2|Alteração da politica de commits| Rafael|

---

Regras para efetuar um commit no repositório:

* Commits devem ser redigidos em português no gerúndio.
* Devem ser simples e concisos, possuindo títulos curtos de no máximo 72 caracteres.
* Devem ser compostos por (#NUMERO_DA_ISSUE) + MENSAGEM.

<b>Exemplo: </b>

``` 
(#28) Criando documento de visão.
```

* Caso 2 ou mais pessoas tenham feito o trabalho, basta incluir a instrução ```Co-authored-by:```  na mensagem, para que eles sejam incluidos como contribuintes no gráfico de commits do GitHub.

<b>Exemplo: </b>

```
(#28) Criando documento de visão.
Co-authored-by: Roberto Mangabeira <robertosantana2001@gmail.com>
Co-authored-by: Rafael Cleydson <rafael.cleydson@gmail.com>"
```