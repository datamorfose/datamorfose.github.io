---
title: "Fundamentos de Dados"
date: 2023-12-08T08:06:25+06:00
description: Sample post with multiple images, embedded video ect.
menu:
  sidebar:
    name: Fundamentos de Dados
    identifier: concursopublico-tecnologia-dados-fundamentos
    parent: concursopublico-tecnologia-dados
    weight: 1
hero: images/fundamentos.png
tags: ["Markdown","Content Organization","Multi-lingual"]
categories: ["Básico"]
---



## Introdução


Um VCS (sistema de controle de versão) é um programa ou um conjunto de programas que controla as alterações feitas em uma coleção de arquivos. Uma meta de um VCS é recuperar com facilidade as versões anteriores de arquivos individuais ou do projeto inteiro. Outra meta é permitir que vários membros da equipe trabalhem em um projeto, até mesmo nos mesmos arquivos, simultaneamente sem afetar uns aos outros.

Com o VCS, você pode:

- Ver todas as alterações feitas no projeto, quando as alterações foram feitas e quem as fez.
- Incluir uma mensagem com cada alteração para explicar o raciocínio por trás dela.
- Recuperar as versões anteriores de todo o projeto ou de arquivos individuais.
- Criar branches, em que as alterações podem ser feitas de maneira experimental. Esse recurso permite que vários conjuntos diferentes de alterações (por exemplo, recursos ou correções de bug) sejam trabalhados ao mesmo tempo, possivelmente por pessoas diferentes, sem afetar a ramificação principal. Posteriormente, você pode mesclar as alterações que deseja manter na ramificação principal.
- Anexar uma marca a uma versão, por exemplo, para marcar uma nova versão.
- O Git é um VCS rápido, versátil, altamente escalonável, gratuito e de software livre. O autor principal é Linus Torvalds, o criador do Linux.
  
<details>
<summary>TITLE</summary>

BODY CONTENT

</details>


### Terminologia

Para entender o Git, você precisa entender a terminologia. Veja a seguir uma breve lista dos termos usados com frequência pelos usuários do Git. Não se preocupe com os detalhes por enquanto. Todos esses termos passarão a ser conhecidos à medida que você trabalhar com os exercícios deste módulo.

Árvore de trabalho: o conjunto de diretórios e arquivos aninhados que contém o projeto no qual está sendo feito o trabalho.

Repositório: o diretório, localizado no nível superior de uma árvore de trabalho, no qual o Git mantém todo o histórico e os metadados de um projeto. Os repositórios são quase sempre chamados de repositórios. Um repositório simples é aquele que não faz parte de uma árvore de trabalho; ele é usado para compartilhamento ou backup. Geralmente, um repositório simples é um diretório com um nome que termina com .git, por exemplo, project.git.

Hash: um número produzido por uma função de hash que representa o conteúdo de um arquivo ou de outro objeto como um número fixo de dígitos. O Git usa hashes que têm 160 bits de comprimento. Uma vantagem de usar hashes é que o Git pode informar se um arquivo foi alterado pelo hash do conteúdo e pela comparação do resultado com o hash anterior. Se o carimbo de data/hora do arquivo for alterado, mas o hash do arquivo não, o Git saberá que o conteúdo do arquivo não foi alterado.

Objeto: um repositório Git contém quatro tipos de objetos, cada um exclusivamente identificado por um hash SHA-1. Um objeto de blob contém um arquivo comum. Um objeto de árvore representa um diretório; ele contém nomes, hashes e permissões. Um objeto de commit representa uma versão específica da árvore de trabalho. Uma marca é um nome anexado a um commit.

Commit: quando usado com o verbo fazer, commit significa fazer um objeto de commit. Essa ação recebe o nome dos commits feitos em um banco de dados. Isso significa que você está fazendo commit das alterações feitas, de modo que outras pessoas possam acabar vendo-as também.

Branch: um branch é uma série nomeada de commits vinculados. O commit mais recente em um branch é chamado de principal. A ramificação padrão, que é criada quando você inicializa um repositório, é chamada de main, em geral com o nome master no Git. O principal do branch atual é chamado de HEAD. Os branches são um recurso incrivelmente útil do Git, pois permitem que os desenvolvedores trabalhem de modo independente (ou em conjunto) nos branches e, posteriormente, mesclem as alterações no branch padrão.

Repositório remoto: um repositório remoto é uma referência nomeada a outro repositório Git. Quando você cria um repositório, o Git cria um repositório remoto chamado origin, que é o repositório remoto padrão das operações de push e pull.

Comandos, subcomandos e opções: as operações do Git são executadas por meio de comandos como git push e git pull. git é o comando e push ou pull é o subcomando. O subcomando especifica a operação que você deseja que o Git execute. Os comandos são frequentemente acompanhados por opções, que usam hifens (-) ou hifens duplos (--). Por exemplo, git reset --hard.

Esses e outros termos, como push e pull, farão mais sentido em breve. Porém, você precisa começar de algum lugar e talvez ache útil voltar e examinar este glossário de termos depois de concluir o módulo.


### Git e Github


O GitHub é uma plataforma de nuvem que usa o Git como sua tecnologia principal. O GitHub simplifica o processo de colaboração em projetos e fornece um site, mais ferramentas de linha de comando e um fluxo geral que pode ser usado pelos desenvolvedores e pelos usuários para trabalhar juntos. O GitHub funciona como o repositório remoto mencionado anteriormente.

Os principais recursos fornecidos pelo GitHub incluem:

Problemas
Discussões
Solicitações de pull
Notificações
Rótulos
Ações
Garfos
Projetos

```
git --version

```

    git --version

{{< highlight go  >}}
git --version
{{< / highlight >}}    

```
git config --global user.name "<USER_NAME>"
```
```
git config --global user.email "<USER_EMAIL>"
```
```
git config --list
```
```
mkdir Cats
```
```
cd Cats
```
```
git init --initial-branch=main
```
```
git init -b main
```
```
git init
git checkout -b main
```

git status

ls -a

git --help


### Comandos Básicos

git status
O primeiro e mais comumente usado comando do Git é git status. Você já o usou uma vez no exercício anterior para ver se inicializou o repositório Git corretamente.

git status exibe o estado da árvore de trabalho (e da área de preparo. Falaremos mais sobre a área de preparo em breve). Ele permite ver quais alterações estão sendo controladas pelo Git. Portanto, você pode decidir se deseja solicitar ao Git que tire outro instantâneo.

git add
git add é o comando usado para instruir o Git a começar a controlar as alterações em determinados arquivos.

O termo técnico é preparar essas alterações. Você usará git add para preparar as alterações para um commit. Todas as alterações de arquivos que foram adicionadas, mas que ainda não foram confirmadas, são armazenadas na área de preparo.

git commit
Depois de preparar algumas alterações para commit, você poderá salvar o trabalho em um instantâneo invocando o comando git commit.

Commit é um verbo e um substantivo. Ele tem, essencialmente, o mesmo significado de quando você se compromete com um plano ou confirma uma alteração em um banco de dados. Como verbo, fazer commit de alterações significa que você coloca uma cópia (do arquivo, do diretório ou de outros itens) no repositório como uma nova versão. Como substantivo, um commit é a pequena parte dos dados que fornece uma identidade exclusiva às alterações confirmadas. Os dados salvos em um commit incluem o nome e o endereço de email do autor, a data, os comentários sobre o que você fez (e o motivo), uma assinatura digital opcional e o identificador exclusivo do commit anterior.

git log
O comando git log permite que você veja informações sobre commits anteriores. Cada commit tem uma mensagem anexada (uma mensagem de commit), e o comando git log imprime informações sobre os commits mais recentes, como o carimbo de data/hora, o autor e uma mensagem de commit. Esse comando ajuda você a acompanhar o que está sendo feito e quais alterações foram salvas.

git help
Você já testou o comando git help, mas vale a pena relembrar como usá-lo. Use esse comando para obter com facilidade informações sobre todos os comandos que aprendeu até agora, entre outros.

Lembre-se de que cada comando também é fornecido com a página de ajuda própria. Encontre essas páginas de ajuda digitando git <command> --help. Por exemplo, git commit --help abre uma página que traz mais informações sobre o comando git commit e como usá-lo.

### VErificação de conhecimentos

1. Quais dos cenários a seguir é um caso de uso comum para um sistema de controle de versão? 

Excluir versões anteriores de um projeto ou um arquivo, de modo que você saiba que está trabalhando apenas com o arquivo ou os dados mais atuais.

Fazer alterações experimentais no projeto em um branch isolado.
Correto! O uso de branches para criar diferentes conjuntos de alterações em um projeto é um caso de uso fundamental para o controle de versão.


Coletar requisitos de recursos para um projeto grande e comunicá-los aos stakeholders.
2. Qual é outro nome para um sistema de controle de versão? 

VMS (Software de gerenciamento de versões)

Sistema de SCM (gerenciamento de controle de software)

Sistema de SCM (gerenciamento de configuração de software)
Correto!

3. Qual é a diferença entre o Git e o GitHub? 

O Git permite trabalhar com um ou mais branches locais e enviar alterações por push para um repositório remoto. O GitHub funciona como o repositório remoto, que é acessado por meio de um site ou de ferramentas de linha de comando.
Correto! O Git é a ferramenta que você pode usar para trabalhar com um branch local e enviar alterações por push para um repositório remoto. O GitHub funciona como o repositório remoto.


O Git é um DVCS (sistema de controle de versão distribuído) executado na nuvem. O GitHub é uma camada de interface que fornece acesso à tecnologia do Git.

O Git é usado por um colaborador individual. O GitHub é usado por vários colaboradores para simplificar o trabalho de desenvolvimento em grupo.
4. Qual comando do Git fornece informações sobre como usá-lo? 

git init

git status

git help
Correto! Use git help para ver informações sobre como usar o Git.





Recursos
Caso deseje obter detalhes, veja estes outros recursos:

Execute os comandos git help tutorial e git help tutorial-2.
Acesse o site do Everyday Git ou use o comando git help everyday.
Examine Recursos de aprendizagem do Git e do GitHub.
Assista ao vídeo Recapitulação da introdução ao Git.
Confira a seção de documentação do site oficial do Git.




## Como criar e modificar um projeto Git

### Introdução
Neste módulo, você vai começar seu projeto no Git e ganhar prática em editar alguns erros que podem existir em seu código. O Git pode parecer confuso quando você começa pela primeira vez, mas à medida que você ganhar prática, conseguirá navegar sem problemas.

Saiba como criar um projeto Git
Entender como controlar as alterações no Git
Saber corrigir erros simples no Git
Recuperar arquivos excluídos no Git

### Exercício

O Git não faz muita coisa com diretórios vazios. Portanto, vamos adicionar um arquivo à árvore de trabalho para que ele sirva como a home page do site de fotos de gatos.



```
touch index.html
```

```
git status
```

```
git add .
```

```
git status
```

```
git commit index.html -m "Create an empty index.html file"
```

```
git log
```



### Fazer alterações e rastreá-las com o Git


```
git diff
```
O formato de saída é o mesmo do comando diff do UNIX, e o comando do Git usa muitas das mesmas opções. Um sinal de adição é exibido na frente das linhas que foram adicionadas e um sinal de subtração indica as linhas que foram excluídas.

O padrão é que git diff compare a árvore de trabalho com o índice. Em outras palavras, ele mostra todas as alterações que ainda não foram preparadas (adicionadas ao índice do Git). Para comparar a árvore de trabalho com o último commit, use git diff HEAD.
Se o comando não retornar ao prompt após a execução, insira q para sair da exibição de comparação.

```
code .gitignore
```


```
*.bak
*~

```


```
git add -A
git commit -m "Make small wording change; ignore editor backups"
```



#### Listar os commits

```
git log
```



```
git log --oneline
```

Você poderá ver por que, quando há centenas (ou milhares) de commits em um projeto, a opção --oneline pode ser sua melhor amiga. Outra opção útil é -nX, em que X é um número de commit: 1 para o último commit, 2 para o anterior a esse etc. Para ver isso por conta própria, experimente usar um comando git log -n2.

Às vezes, as coisas dão errado. Você pode esquecer de adicionar um novo arquivo ou talvez adicionar um arquivo por engano. Talvez você tenha cometido um erro de ortografia no último commit ou tenha confirmado algo que não pretendia. Talvez você tenha excluído acidentalmente um arquivo.

O Git permite que você faça alterações sem receios, pois sempre oferece uma maneira de voltar ao local em que estava. Você pode, até mesmo, alterar o histórico de commits do Git, desde que altere somente os commits que não foram compartilhados

#### Corrigir um commit: sinalizador --amend




```
git commit --amend --no-edit
```
A opção --no-edit instrui o Git a fazer a alteração sem alterar a mensagem de commit. Use também --amend para editar uma mensagem de commit, adicionar arquivos acidentalmente deixados fora do commit ou remover arquivos que foram adicionados por engano.


#### Recuperar um arquivo excluído: git checkout

Imagine que você fez uma alteração em um arquivo de código-fonte que desfez todo o projeto e, portanto, deseja reverter esse arquivo para a versão anterior. Ou talvez tenha excluído acidentalmente um arquivo. O Git facilita a recuperação de uma versão anterior, mesmo que a versão atual não exista mais. Seu melhor amigo nessa situação é o comando git checkout.

`git checkout ` tem vários usos, mas no próximo exercício, vamos usá-lo para recuperar um arquivo excluído. git checkout atualiza os arquivos na árvore de trabalho para que correspondam à versão no índice ou na árvore especificada.

Se você excluiu acidentalmente um arquivo, recupere-o trazendo a versão do índice de volta à árvore de trabalho com este comando:



```
git checkout -- <file_name>
```

Você também pode fazer check-out de um arquivo de um commit anterior (normalmente, o principal de outro branch), mas o padrão é obter o arquivo do índice. O -- na lista de argumentos serve para separar o commit da lista de caminhos de arquivos. Isso não é estritamente necessário nesse caso, mas se você tiver um branch chamado <> (talvez porque esse é o nome do arquivo que está sendo trabalhado nesse branch), -- impedirá que o Git fique confuso.

Posteriormente, você aprenderá também a usar checkout para alternar os branches.

####  Recuperar arquivos: git reset

Você também pode excluir um arquivo usando git rm. Esse comando exclui o arquivo em disco e faz com que o Git registre a exclusão do arquivo no índice.

Portanto, se você executou este comando:

```
git reset HEAD index.html
git checkout -- index.html

```

Você pode usar git reset para remover o preparo das alterações.
Aqui, git reset remove o preparo da exclusão de arquivo do Git. Esse comando traz o arquivo de volta ao índice, mas o arquivo ainda está excluído em disco. Em seguida, você pode restaurá-lo no disco por meio do índice usando git checkout.

#### Reverter um commit: git revert

O último comando importante a ser conhecido para corrigir erros com o Git é git revert. git checkout só funciona em situações em que as alterações a serem desfeitas estão no índice. Depois de fazer commit das alterações, você precisará usar outra estratégia para desfazê-las. Nesse caso, podemos usar git revert para reverter o commit anterior. Ele funciona fazendo outro commit que cancela o primeiro.

Podemos usar git revert HEAD para fazer um commit exatamente oposto ao último commit, desfazendo o commit anterior, mas deixando todo o histórico intacto. A parte HEAD do comando apenas informa o Git de que só queremos "desfazer" o último commit.

Além disso, você pode remover o commit mais recente usando o comando git reset:



```
git reset --hard HEAD^
```

O Git oferece vários tipos de redefinições. O padrão é --mixed, que redefine o índice, mas não a árvore de trabalho; também moverá HEAD se você especificar outro commit. A opção --soft só move HEAD e mantém o índice e a árvore de trabalho inalterados. Essa opção mantém todas as alterações como "alterações a serem confirmadas", como indicado em git status. Uma redefinição --hard altera o índice e a árvore de trabalho para que correspondam ao commit especificado. As alterações feitas nos arquivos com controle de alterações são descartadas.



### Exercício – Usar o Git para corrigir erros

```
rm index.html
```

```
ls
```

```
CSS
```

```
git checkout -- index.html
```

```
git rm index.html
```

```
git checkout -- index.html
```

```
git reset HEAD index.html
```

```
git checkout -- index.html
```


### Verificaçaõ de conhecimentos

Verificação de conhecimentos
Concluído
200 XP
4 minutos

1. Como incluir um arquivo em seu índice do Git? 

Usando o comando 'git include'

Usando o comando 'git add'
Correto! O git add adicionará qualquer arquivo que você o informe ao seu índice do git.


Usando o comando 'git commit'
2. O que a tag -m faz para seu commit? 

A tag -m não é válida no git

A tag modifica sua confirmação se você se esqueceu de adicionar algo

Essa tag permite que você adicione uma mensagem ao seu commit
Correto! Mantenha suas mensagens de commit curtas e legíveis

3. Qual delas é um bom exemplo de uma mensagem de commit? 

Adicionar recurso ao administrador de alertas ao novo registro de usuário…
Correto! Uma boa regra prática é manter suas mensagens de git commit em 50 palavras e garantir que sejam descritivas para outros desenvolvedores.


recurso adicionado

Adicione rótulos de nome, idade, altura, peso e salário com caixas de texto correspondentes e mais sobre um botão enviar à página da Web para garantir que o usuário saiba claramente o que está sendo adicionado...
Incorreto. Esse commit, embora seja bastante descritivo do trabalho feito, adiciona muitas informações que podem ser excessivas.

4. Qual que é uma forma de corrigir um de seus commits anteriores sem precisar fazer um novo commit? 

Excluir o arquivo e criar um em seu lugar com as alterações corretas.

Utilizando a tag 'amend' do Git
Correto! Usar amend significa que você está alterando o que foi colocado no commit inicial.


Reverter o commit e criar outro
5. Como escolher entre o Git reset e o Git checkout para recuperar um arquivo perdido? 

O Git checkout pode recuperar um arquivo que você tenha excluído por engano. O git reset recuperará um arquivo que você excluiu usando o comando 'git rm'
Correto! O Git checkout atualiza seu arquivo com aquele presente no git index, enquanto o git reset desprepara os arquivos excluídos.


Sempre usar o git checkout porque é a opção mais segura

Criar um arquivo com o mesmo nome e usar a redefinição do Git
6. Quando você deve evitar alterar um commit anterior? 

Evite corrigir commits em que outros desenvolvedores basearam seu trabalho
Correto! Quando você altera um commit, o commit anterior a ele desaparece e é substituído pelo commit corrigido.


Quando você deseja adicionar um arquivo ao seu commit

Quando você quiser alterar o commit não mais recente.



## Colaborar com o Git

### Introdução

Você usará o Git para colaboração e controlar as alterações (e quem as faz), verificar se nada de errado ocorre quando duas pessoas alteram o mesmo arquivo e manter todos os arquivos de código-fonte copiados em backup.


Neste módulo, você vai:

Clonar um repositório
Enviar alterações a um repositório remoto por push
Aplicar stash às alterações
Efetuar pull de alterações de outros usuários para atualizar um repositório


### Colaboração usando um comando de pull


Nesta lição, você aprenderá a clonar um repositório para disponibilizá-lo para outras pessoas. Você também aprenderá a usar um dos recursos mais importantes do Git: as solicitações de pull.


#### Clonar um repositório (git clone)

No Git, um repositório é copiado pelo clone dele usando o comando git clone. Você pode clonar um repositório seja qual for o local de armazenamento dele, desde que você tenha uma URL ou um caminho para o qual apontá-lo.

git clone aceita um caminho do sistema de arquivos, um caminho SSH (por exemplo, git@example.com:alice/Cats. Você estará familiarizado com esse formato se tiver usado o Rsync ou o SCP) ou uma URL, normalmente começando com file:, git: ou ssh. Os vários formatos são descritos na documentação de git clone. No UNIX e no Linux, a operação de clonagem usa links físicos. Portanto, ela é rápida e ocupa espaço mínimo, porque apenas as entradas do diretório precisam ser copiadas, não os arquivos.

#### Repositórios remotos (git pull)
Quando o Git clona um repositório, ele cria uma referência ao repositório original chamada repositório remoto usando o nome origin. Ele configura o repositório clonado para que ele efetue pull ou recupere os dados do repositório remoto. (O Git também pode efetuar push. Você aprenderá a usar o push no Git mais adiante neste módulo). origin é a localização padrão para o Git efetuar pull de alterações e enviá-las por push. git pull copia as alterações do repositório remoto para o local. O comando git pull é muito eficiente, porque só copia novos commits e objetos e faz o check-in deles na árvore de trabalho.

Você efetua pull do origin usando o comando git pull. É útil comparar git pull com outros métodos de cópia de arquivos. O comando scp copia tudo. (scp é semelhante ao comando cp do UNIX, com a exceção de que os arquivos que estão sendo copiados não precisam estar no mesmo computador.) Se houver 10.000 arquivos no diretório remoto, scp copiará todos eles. Um programa mais eficiente chamado Rsync examina todos os arquivos nos diretórios local e remoto e só copia aqueles que são diferentes. Geralmente, o Rsync é usado para fazer backups, mas ainda precisa aplicar hash a todos os arquivos, a menos que tenham tamanhos ou datas de criação diferentes.

O Git examina apenas os commits. Ele já conhece o último commit obtido do repositório remoto porque salvou a lista de commits. Em seguida, o Git instrui o computador do qual está sendo feita a cópia a enviar tudo o que foi alterado, incluindo os novos commits e os objetos para os quais eles apontam. Esses commits e objetos são empacotados em um arquivo chamado de pacote e enviados em um lote. Por fim, o Git atualiza a árvore de trabalho desempacotando todos os objetos que foram alterados e mesclando-os (se necessário) com os commits e os objetos na árvore de trabalho.

O Git só efetua pull ou push quando você o instrui a fazer isso. Isso é diferente, digamos, do Dropbox, que precisa solicitar ao sistema operacional que o notifique das alterações feitas na pasta e, ocasionalmente, perguntar ao servidor se alguma outra pessoa fez alterações.

### Criar solicitações pull (git request-pull)
Depois que outro desenvolvedor, como Alice, clonar seu repositório e fizer algumas alterações localmente, o ideal será que ele incorpore essas alterações novamente no repositório original. Pode parecer que efetuar push dessas alterações para o repositório original é a abordagem certa. No entanto, um push para o repositório original falhará, porque outros usuários não têm permissão para fazer alterações no seu repositório. E é assim que deve ser. Por enquanto, você deseja examinar as alterações recebidas antes de mesclá-las na base de código principal.

Por enquanto, Alice precisará enviar uma solicitação de pull para solicitar que você envie as alterações dela para a base de código principal. Alice pode fazer isso usando git request-pull, que pode ser semelhante a este exemplo:

git request-pull -p origin/main .

Alice refere-se ao branch main no repositório remoto origin como origin/main.

Essa solicitação de pull é, essencialmente, a mesma coisa que uma solicitação de pull no GitHub (um local para armazenar códigos, o que não abordaremos neste módulo). Uma solicitação de pull dá a oportunidade de examinar as alterações de outros colaboradores antes de incorporar o trabalho deles no trabalho que você está fazendo no site. As revisões de código são uma parte importante (alguns dizem a parte mais importante) da programação colaborativa.


#### Criar um repositório remoto (git remote) e concluir a solicitação de pull (git pull)
Como proprietário de um projeto, você precisa saber como mesclar as solicitações de pull. Primeiro, você usa o comando git remote para configurar o repositório de outro desenvolvedor como um repositório remoto. Em seguida, você usa esse repositório remoto para pulls e solicitações de pull usando o comando git pull.

Nos bastidores, git pull é uma combinação de duas operações mais simples: git fetch, que obtém as alterações, e git merge, que mescla essas alterações no repositório. Nesse caso, a mesclagem foi de avanço rápido, o que significa que Alice teve seu último commit no repositório dela, de modo que o commit dela pôde ser adicionada à frente do seu histórico sem nenhuma modificação.


------

git stash salva o estado da árvore de trabalho e do índice fazendo alguns commits temporários. Considere o stash como uma maneira de salvar seu trabalho atual enquanto você faz alguma outra coisa, sem fazer um commit "real" nem afetar o histórico do repositório.

Verificação de conhecimentos


1. Qual é a principal vantagem da natureza distribuída do Git? 

O Git mescla automaticamente as alterações salvas de vários autores remotos em um só repositório de projeto.

Vários colaboradores remotos podem trabalhar juntos em um projeto sem o receio de substituir o trabalho uns dos outros. Os colaboradores podem verificar as alterações de outro colaborador antes de mesclá-las com as próprias.
Correto! A natureza distribuída do Git ajuda todos os colaboradores a garantir e manter a validade do conteúdo do projeto.


O Git distribui arquivos e uma estrutura de pastas para o computador de cada colaborador em uma rede de longa distância para manter a segurança. Essa arquitetura fornece armazenamento de dados altamente seguro e garante que os dados do repositório do projeto não possam ser corrompidos.
2. Quando um usuário do Git copia um repositório, qual termo descreve a referência que o Git configura para o repositório original? 

origin
Incorreto. O Git usa o nome origin para se referir ao repositório original, mas essa não é a própria referência.


repositório

remote
Correto! Quando você clona (copia) um repositório, o Git cria uma referência ao repositório original chamada "repositório remoto". O Git usa o nome "origem" para se referir ao repositório remoto.

3. Qual comando do Git faz uma cópia de um repositório existente? 

git clone <repo-name>

git clone <repo-path>
Correto! O comando git clone usa uma URL ou um caminho para um repositório existente como parâmetro.


git copy <repo-name>
4. Qual comando do Git pode ser usado para salvar as alterações atuais, mas sem usar uma solicitação de pull? 

git stash
Correto! O comando git stash salva o estado da árvore de trabalho e do índice fazendo alguns commits temporários. Esse tipo de processo de salvamento não afeta o histórico do repositório.


git save

git store
5. Suponha que você tenha um projeto com dez arquivos no branch de trabalho local do repositório. Recentemente, você atualizou três dos arquivos: toc.yml, intro.txt e exercise.json. Agora, você deseja criar uma solicitação de pull somente para as alterações no arquivo JSON. Qual conjunto de comandos do Git você deverá usar para criar a solicitação de pull apenas para essas alterações? 

git add .
git commit -m "my changes for the exercise"
git push origin <working-branch>


git add exercise.json
git commit -m "my changes for the exercise"
git push origin <working-branch>

Correto! Para enviar por push todas as alterações atuais, especifique . após git add. Para enviar as alterações por push para apenas um arquivo, insira o nome do arquivo específico.


git add exercise
git commit -m "my changes for the exercise"
git push remote <working-branch>


Resumo
Concluído
100 XP
5 minutos
Parabéns! Neste módulo, você aprendeu a usar o Git para colaborar com outros desenvolvedores.

Neste módulo, você aprendeu:

Como clonar um repositório
Como aplicar stash às alterações
Como enviar alterações por push para um repositório
O que são solicitações de pull e como iniciá-las
Neste ponto, você sabe o suficiente sobre o Git para colaborar com outras pessoas de maneiras simples, mas ainda há muito mais para aprender!



## Editar código por meio de branches e mesclagem no Git

### Introdução

Imagine que você seja um novo desenvolvedor de software em uma empresa que escreve softwares de aviônica para companhias aéreas comerciais. O controle de qualidade é essencial, e os desenvolvedores trabalham em pequenas equipes usando o Git para o controle de versão. Você já sabe um pouco sobre o Git. Você o usou para acompanhar suas alterações, corrigir erros e colaborar com outros desenvolvedores por meio de um repositório compartilhado e usando solicitações de pull. No entanto, você sabe que o Git tem ainda mais a oferecer e está empolgado para aprender.

Você já criou um pequeno site que você e seus amigos podem usar para praticar o Git compartilhando fotos dos seus gatos. Você chamou alguns amigos que são desenvolvedores de software para ajudar você.

À medida que seu projeto progride, você deseja facilitar a colaboração com seus amigos, para que possa trabalhar em recursos do site sem conflitos nem esforço desperdiçado.

Neste módulo, você aprenderá quais branches estão no Git, como usá-los para desenvolvimento e como mesclá-los, incluindo lidar com conflitos de mesclagem.

Objetivos de aprendizagem
Neste módulo, você vai:

Saber como os branches funcionam no Git
Criar branches e alternar entre eles
Mesclar branches
Aprender técnicas básicas para resolver conflitos de mesclagem

### Branches no Git

Você é um desenvolvedor da Web que está tentando saber mais sobre o Git para seu trabalho. Você criou um site HTML e CSS simples com fotos de gatos para praticar suas habilidades do Git e tem trabalhado nele com seus amigos, Alice e Bob.

À medida que o projeto avança, você percebe que deseja que todos possam trabalhar em mais de uma tarefa por vez sem atrapalhar o trabalho de outra pessoa. Você precisa de uma maneira de manter o trabalho de todos separado, para que o novo desenvolvimento não atrapalhe a correção de bugs existentes. No Git, os branches facilitam esse tipo de colaboração.

O trabalho feito em um branch não precisa ser compartilhado e não interfere no trabalho de outros branches. Os branches permitem que você mantenha os commits relacionados a cada tópico juntos e isolados de outros trabalhos, de modo que as alterações feitas em um tópico sejam fáceis de examinar e acompanhar.

O desenvolvimento de software moderno é feito quase inteiramente em branches. A meta é manter o branch principal limpo até que o trabalho esteja pronto para fazer check-in. Você efetua push das suas alterações para o branch principal, ou ainda melhor, envia uma solicitação de pull para mesclar as alterações.

Uma das vantagens do Git em relação aos VCSs (sistemas de controle de versão) mais antigos é que a criação de um branch é extremamente rápida com o Git. Ela equivale à gravação de um hash de 40 caracteres em um arquivo em .git/heads. A troca de branches também é rápida, porque o Git armazena arquivos inteiros e os descompacta em vez de tentar reconstruí-los de listas de alterações. A mesclagem no Git não é muito simples, mas é direta e, em geral, totalmente automática.

Vamos aprender o que são branches, como são usados e como funcionam.

Estrutura e nomenclatura do branch
Um branch é simplesmente uma cadeia de commits que é ramificada da linha principal de desenvolvimento, como uma ramificação em uma árvore.

Se você está alternando de outro VCS para o Git, pode estar acostumado a uma terminologia levemente diferente. O VCS Subversion nomeia seu branch padrão como trunk, enquanto o Git o chama de master. Você pode renomear o branch padrão, assim como renomear qualquer outro branch. Neste módulo, nomeamos o branch padrão como main.

Um branch geralmente começa com um commit no branch padrão. Neste caso, no main. O branch amplia uma cadeia de histórico separada à medida que commits são adicionados. Eventualmente, as alterações no branch são mescladas novamente no main. Neste módulo, você aprenderá a fazer commits em um branch e mesclá-los no branch main.

Suponha que você ramifique o branch main. Veja como visualizar o que acontece:

Diagrama mostrando a relação do branch principal e branches locais.

Cada letra maiúscula no diagrama representa uma confirmação. Os branches têm nomes como add-authentication e fix-css-bug e também podem ter seus próprios branches. A meta final é permitir que os desenvolvedores façam o que precisam fazer sem atrapalhar os colegas e tenham com uma ramificação principal que represente os melhores esforços de todos os envolvidos.

Criar e alternar branches (git branch e git checkout)
Um motivo comum para criar um branch é fazer alterações em um recurso existente. Um branch para essa finalidade normalmente seria chamado de branch do tópico ou branch de recurso.

Você pode criar um branch usando o comando git branch. Alterne entre branches usando o comando git checkout.

Você já encontrou checkout como uma forma de substituir arquivos na árvore de trabalho obtendo-os do índice. Sem caminhos na lista de argumentos, o checkout atualiza tudo na árvore de trabalho e no índice para corresponder ao commit especificado – neste caso, o cabeçalho do branch.

Mesclar branches (git merge)
Ao finalizar algum trabalho em um branch, como um recurso ou uma correção de bug, convém mesclar esse branch de volta no branch principal. Você pode usar o comando git merge para mesclar um branch específico em seu branch atual.

Por exemplo, se você estivesse trabalhando em um branch chamado my-feature, o fluxo de trabalho ficaria assim:

Bash

Copiar
 Switch back to the main branch
git checkout main

 Merge my-feature branch into main
git merge my-feature

Depois de usar esses comandos e resolver quaisquer conflitos de mesclagem (vamos discutir os conflitos de mesclagem posteriormente neste módulo), todas as alterações do seu branch my-feature estarão em main.

### Exercício – Criar um branch como Alice

Sua amiga desenvolvedora Alice quer adicionar CSS para estilizar as fotos de gatos em seu site. Alice quer realizar esse trabalho em seu próprio branch.

Instalação
Antes de assumir a função de Alice, você deve fazer um trabalho de configuração de um repositório básico para ser compartilhado entre todos e adicionar alguns arquivos.

O Git já está instalado para nós no Azure Cloud Shell e, portanto, podemos usar o Git no Cloud Shell à direita.

Criar um repositório básico compartilhado
Crie um diretório chamado Shared.git para armazenar o repositório básico:

Bash

Copiar
mkdir Shared.git
cd Shared.git

Agora, execute o seguinte comando para criar um repositório básico no diretório compartilhado:

Bash

Copiar
git init --bare

Defina o nome do branch padrão para o novo repositório. Para realizar essa etapa, você pode alterar o branch HEAD para que ele aponte para outro branch. Neste caso, o branch main:

Bash

Copiar
git symbolic-ref HEAD refs/heads/main

Clonar o repositório compartilhado para Bob
Suba um nível desse diretório e crie um diretório para Bob a fim de armazenar o repositório:

Bash

Copiar
cd ..
mkdir Bob

Clone e configure o repositório para Bob:

Bash

Copiar
cd Bob
git clone ../Shared.git .
git config user.name Bob
git config user.email bob@contoso.com
git symbolic-ref HEAD refs/heads/main

 Observação

Como você deseja começar com o branch padrão do main, você precisa alterar HEAD para apontar para refs/heads/main em vez de refs/heads/master, que é o nome do branch padrão.

Adicionar arquivos base
Como uma etapa de configuração final, adicionaremos os arquivos base do site e efetuaremos push deles para o repositório compartilhado. Para esses comandos, ainda estamos trabalhando no diretório Bob.

Crie alguns arquivos executando o comando touch do Linux, prepare os arquivos e confirme-os usando o Git:

Bash

Copiar
touch index.html
mkdir Assets
touch Assets/site.css
git add .
git commit -m "Create empty index.html and site.css files"

Agora, adicione HTML ao arquivo usando o editor de código do Cloud Shell. Você pode abrir o editor executando o comando code. Abra index.html no editor online inserindo code index.html no prompt do terminal:

Bash

Copiar
code index.html

Cole este código HTML:

HTML

Copiar
<!DOCTYPE html>
<html>
  <head>
    <meta charset='UTF-8'>
    <title>Our Feline Friends</title>
    <link rel="stylesheet" href="CSS/site.css">
  </head>
  <body>
    <nav><a href="./index.html">home</a></nav>
    <h1>Our Feline Friends</h1>
    <p>Eventually we will put cat pictures here.</p>
    <footer><hr>Copyright (c) 2021 Contoso Cats</footer>
  </body>
</html>
Salve o arquivo e feche o editor. Selecione as reticências "…" no canto direito do editor ou use a tecla de acelerador (pressione CTRL+S no Windows e no Linux e Cmd+S no macOS).

Altere para o diretório Ativos e abra site.css no editor:

Bash

Copiar
cd Assets
code site.css

Adicione o seguinte CSS ao arquivo:

css

Copiar
h1, h2, h3, h4, h5, h6 { font-family: sans-serif; }
body { font-family: serif; background-color: #F0FFF8; }
nav, footer { background-color: #C0D8DF; }
Salve o arquivo e feche o editor.

Volte ao diretório Bob e confirme novamente:

Bash

Copiar
cd ..
git add .
git commit -m "Add simple HTML and stylesheet"
git push --set-upstream origin main

 Observação

Como estamos usando um nome de branch padrão diferente, você precisa dizer ao git para associar o seu branch principal ao branch principal do repositório de origem.

Verifique a saída. Se um aviso como este for exibido, não se preocupe. O aviso só está informando os usuários de uma alteração nos comportamentos padrão do Git.

Saída

Copiar
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, run:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)
Se você quiser ter certeza de que não verá esse aviso novamente, execute este comando:

Bash

Copiar
git config --global push.default simple

Verifique a saída deste indicador de êxito:

Saída

Copiar
Counting objects: 9, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (9/9), 953 bytes | 953.00 KiB/s, done.
Total 9 (delta 0), reused 0 (delta 0)
To ../Shared.git
 * [new branch]      main -> main
Criar um branch para Alice
Alice quer criar um branch do tópico chamado add-style para trabalhar. Vamos assumir a função de Alice, criar o branch e adicionar código a ele.

Mova um nível para cima desse diretório e crie um diretório para a cópia do repositório da Alice:

Bash

Copiar
cd ..
mkdir Alice

Clone o repositório para Alice e o configure:

Bash

Copiar
cd Alice
git clone ../Shared.git .
git config user.name Alice
git config user.email alice@contoso.com

Agora você tem uma cópia atual do repositório. Para confirmar, você pode listar o conteúdo do arquivo e executar git status para confirmar o estado do repositório.

Bash

Copiar
ls
git status

Execute o comando git branch para criar um branch chamado add-style. Execute o comando git checkout para alternar para esse branch (torná-lo o branch atual).

Bash

Copiar
git branch add-style
git checkout add-style

No diretório Alice/Ativos, abra site.css. Adicione a seguinte definição de classe CSS à parte inferior do arquivo:

css

Copiar
.cat { max-width: 40%; padding: 5 }
Salve as alterações feitas no arquivo e feche o editor.

Confirme a alteração:

Bash

Copiar
git commit -a -m "Add style for cat pictures"

Neste ponto, Alice deseja disponibilizar seu estilo a todos os outros usuários. Portanto, ela volta para main e efetua pull caso qualquer outra pessoa tenha feito alterações:

Bash

Copiar
git checkout main
git pull

A saída informa que o branch main está atualizado (em outras palavras, main no computador de Alice corresponde a main no repositório compartilhado). Portanto, Alice mescla o branch add-style com o branch main executando git merge --ff-only para executar uma mesclagem de avanço rápido. Alice efetua push de main do repositório dela para o repositório compartilhado.

Bash

Copiar
git merge --ff-only add-style
git push

Nesse caso, uma mesclagem de avanço rápido não era estritamente necessária porque o branch main não tinha nenhuma alteração, e o Git teria mesclado as alterações de qualquer forma. Mas usar o sinalizador --ff only é uma boa prática, pois uma mesclagem --ff-only falhará se main tiver sido alterado.

### Exercício – Mesclar branch de Bob


Retorne ao diretório Bob e execute o comando a seguir para criar um branch chamado add-cat. Use a opção checkout -b popular para criar o branch e alternar para um único comando.

Bash

Copiar
cd ../Bob
git checkout -b add-cat

Baixe o arquivo zip que contém alguns recursos do site. Descompacte os arquivos de recurso:

Bash

Copiar
wget https://github.com/MicrosoftDocs/mslearn-branch-merge-git/raw/main/git-resources.zip
unzip git-resources.zip

Agora, mova o arquivo bobcat2-317x240.jpg para o diretório Ativos de Bob. Exclua os outros arquivos. Você baixará os arquivos e os usará novamente mais tarde.

Bash

Copiar
mv bobcat2-317x240.jpg Assets/bobcat2-317x240.jpg
rm git-resources.zip
rm bombay-cat-180x240.jpg

Abra o arquivo index.html e substitua a linha que diz "Eventualmente, colocaremos as imagens de gato aqui" pela seguinte linha:

HTML

Copiar
<img src="Assets/bobcat2-317x240.jpg" />
Salve o arquivo e feche o editor.

Você fez duas alterações no branch add-cat de Bob – adicionou um arquivo e modificou outro. Execute git status para verificar as alterações mais uma vez:

Bash

Copiar
git status

Execute os seguintes comandos para adicionar o novo arquivo no diretório Ativos para o índice e confirmar todas as alterações:

Bash

Copiar
git add .
git commit -a -m "Add picture of Bob's cat"

Bob agora executa a mesma ação que Alice realizou anteriormente. Bob retorna para o branch main e executa um pull para ver se algo foi alterado:

Bash

Copiar
git checkout main
git pull

Verifique a saída. Desta vez, a saída indica que alterações foram feitas no branch main no repositório compartilhado (o resultado do push de Alice). Também indica que as alterações extraídas de main no repositório compartilhado foram mescladas com main no repositório de Bob:

Saída

Copiar
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 1), reused 0 (delta 0)
Unpacking objects: 100% (4/4), done.
From D:/Labs/Git/Bob/../Shared
   e81ae09..1d2bfea  main     -> origin/main
Updating e81ae09..1d2bfea
Fast-forward
 Assets/site.css | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
Bob mescla seu branch no branch main para que main no repositório tenha as alterações dele e as alterações de Alice. Bob efetua push de main em seu computador para o branch main no repositório compartilhado:

Bash

Copiar
git merge add-cat --no-edit
git push

Bob não usou o sinalizador --ff-only porque sabia que main tinha mudado. Uma mesclagem somente de avanço rápido teria falhado.

Sincronizar o repositórios
Neste ponto, Bob tem um repositório atualizado, mas Alice não. Alice precisa fazer um git pull do repositório compartilhado para garantir que ela tenha a melhor e mais recente versão do site.

Execute os seguintes comandos para sincronizar o repositório de Alice com o repositório compartilhado:

Bash

Copiar
cd ../Alice
git pull

Reserve um tempo para verificar se o repositório de Alice e de Bob estão sincronizados. Cada repos deve ter um arquivo JPG no diretório Ativos e um elemento <img> declarado no arquivo index.html. O arquivo site.css na pasta Ativos de cada repositório deve conter uma linha que define um estilo CSS chamado gato. Esse estilo foi adicionado por Alice quando ela fez suas alterações.

Se você abrir index.html em um navegador, verá a seguinte imagem:

Captura de tela que mostra gatos no site.

Na próxima lição, você aprenderá a resolver os conflitos de mesclagem, que ocorrem quando as alterações feitas por dois ou mais desenvolvedores se sobrepõem.


### Exercício – Resolver conflitos de mesclagem

Às vezes, não importa o quão bem você planeja, o projeto dá errado. Imagine que dois desenvolvedores estejam trabalhando no mesmo arquivo de projeto ao mesmo tempo. O primeiro desenvolvedor efetua push de suas alterações para o branch main do repositório do projeto sem nenhum problema. Quando o segundo desenvolvedor tenta efetuar push de suas alterações, o Git diz que há um conflito de mesclagem. O arquivo que o segundo desenvolvedor está tentando modificar não está mais atualizado quanto às alterações mais recentes ou à versão do arquivo. A versão do arquivo deve ser atualizada para que as alterações do segundo desenvolvedor possam ser mescladas. Os desenvolvedores que usam controle de versão temem poucas coisas mais do que o conflito de mesclagem.

Conflitos como esse podem acontecer. Portanto, você deve saber como lidar com eles. A boa notícia é que o Git fornece soluções para lidar com conflitos de mesclagem.

Criar branches para Alice e Bob
Vamos começar criando um branch para Alice e um para Bob. Os dois amigos desenvolvedores estão atualizando arquivos no repositório do projeto ao mesmo tempo. Eles não estão cientes das alterações um do outro porque estão fazendo atualizações em seus branches locais.

Verifique se você está no diretório Alice e crie um branch chamado add-cat para Alice trabalhar:

Bash

Copiar
git checkout -b add-cat

Altere para o diretório Bob e crie um branch chamado style-cat para Bob trabalhar:

Bash

Copiar
cd ../Bob
git checkout -b style-cat

Agora, vamos fazer algumas alterações nos branches.

Faça uma alteração como Alice
Comece assumindo a função de Alice e faça uma alteração na página inicial do site. Substitua a imagem do gato de Bob por uma imagem de Alice.

Volte para o diretório Alice:

Bash

Copiar
cd ../Alice

Se você não baixou os recursos anteriormente, baixe o arquivo zip que contém os recursos desta lição. Descompacte os arquivos de recurso:

Bash

Copiar
wget https://github.com/MicrosoftDocs/mslearn-branch-merge-git/raw/main/git-resources.zip
unzip git-resources.zip

Mova o arquivo bombay-cat-180x240.jpg para o diretório Ativos de Alice e exclua os outros arquivos:

Bash

Copiar
mv bombay-cat-180x240.jpg Assets/bombay-cat-180x240.jpg
rm git-resources.zip
rm bobcat2-317x240.jpg

Abra o arquivo index.html e substitua esta instrução (que usa uma das imagens de gato de Bob):

HTML

Copiar
<img src="Assets/bobcat2-317x240.jpg" />
Por esta instrução (que usa uma das imagens de gato de Alice):

HTML

Copiar
<img class="cat" src="Assets/bombay-cat-180x240.jpg" />
Salve o arquivo e feche o editor.

Agora, execute os comandos do Git a seguir para efetuar push das alterações para o repositório do projeto. Primeiro, adicionaremos os commits feitos na pasta Ativos. Depois, vamos voltar para o branch main e executar git pull para garantir que nada tenha mudado. Por fim, mesclaremos o branch local add-cat no branch main e efetuaremos push das alterações para o repositório.

Bash

Copiar
git add Assets
git commit -a -m "Add picture of Alice's cat"
git checkout main
git pull
git merge --ff-only add-cat
git push

Conclua confirmando que o push foi bem-sucedido.

Faça uma alteração como Bob
Sem saber o que Alice está fazendo, Bob observa que o último push de Alice adicionou um estilo CSS chamado cats ao arquivo site.css do repositório. Bob decide aplicar essa classe à imagem de gato dele.

Volte para o diretório Bob:

Bash

Copiar
cd ../Bob

Abra o arquivo index.html . Substitua a instrução que usa a imagem de gato de Bob pela seguinte instrução que adiciona um atributo class="cat" ao elemento <img>:

HTML

Copiar
<img class="cat" src="Assets/bobcat2-317x240.jpg" />
Salve o arquivo e feche o editor.

Agora, execute os comandos do Git a seguir para sincronizar as alterações com o repositório do projeto, como você fez para as atualizações do repositório de Alice. Confirme a alteração, alterne para o branch main, execute git pull e mescle a alteração de estilo:

Bash

Copiar
git commit -a -m "Style Bob's cat"
git checkout main
git pull
git merge style-cat

E aqui está: o temido conflito de mesclagem. A mesma linha no mesmo arquivo foi alterada por duas pessoas. O Git vê o conflito e relata "Falha na mesclagem automática".O Git não tem como saber se o atributo src no elemento <img> deve referenciar o arquivo bobcat2-317x240.jpg ou o arquivo bombay-cat-180x240.jpg.

Saída

Copiar
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
A saída do Git identifica o arquivo index.html como a origem do conflito.

A pergunta agora é: o que Bob deve fazer?

Resolver o conflito de mesclagem
Bob tem algumas opções neste ponto. Ele pode executar uma destas ações:

Execute o comando git merge --abort para restaurar o branch main para o que era antes da tentativa de mesclagem. Execute o comando git pull para obter as alterações de Alice. Criar um branch, fazer as alterações e mesclar o branch com o branch main. Por fim, efetuar push das alterações.
Execute o comando git reset --hard para voltar ao local em que estava antes de iniciar a mesclagem.
Resolver o conflito manualmente usando as informações que o Git insere nos arquivos afetados.
Os desenvolvedores parecem preferir a última opção. Quando o Git detecta um conflito nas versões de conteúdo, ele insere ambas as versões no arquivo. O Git usa formatação especial para ajudar você a identificar e resolver o conflito: colchetes angulares esquerdos <<<<<<<, traços duplos (sinais de igual) ======= e colchetes angulares direitos >>>>>>>. O conteúdo acima da linha de traços ======= mostra as alterações em seu branch. O conteúdo abaixo da linha do separador mostra a versão do conteúdo no branch que você está tentando mesclar.

Confira abaixo como está o arquivo index.html no repositório de Bob agora. Observe a formatação especial em torno do conteúdo com conflitos:

HTML

Copiar
<!DOCTYPE html>
<html>
  <head>
    <meta charset='UTF-8'>
    <title>Our Feline Friends</title>
    <link rel="stylesheet" href="CSS/site.css">
  </head>
  <body>
    <nav><a href="./index.html">home</a></nav>
    <h1>Our Feline Friends</h1>
    <<<<<<< HEAD
    <img class="cat" src="Assets/bombay-cat-180x240.jpg">
    =======
    <img class="cat" src="assets/bobcat2-317x240.jpg">
    >>>>>>> style-cat
    <footer><hr>Copyright (c) 2021 Contoso Cats</footer>
  </body>
</html>
Vamos resolver o conflito de mesclagem editando o arquivo index.html. Como esse conflito de mesclagem é uma correção rápida, você fará a alteração diretamente no branch main, embora ainda esteja no diretório Bob.

Abra o arquivo index.html e exclua as linhas de formatação especiais. Não remova nenhuma outra instrução.

HTML

Copiar
<<<<<<< HEAD
=======
>>>>>>> style-cat
Salve o arquivo e feche o editor.

O arquivo index.html agora tem dois elementos <img>: um para a imagem de gato de Bob e outro para a imagem de Alice.

Alguns editores de texto apresentam integração com o Git e oferecem ajuda quando observam texto que indica um conflito de mesclagem. Se você abrir o arquivo index.html no Visual Studio Code, verá o seguinte código:

Captura de tela que mostra como resolver conflitos de mesclagem no Visual Studio Code.

Se você selecionar Aceitar Ambas as Alterações, o editor removerá as linhas em volta dos elementos <img> e deixará ambos os elementos intactos.

Execute os seguintes comandos para confirmar a alteração:

Bash

Copiar
git add index.html
git commit -a -m "Style Bob's cat"

O comando git add informa ao Git que o conflito no arquivo index.html foi resolvido.

Efetue push das alterações para o branch main no repositório remoto:

Bash

Copiar
git push

Conclua sincronizando as alterações no repositório de Alice:

Bash

Copiar
cd ../Alice
git pull

Por fim, abra o arquivo index.html de Alice e confirme se a versão também tem duas tags <img> com fotos de gato.


### Verificação de conhecimentos
1. Qual das afirmações a seguir é verdadeira sobre branches no Git? 

O trabalho feito em um branch não interfere no trabalho em outros branches.
Correto! A finalidade dos branches é isolar as alterações em um branch de alterações feitas em outro branch, até que você esteja pronto para mesclar as alterações de ambos os branches.


Um branch não pode ter outros branches que se estendem de sua linha de desenvolvimento.

O branch padrão em um repositório Git é chamado de master, e esse nome de branch nunca pode ser alterado.
2. Quais dos comandos Git a seguir criam um novo branch e alteram seu local de trabalho para o novo branch? 

git branch my-new-branch
git checkout my-new-branch
Correto! Você também pode usar o comando git checkout -b my-new-branch para criar e alternar para o branch em uma única etapa.


git branch -new my-new-branch
git checkout my-new-branch

git branch -new my-new-branch
git switch my-new-branch
3. Suponha que você tente mesclar as alterações do branch local no repositório do projeto, mas o Git retorne um erro de conflito de mesclagem. Qual comando você pode usar para restaurar o branch padrão (main) para seu estado correto? 

git merge --cancel

git merge --abort
Correto! Esse comando restaura o branch padrão (main) para o estado em que estava antes de você tentar mesclar suas alterações.


git merge --reset
4. Qual das amostras a seguir é uma exibição precisa do que o Git pode mostrar para um conflito de mesclagem entre o branch my-penguins e o branch main? 

HTML
<img class="cat" src="images/panda.jpg">
<img class="cat" src="images/peacock.jpg">
<<<<<<< my-penguins
<img class="cat" src="images/penguin.jpg">
<img class="cat" src="images/platypus.jpg">
<img class="cat" src="images/pony.jpg">
>>>>>>> main
<footer>Copyright 2021 - Perfect Pets</footer>

HTML

Copiar
<body>
  <img class="cat" src="images/panda.jpg">
  <img class="cat" src="images/peacock.jpg">
  <<<<<<< main
  <img class="cat" src="images/platypus.jpg">
  <img class="cat" src="images/pony.jpg">
  =======
  <img class="cat" src="images/penguin.jpg">
  >>>>>>> my-penguins
  <footer>Copyright 2021 - Perfect Pets</footer>
</body>
Incorreto. Verifique o local do conteúdo que tem conflitos. O Git deve mostrar as alterações de entrada acima do separador e o conteúdo existente no branch main abaixo da linha.


HTML

Copiar
<head><body>
  <img class="cat" src="images/panda.jpg">
  <img class="cat" src="images/peacock.jpg">
  <<<<<<< my-penguins
  <img class="cat" src="images/penguin.jpg">
  =======
  <img class="cat" src="images/platypus.jpg">
  <img class="cat" src="images/pony.jpg">
  >>>>>>> main
  <footer>Copyright 2021 - Perfect Pets</footer>
</body></head>
Correto! O Git sempre mostra todo o arquivo. O Git usa colchetes angulares esquerdo e direito para cercar as seções de conteúdo que têm um conflito. O Git usa uma linha de sinais de igual para separar duas versões de conteúdo que estão em conflito.



### Resumo

Parabéns! Neste módulo, você aprendeu a usar branches do Git para colaborar com outros desenvolvedores e resolver conflitos de mesclagem.

Você aprendeu:

O que são branches, como e quando usá-los
Como mesclar branches
Como resolver conflitos de mesclagem
Neste ponto, você sabe o suficiente sobre o Git para trabalhar bem com outros desenvolvedores e cumprir as metas do seu projeto.


## 
Introdução ao GitHub

### Introdução

O GitHub é uma plataforma de desenvolvimento que permite que você hospede e revise códigos, gerencie projetos e crie software com 50 milhões de desenvolvedores.

Por que todos estão criando no GitHub? Porque ele fornece os recursos importantes de DevOps que as empresas e organizações de todos os tamanhos precisam para seus projetos públicos e privados. Seja planejando recursos, corrigindo bugs ou colaborando em alterações, o GitHub é o lugar em que os desenvolvedores de software do mundo todo se reúnem para fazer coisas e depois melhorá-las.

Neste módulo, você aprenderá a utilizar os principais recursos do GitHub, incluindo problemas, notificações, ramificações, confirmações e solicitações de pull.

Objetivos de aprendizagem
Neste módulo, você vai:

Comunique-se com a comunidade do projeto sobre os problemas.
Gerenciar notificações para os eventos do projeto.
Crie ramificações para gerenciar o trabalho em paralelo.
Faça confirmações para atualizar o código-fonte do projeto.
Introduzir alterações com solicitações de pull.
Implantação de uma página da Web no GitHub Pages.
Reconheça as diferenças entre o Git e o GitHub e as funções que eles desempenham no ciclo de vida do desenvolvimento de software.
Descreva um repositório bifurcado e como ele difere de um clone.
Explicar a funcionalidade dos rótulos de repositório e em que ponto aplicá-los em problemas e solicitações de pull.

### O que é o GitHub?

Aqui, discutimos os principais recursos do GitHub que você usará diariamente para gerenciar e contribuir com projetos de software.

O fluxo do GitHub
Além de fornecer uma plataforma para o desenvolvimento colaborativo de software, o GitHub também oferece um fluxo de trabalho projetado para otimizar o uso de seus vários recursos. Embora esta unidade ofereça uma visão geral superficial de componentes importantes da plataforma, recomendamos que você analise primeiro o fluxo do GitHub.

Git e GitHub
Ao trabalhar com Git e GitHub, você pode se perguntar qual é a diferença entre os dois.

O Git é um sistema de controle de versão distribuído (DVCS) que permite que vários desenvolvedores ou outros colaboradores trabalhem em um projeto. Ele fornece um modo de trabalhar com um ou mais branches locais e os envia por push para um repositório remoto. O Git é responsável por tudo relacionado ao GitHub que acontece localmente no seu computador. Os principais recursos do Git incluem:

Ele é instalado e usado no seu computador local
Lida com controle de versão
Dá suporte à ramificação
Para obter mais informações sobre o Git, consulte Usando o Git.

O GitHub é uma plataforma de nuvem que usa o Git como sua tecnologia principal. Ele simplifica o processo de colaboração em projetos e fornece um site, ferramentas de linha de comando e um fluxo geral que permite que os desenvolvedores e usuários trabalhem juntos. O GitHub atua como o "repositório remoto" mencionado anteriormente na seção Git.

Os principais recursos do GitHub incluem:

Problemas
Discussões
Solicitações de pull
Notificações
Rótulos
Ações
Garfos
Projetos
Para obter mais informações sobre o GitHub, consulte Introdução ao GitHub.

Problemas
Os problemas são os locais em ocorre a maior parte da comunicação entre os consumidores e a equipe de desenvolvimento de um projeto. Você pode criar um problema para discutir um amplo conjunto de tópicos, incluindo relatórios de bugs, solicitações de recursos, esclarecimentos sobre documentação e muito mais. Uma vez criado um problema, você poderá atribuir proprietários, rótulos, projetos e marcos. Você também pode associar problemas com solicitações de pull e outros itens do GitHub para fornecer uma possível rastreabilidade futura.

Captura de tela de um problema do GitHub que fornece comentários aos desenvolvedores sobre uma sugestão de bug ou recurso.

Para obter mais informações sobre os problemas do GitHub, consulte Sobre os Problemas.

Notificações
Como uma plataforma colaborativa, o GitHub oferece notificações para praticamente todos os eventos que ocorrem em um determinado fluxo de trabalho. Você pode ajustar essas notificações para atender às suas preferências. Por exemplo, você pode se inscrever em todas as criações e edições de problemas em um projeto ou receber apenas as notificações de problemas nos quais você é mencionado. Você também pode decidir se receberá notificações por email, pela Web e por dispositivos móveis, ou por ambos. Para manter o controle de todas as suas notificações em diferentes projetos, use o Painel de Notificações do GitHub.

Captura de tela do painel de Notificações do GitHub. O GitHub fornece uma caixa de entrada que os desenvolvedores utilizam para se manterem atualizados sobre as alterações nos repositórios.

Para saber mais sobre as notificações do GitHub, confira Configurar notificações.

Branches
Os branches são a maneira preferida de criar alterações no fluxo do GitHub. Eles fornecem isolamento para que várias pessoas possam trabalhar simultaneamente no mesmo código de forma controlada. Esse modelo permite a estabilidade entre branches críticos, como o main, ao mesmo tempo que permite que os desenvolvedores confirmem as alterações necessárias para atender às metas. Uma vez que o código de uma ramificação esteja pronto para se tornar parte da ramificação main, você poderá mesclá-lo por meio da solicitação de pull.

Fluxo do GitHub com um branch de recurso. As alterações feitas em um branch podem ser mescladas novamente no branch principal.

Para saber mais sobre branches do GitHub, confira Sobre branches.

Confirmações
Um commit é um instantâneo de uma ou mais alterações em um ou mais arquivos em uma ramificação. Toda vez que uma confirmação é criada, é atribuído a ela uma ID exclusiva, que é rastreada juntamente com o tempo e o colaborador. Isso fornece uma trilha de auditoria clara para qualquer pessoa que revise o histórico de um arquivo ou item vinculado, como um problema ou uma solicitação de pull.

Captura de tela de uma lista de confirmações do GitHub para uma ramificação principal.

Para saber mais sobre as confirmações do GitHub, confira Confirmando e revisando alterações em seu projeto.

Solicitações de pull
Uma solicitação de pull é o mecanismo usado para sinalizar que as confirmações de um branch estão prontas para serem mescladas em outro branch. O desenvolvedor que envia a solicitação de pull muitas vezes solicitará um ou mais revisores para verificar o código e aprovar a mesclagem. Esses revisores têm a oportunidade de comentar sobre as alterações, adicionar as próprias ou usar a solicitação de pull para uma discussão adicional. Uma vez que as alterações forem aprovadas (se a aprovação for obrigatória), a ramificação de origem da solicitação de pull (a ramificação de comparação) poderá ser mesclada à ramificação de base.

Captura de tela de uma solicitação de pull do GitHub; as solicitações de pull fornecem uma maneira de obter as confirmações de uma ramificação em outra ramificação.

Para saber mais sobre solicitações de pull do GitHub, confira Sobre solicitações de pull.

Rótulos
Os rótulos fornecem um modo de categorizar e organizar problemas e solicitações de pull em um repositório. Ao criar um repositório GitHub, vários rótulos são adicionados automaticamente para você. Você também pode criar.

Exemplos de Rótulos incluem:

bug
documentação
duplicado
help wanted
melhoria
pergunta
Captura de tela das etiquetas do GitHub, que você pode utilizar para categorizar seus problemas e solicitações de pull do repositório GitHub.

Para obter mais informações sobre os rótulos do GitHub, consulte Gerenciando rótulos.

Ações
O GitHub Actions fornece automação de tarefas e funcionalidade de fluxo de trabalho em um repositório. Você pode utilizar ações para simplificar os processos no seu ciclo de vida de desenvolvimento de software e implantar a integração contínua e a implantação contínua (CI/CD).

O GitHub Actions tem os seguintes componentes:

Fluxos de trabalho: Processos automatizados adicionados ao seu repositório.
Eventos: Uma atividade que dispara um fluxo de trabalho.
Trabalhos: Um conjunto de etapas que são realizadas em um executor.
Etapas: Uma tarefa que pode executar um ou mais comandos (ações).
Ações: comandos autônomos que podem ser combinados em etapas. Você pode combinar várias etapas para criar um trabalho.
Executores: Um servidor que tem o aplicativo de executor do GitHub Actions instalado.
Diagrama do GitHub Actions, que fornece uma maneira de automatizar o ciclo de vida do desenvolvimento de software.

Para obter mais informações sobre o GitHub Actions, consulte Entendendo o GitHub Actions.

Clonagem e bifurcação
O GitHub fornece várias maneiras de copiar um repositório para que você possa trabalhar nele.

Clonagem de um repositório: a clonagem de um repositório faz uma cópia do repositório e do seu histórico no computador local. Se você tiver acesso de gravação ao repositório, poderá enviar por push as alterações do computador local para o repositório remoto (chamado de origem) à medida que elas forem concluídas. Para clonar um repositório, você pode usar o comando git clone [url] ou o comando gh repo clone [url] da CLI do GitHub.
Bifurcação de um repositório: a bifurcação de um repositório faz uma cópia do repositório na sua conta do GitHub. O repositório pai é chamado de upstream, enquanto sua cópia bifurcada é chamada de origem. Depois de ter criado fork de um repositório na sua conta do GitHub, você pode cloná-lo em seu computador local. A bifurcação permite que você faça alterações livremente em um projeto sem afetar o repositório original de upstream. Para reverter as alterações para o repositório upstream, crie uma solicitação de pull por meio do seu repositório bifurcado. Você também pode executar os comandos git para garantir que a sua cópia local permaneça sincronizada com o repositório de upstream.
Quando você clonaria um repositório em vez de bifurcá-lo? Se você estiver trabalhando com um repositório e tiver acesso de gravação, poderá cloná-lo no seu computador local. A partir daí, você pode fazer alterações e enviar suas mudanças diretamente para o repositório de origem.

Se você precisar trabalhar com um repositório criado por outro proprietário, como github/example, e não tiver acesso de gravação, poderá bifurcar o repositório na sua conta do GitHub e, em seguida, clonar a bifurcação no seu computador local. Para ver isso visualmente, vamos supor que a sua conta do GitHub tenha o nome de githubtraining. Usando o site do GitHub, você pode bifurcar github/example ou qualquer outro repositório na sua conta. Em seguida, você pode clonar a versão bifurcada do repositório no seu computador local. A imagem a seguir ilustra essas etapas:

Diagrama de bifurcação de um repositório, que cria uma cópia dele em sua conta do GitHub. Em seguida, você pode clonar a cópia bifurcada no seu computador local.

Você pode fazer alterações na sua cópia local de githubtraining/example e, em seguida, enviar por push para o repositório remoto de origem (githubtraining/example). Em seguida, você pode enviar essas alterações para o repositório github/exampleupstream utilizando uma solicitação de pull, conforme mostrado na imagem a seguir:

Diagrama mostrando como você pode enviar as alterações locais para o repositório de origem e, em seguida, criar uma solicitação de pull para efetuar as alterações no repositório upstream.

Para saber mais, confira Bifurcar um repositório.

GitHub Pages
As GitHub Pages são um mecanismo de hospedagem criado diretamente na sua conta do GitHub. Ao seguir algumas convenções e habilitar o recurso, você pode criar seu próprio site estático gerado a partir de um código HTML e markdown efetuado diretamente do seu repositório.

Captura de tela do GitHub Pages, a qual é um mecanismo de hospedagem disponível com sua conta do GitHub. Você pode usá-lo para hospedar sites estáticos gerados a partir de seu repositório.

Para saber mais, confira GitHub Pages.

https://docs.github.com/pt/get-started/quickstart/github-flow




### Exercício – um tour guiado pelo GitHub


Este exercício verifica seu conhecimento dos principais recursos do GitHub, incluindo a confirmação de uma ramificação, a confirmação de um arquivo, a abertura de uma solicitação de pull e a mesclagem de uma solicitação de pull.

Introdução
Ao selecionar o botão Iniciar o exercício no GitHub abaixo, você será direcionado para um repositório público de modelos do GitHub que solicita que você conclua uma série de pequenos desafios. Para iniciar o exercício, conclua estas tarefas:

Selecione o botão Iniciar curso ou o recurso Usar este modelo no repositório de modelos. Isso solicitará que você crie um repositório. É recomendável criar um repositório público, pois repositórios privados usarão minutos do Actions.

Depois de criar seu próprio repositório com base no modelo, aguarde cerca de 20 segundos e atualize.

Siga as instruções no arquivo LEIA-ME do repositório para entender como o exercício funciona, seus objetivos de aprendizado e como concluir o exercício com êxito.

Ao concluir o exercício no GitHub, volte aqui para:

Uma rápida verificação de conhecimentos
Um resumo do que você aprendeu
Receber o selo de conclusão deste módulo



### Verificação de conhecimentos


1. Qual é a melhor maneira de relatar um bug em um projeto do GitHub? 

Enviar um email para um proprietário do projeto.

Eu não me importo em relatar bugs de software porque não há transparência e eles nunca são corrigidos de qualquer forma.

Procure o bug nos problemas existentes do projeto e crie um se ele ainda não tiver sido relatado.
Os problemas de um projeto são visíveis para qualquer pessoa que tenha acesso ao projeto, portanto, você pode encontrar uma resolução que já esteja planejada ou disponível. Caso contrário, você pode criar e acompanhar o problema por conta própria.

2. Suponha que você tenha criado uma correção de bugs em uma nova ramificação e deseje que ela faça parte da próxima compilação na produção gerada a partir da ramificação main. O que você deverá fazer em seguida? 

Copie as alterações do branch e confirme-as diretamente no branch main.

Crie uma solicitação de pull para mesclar o novo branch na ramificação main.
As solicitações de pull são a maneira correta de comunicar que as confirmações estão prontas para revisão e inclusão final no branch main.


Pensando melhor, talvez eu não compartilhe essa correção. Vou apenas colocá-la em minha própria versão privada do código-fonte.
3. Suponha que você gostaria de trabalhar com um projeto no GitHub, mas não tem acesso de gravação ao projeto. O que você pode fazer para contribuir? 

Bifurque o repositório do projeto para a sua conta do GitHub, clone o repositório bifurcado para o seu computador local, envie por push as alterações para o repositório e envie uma solicitação de pull para o repositório de destino (upstream).
O GitHub fornece a funcionalidade de bifurcação projetada para permitir que você trabalhe com projetos nos quais você não é proprietário ou não tem acesso de gravação. A bifurcação faz uma cópia remota do projeto no seu repositório que você pode clonar localmente. Para enviar atualizações para o repositório de destino (repositório upstream), você pode enviar uma solicitação de pull.


Clone o projeto no seu computador local e envie por push atualizações diretamente para o repositório do projeto.

Use comandos git para fazer uma cópia do projeto para que você possa trabalhar localmente. Envie um problema para obter suas alterações no repositório de destino.

### Resumo

Neste módulo, você aprendeu sobre os principais recursos do GitHub, incluindo problemas, confirmações e solicitações de pull. Você também usou GitHub Pages para publicar um site público com base no conteúdo do seu projeto.

Você aprendeu a:

Comunicação com a comunidade do projeto em relação aos problemas.
Gerenciar as notificações de eventos do projeto.
Criação de ramificações para gerenciar o trabalho em paralelo.
Fazendo confirmações para atualizar o código-fonte do projeto.
Introdução às alterações com solicitações de pull.
Implantação de uma página da Web no GitHub Pages.
Diferenças entre o Git e o GitHub e as funções que eles desempenham no ciclo de vida de desenvolvimento de software.
Como um repositório bifurcado difere de um clone.
Rótulos de repositório nos quais podem ser aplicados em problemas e solicitações de pull.






















This sample post tests the followings:

- Category, sub-category nesting in the sidebar.
- Hero image and other images are in `images` folder inside this post directory.
- Different media rendering like image, tweet, YouTube video, Vimeo video etc.

### Image Sample

{{< img src="/posts/category/sub-category/rich-content/images/forest.jpg" align="center" title="Forest">}}

{{< vs >}}

### Tweet Sample

{{< tweet user="SanDiegoZoo" id="1453110110599868418" >}}

{{< vs >}}

### YouTube Video Sample

{{< youtube ZJthWmvUzzc >}}

{{< vs >}}

### Vimeo Video Sample

{{< vimeo 48912912 >}}
