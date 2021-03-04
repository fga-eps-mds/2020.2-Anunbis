# Política de commits

---

* Commits devem ser redigidos em português no gerúndio.
* Devem ser simples e concisos, possuindo títulos curtos de no máximo 72 caracteres.
* Devem ser compostos por #NUMERO_DA_ISSUE + MENSAGEM.

<b>Exemplo: </b>

``` 
#28 Criando documento de visão.
```

* Caso 2 ou mais pessoas tenham feito o trabalho, basta incluir a instrução ```Co-authored-by:```  na mensagem, para que eles sejam incluidos como contribuintes no gráfico de commits do GitHub.

<b>Exemplo: </b>

```
$ git commit -m "#28 Criando documento de visão.
>Co-authored-by: Roberto Mangabeira <robertosantana2001@gmail.com>
>Co-authored-by: Rafael Cleydson <rafael.cleydson@gmail.com>"
```