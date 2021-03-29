# Politica de Criação de Branchs

## Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
03/03|0.1|Abertura do documento com template inicial|Rafael e Roberto|
03/03|0.2|Adição dos tópicos 1,2 e dos subtópicos de 2|Rafael e Roberto|

---

## 1. <a name="1">Introdução</a>
<p align = "justify"> &emsp;&emsp; Esse documento tem por objetivo padronizar a criação de branchs no repósitorio do Anunbis. Dessa forma, se torna indispensável a presença da issue, funcionalidade aos quais a branch se refere. </p>

## 2. <a name="2">Branchs Principais</a>
### 2.1 <a name="2.1">Master</a>
<p align = "justify"> &emsp;&emsp; Essa é a branch que contém o código mais estável do Anunbis. Tudo que o usuário consome da versão atual está aqui. As diretrizes dela são:</p>

* Só existe <b>uma master</b> no projeto;
* Commits não são permitidos <b>diretamente</b> nessa branch;
* Mudanças nela só ocorrem por meio de pull requests das branchs <b>release</b> e <b>hotfix</b>.

### 2.2 <a name="2.2">Develop</a>
<p align = "justify"> &emsp;&emsp; Destinada ao desenvolvimento do projeto. Ou seja, toda novidade está nessa branch. Suas diretrizes são:</p>

* Só existe uma branch <b>develop</b> no projeto;
* Deve ser sincronizada com todas as outras branchs;
* Deve ser derivada da master.

### 2.3 <a name="2.3">Document</a>
<p align = "justify"> &emsp;&emsp; Destinada à criação e manutenção dos documentos do projeto, ou seja, toda alteração na gitpage, local principal dos documentos, passa por essa branch. Diretrizes:</p>

* Deve ser derivada da <b>develop</b>;
* Deve ser mesclada a <b>develop</b> aṕos documento ser concluído;
* Seu nome segue o padrão:

```
document/issueID-Nome_da_Funcionalidade
```

<p align = "justify">&emsp;&emsp;Onde:</p>

* <b>"document"</b> é padrão;
* <b>"issueID"</b> é o número da issue ao qual o documento se refere;

<p align = "justify">&emsp;&emsp;Exemplo:</p>

```
document/#88-Atualizar_Roadmap
```

### 2.4 <a name="2.4">Feature</a>
<p align = "justify"> &emsp;&emsp; Destinada à criação de uma novas funcionalidades ao projeto. Diretrizes:</p>

* Deve ser derivada da <b>develop</b>
* Deve ser mesclado de volta a <b>develop</b> após a funcionalidade ser desenvolvida;
* Toda nova funcionalidade tem sua própria branch, seguindo o seguite padrão de nome:

```
feature/issueID-Nome_da_Funcionalidade
```

<p align = "justify">&emsp;&emsp;Onde:</p>

* <b>"feature"</b> é padrão;
* <b>"issueID"</b> é o número da issue ao qual a funcionalidade se refere;

<p align = "justify">&emsp;&emsp;Exemplo:</p>

```
feature/#55-Criar_Feed_de_Notícias
```


### 2.5 <a name="2.5">Release</a>
<p align = "justify"> &emsp;&emsp; Branch que contém um conjunto de funcionalidades que podem ser implementadas na <b>master</b>. Diretrizes:</p>

* Deve ser derivada da <b>develop</b>;
* Após ser concluída deve ser mesclada na <b>master</b>;
* Nenhuma nova funcionalidade pode ser inserida na <b>master</b> se não por meio da <b>release</b>;
* Somente aceita mesclagens do tipo <b>bugfix</b>;
* A cada nova <b>release</b>, o número do extremo esquerdo deve ser incrementado em 1;
* O nome dessa branch deve seguir o padrão:

```
release/vNúmero.versão
```

<p align = "justify">&emsp;&emsp;Onde:</p>

* <b>"release"</b> é padrão;

<p align = "justify">&emsp;&emsp;Exemplo:</p>

```
release/v2.5
```

### 2.6 <a name="2.6">Bugfix</a>
<p align = "justify"> &emsp;&emsp; Branch destinada a resolver problemas como bugs e erros presentes na <b>release</b>. Diretrizes:</p>

* Deve ser derivada da <b>release</b>;
* Deve ser mesclada a release depois de finalizada;
* Seu nome segue o seguinte padrão:

```
bugfix/issueID-Nome_do_bugfix
```

<p align = "justify">&emsp;&emsp;Onde:</p>

* <b>"bugfix"</b> é padrão;
* <b>"issueID"</b> é número da issue ao qual o bugfix se relaciona;

<p align = "justify">&emsp;&emsp;Exemplo:</p>

```
bugfix/#89-Resolver_Feed_de_Noticias
```

### 2.7 <a name="2.7">Hotfix</a>
<p align = "justify"> &emsp;&emsp; Destinada a resolver problemas urgentes na <b>master</b>. Diretrizes:</p>

* Deve ser derivada da <b>master</b>;
* Dever ser mesclada a <b>master</b> e a <b>develop</b> apos ser concluida;
* A cada novo <b>hotfix</b>, a versão do produto deve ser modificado, incrementando uma unidade ao número extremo direito.
* O nome segue o seguinte padrão:

```
hotfix/vNúmero.Versão
```

<p align = "justify">&emsp;&emsp;Onde:</p>

* <b>"hotfix"</b> é padrão;

<p align = "justify">&emsp;&emsp;Exemplo:</p>

```
hotfix/v2.6
```
## 3. <a nome="3">Referências</a>
GABRIEL, Enzo; et al. Política de Branches - Vamos Cuidar. Disponível em: <https://fga-eps-mds.github.io/2020.1-VC_Usuario/#/docs/policies/branches>. Acesso em: 03 mar 2021.