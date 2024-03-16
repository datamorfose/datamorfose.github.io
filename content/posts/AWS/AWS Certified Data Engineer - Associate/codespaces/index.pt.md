---
title: "Github Codespaces"
date: 2023-06-08T08:06:25+06:00
description: Sample post with multiple images, embedded video ect.
menu:
  sidebar:
    name: Github Codespaces
    identifier: devops-git-codespaces
    parent: devops-git
    weight: 10
hero: images/github-codespaces.jpg
tags: ["Markdown","Content Organization","Multi-lingual"]
categories: ["Básico"]
---


##  Codificar com o GitHub Codespaces

### Introdução

O GitHub Codespaces é um ambiente de desenvolvimento instantâneo e baseado em nuvem que usa um contêiner para fornecer linguagens, ferramentas e utilitários de desenvolvimento comuns.

Neste módulo, nós vamos:

Explorar o ciclo de vida e os processos dos Codespaces.
Examinar as maneiras de personalizar a configuração do Codespace.
Comparar as diferenças entre o GitHub Codespaces e GitHub.dev.
Concluir um exercício para praticar a codificação no Codespaces.


 
### O ciclo de vida do Codespace
O GitHub Codespaces é configurável, permitindo que você crie um ambiente de desenvolvimento personalizado para seu projeto. Ao configurar um ambiente de desenvolvimento personalizado para o projeto, você pode ter uma configuração reproduzível do Codespace para todos os usuários do projeto.

O ciclo de vida de um Codespace começa quando você cria um Codespace e termina quando você o exclui. Você pode se desconectar e reconectar a um Codespace ativo sem afetar os processos em execução. Você pode parar e reiniciar um Codespace sem perder as alterações feitas no projeto.

Criar um Codespace
Você pode criar um Codespace no GitHub.com, no Visual Studio Code ou usando a CLI do GitHub. Há quatro maneiras de criar um Codespace:

Usando um modelo do GitHub ou qualquer repositório de modelos no GitHub.com para iniciar um novo projeto.
Usando um branch em seu repositório para um novo trabalho com recursos.
De um pull request aberto para explorar o trabalho em andamento.
Usando um commit no histórico do repositório para investigar um bug em um momento específico.
Você pode usar um Codespace temporariamente para testar o código ou pode voltar ao mesmo Codespace para continuar um trabalho de recursos de longa execução.

Você pode criar mais de um Codespace por repositório ou até mesmo por branch. No entanto, há limites quanto ao número de Codespaces que você pode criar e o que você pode executar ao mesmo tempo. Se você atingir o número máximo de Codespaces e tentar criar outro, uma mensagem informará que um Codespace existente precisa ser removido/excluído antes que outro Codespace possa ser criado.

Você pode criar um Codespace sempre que desenvolver no GitHub Codespaces ou pode manter um Codespace de execução prolongada para um recurso. Se estiver iniciando um novo projeto, crie um Codespace usando um modelo e publique-o em um repositório no GitHub posteriormente.

Ao criar um Codespace sempre que trabalhar em um projeto, você deverá efetuar push das alterações regularmente para garantir que os novos commits estejam no GitHub. Ao usar um Codespace de execução prolongada para um novo projeto, efetue pull do branch padrão do repositório sempre que começar a trabalhar no Codespace. Isso permite que o ambiente obtenha os commits mais recentes. O fluxo de trabalho é semelhante a trabalhar com um projeto em um computador local.

Administradores de repositório podem habilitar pré-compilações do GitHub Codespaces para um repositório para acelerar a criação do Codespace.

Para obter orientações detalhadas e diretrizes passo a passo, confira os recursos Guia para iniciantes para aprender a codificar com o GitHub Codespaces e Desenvolver em um Codespace, localizados na unidade Resumo no final deste módulo.
https://learn.microsoft.com/pt-br/training/modules/code-with-github-codespaces/2-codespace-lifecycle

Ao criar um GitHub Codespace, ocorrem quatro processos:

A VM e o armazenamento são atribuídos ao Codespace.
Um contêiner é criado.
É feita uma conexão com o Codespace.
É feita uma configuração pós-criação.


Salvar alterações em um Codespace
Quando você se conecta a um Codespace por meio da Web, o salvamento automático é habilitado automaticamente para salvar as alterações após um período específico ter passado. Quando se conecta a um Codespace usando o Visual Studio Code em execução na área de trabalho, você precisa habilitar o salvamento automático.

O trabalho é salvo em uma máquina virtual na nuvem. Você pode fechar e parar um Codespace e voltar ao trabalho salvo posteriormente. Se tiver alterações não salvas, você receberá um prompt para salvá-las antes de sair. No entanto, se o Codespace for excluído, seu trabalho será perdido. Para salvar o trabalho, você precisa fazer commit das alterações e efetuar push delas para seu repositório remoto ou publicar o trabalho em um novo caso você tenha criado seu Codespace usando um modelo.

Abrir um Codespace existente
Você pode reabrir qualquer um de seus Codespaces ativos ou parados no GitHub.com, em um IDE do JetBrains, no Visual Studio Code ou usando a CLI do GitHub.

Para retomar um Codespace existente, você pode ir para o repositório onde ele existe e pressionar a tecla "," no teclado e selecionar Retomar este codespace ou abrir https://github.com/codespaces no navegador, selecionar o repositório e selecionar o Codespace existente.

Tempos limite para um Codespace
Se um Codespace estiver inativo ou se você sair dele sem pará-lo explicitamente, o aplicativo atingirá o tempo limite após um período de inatividade e deixará de ser executado. O tempo limite padrão é atingido após 30 minutos de inatividade. Não é possível personalizar a duração do tempo limite para novos Codespaces. Quando um Codespace atinge o tempo limite, seus dados são preservados da última vez em que alterações foram salvas.

Conexão com a Internet usando o GitHub Codespaces
Um Codespace requer uma conexão com a Internet. Se a conexão com a Internet for perdida durante seu trabalho em um Codespace, você não poderá acessar o Codespace. No entanto, as alterações não confirmadas serão salvas. Quando restabelecer a conexão com a Internet, você poderá acessar o Codespace no mesmo estado em que ele foi deixado quando a conexão foi perdida.

Se você tiver uma conexão instável com a Internet, faça commit e efetue push de suas alterações com frequência.

Fechar ou parar um Codespace
Se você sair do Codespace sem executar o comando de parar (por exemplo, fechando a aba do navegador) ou deixar o Codespace em execução sem interação, o Codespace e os processos em execução continuarão durante o período do tempo de inatividade. O período de tempo limite de inatividade padrão é de 30 minutos. Você pode definir sua configuração de tempo limite para os Codespaces que criar, mas isso pode ser anulado por uma política de tempo limite da organização.

Somente Codespaces em execução incorrem em encargos de CPU. Um Codespace parado incorre apenas em custos de armazenamento.

Você pode parar e reiniciar um Codespace para aplicar alterações. Por exemplo, se você alterar o tipo de computador usado no Codespace, precisará parar e reiniciá-lo para que a alteração entre em vigor. Quando você fecha ou para o Codespace, todas as alterações não confirmadas são preservadas até você se conectar novamente ao Codespace.

Você também pode parar o Codespace e optar por reiniciá-lo ou excluí-lo se encontrar um erro ou algo inesperado.

Recompilar um Codespace
Você pode recompilar o Codespace para implementar alterações em sua configuração de contêiner de desenvolvimento. Para a maioria dos usos, você pode criar um Codespace como alternativa à recompilação de um Codespace. Quando você recompila o Codespace, as imagens do cache aceleram o processo de recompilação. Você também pode executar uma recompilação completa para limpar o cache e recompilar o contêiner com imagens novas.

Quando você recompila o contêiner em um Codespace, as alterações feitas fora do diretório /workspaces são limpas. Alterações feitas dentro do diretório /workspaces, incluindo o clone do repositório ou modelo com base no qual você criou o Codespace, são preservadas em uma recompilação.

Excluir um Codespace
Você pode criar um Codespace para uma tarefa específica. Após efetuar push de alterações para um branch remoto, você poderá excluir com segurança esse Codespace.

Se você tentar excluir um Codespace com git commits que não foram enviados por push, o editor notificará você de que há alterações que não foram enviadas por push para um branch remoto. Você pode efetuar push de qualquer alteração desejada e excluir o Codespace. Você também pode excluir o Codespace e as alterações não confirmadas ou exportar o código para um novo branch sem criar um Codespace.

Codespaces parados que permanecem inativos por um período especificado são excluídos automaticamente. Codespaces inativos são excluídos após 30 dias, mas você pode personalizar os intervalos de retenção do Codespace.




### Personalizar seu Codespace

O GitHub Codespaces é um ambiente dedicado para você. Você pode configurar seus repositórios com um contêiner de desenvolvimento para definir o ambiente padrão do GitHub Codespaces e personalizar sua experiência de desenvolvimento em todos os seus Codespaces com dotfiles e a Sincronização de Configurações.

O que você pode personalizar
Há várias maneiras de personalizar um Codespace. Vamos examinar cada uma delas.

Sincronização de Configurações: Você pode sincronizar suas configurações do Visual Studio Code (VS Code) entre o aplicativo da área de trabalho e o cliente Web do VS Code.
Dotfiles: você pode usar um repositório dotfiles para especificar scripts, preferências de shell e outras configurações.
Renomear um Codespace: quando você cria um Codespace, ele recebe um nome de exibição gerado automaticamente. Se você tiver vários Codespaces, o nome de exibição ajudará a diferenciar entre eles. Você pode alterar o nome de exibição do Codespace.
Alterar seu shell: você pode alterar seu shell em um Codespace para manter a configuração com a qual está acostumado. Ao trabalhar em um Codespace, você pode abrir uma nova janela de terminal com um shell de sua escolha, alterar o shell padrão para novas janelas de terminal ou instalar um novo shell. Você também pode usar dotfiles para configurar o shell.
Alterar o tipo de computador: você pode alterar o tipo de computador que está executando o Codespace para usar os recursos apropriados ao trabalho que está fazendo.
Definir o editor padrão: você pode definir o editor padrão para Codespaces em sua página de configurações pessoais. Defina sua preferência de editor para que, ao criar um Codespace ou abrir um Codespace existente, ele seja aberto no editor padrão.
Visual Studio Code (aplicativo da área de trabalho)
Visual Studio Code (aplicativo cliente Web)
JetBrains Gateway – para abrir Codespaces em um IDE do JetBrains
JupyterLab – A interface Web do Project Jupyter
Definir a região padrão: você pode definir sua região padrão na página de configurações do perfil do GitHub Codespaces para personalizar o local onde os dados são mantidos.
Definir o tempo limite: um Codespace deixará de ser executado após um período de inatividade. Por padrão, esse período é de 30 minutos, mas você pode especificar um período de tempo limite padrão maior ou menor nas configurações pessoais no GitHub. A configuração atualizada se aplica a todos os Codespaces que você criar ou aos Codespaces existentes na próxima inicialização.
Configurar a exclusão automática: Codespaces inativos são excluídos automaticamente. Você pode escolher por quanto tempo Codespaces parados são retidos, até, no máximo, 30 dias.
Informações adicionais e instruções passo a passo sobre a personalização estão localizadas na unidade Resumo no final deste módulo.

Adicionar ao Codespace com extensões ou plug-ins
Você pode adicionar plug-ins e extensões em um Codespace para personalizar sua experiência no JetBrains e no VS Code.

Extensões do VS Code
Se você trabalha em seus Codespaces e no aplicativo da área de trabalho do VS Code ou no cliente Web, pode adicionar as extensões necessárias do Marketplace do Visual Studio Code. Consulte Suporte ao desenvolvimento remoto e ao GitHub Codespaces na documentação do VS Code para obter informações sobre como as extensões são executadas no GitHub Codespaces.

Se você já usa o VS Code, use a Sincronização de Configurações para sincronizar automaticamente extensões, configurações, temas e atalhos de teclado entre a instância local e os Codespaces que você criar.

Plug-ins do JetBrains
Se você trabalha nos Codespaces em um IDE do JetBrains, pode adicionar plug-ins do Marketplace do JetBrains.



### Codespaces versus editor GitHub.dev
Provavelmente, você está se perguntando, quando devo usar o GitHub Codespaces e quando devo usar GitHub.dev?

Você pode usar GitHub.dev para navegar por arquivos e repositórios de código-fonte do GitHub e fazer e confirmar alterações de código. Você pode abrir qualquer repositório, bifurcação ou PR no editor GitHub.dev.

Se quiser fazer um trabalho mais pesado, como testar o código, use o GitHub Codespaces. Ele tem computação associada para que você possa criar o código, executar o código e ter acesso ao terminal. GitHub.dev não tem computação. Com o GitHub Codespaces, você obtém o poder de uma VM (Máquina Virtual) pessoal com acesso ao terminal, da mesma maneira que poderia usar seu ambiente local, só que na nuvem.

Comparação entre Codespaces e GitHub.dev
A seguinte tabela lista as diferenças principais entre Codespaces e GitHub.dev:

GitHub.dev	Codespaces do GitHub
Custo	Gratuita	Cota mensal gratuita de uso para contas pessoais
Disponibilidade	Disponível para todos no GitHub.com	Disponível para todos no GitHub.com
Inicialização	GitHub.dev é aberto de maneira instantânea com um toque de tecla, e você pode começar a usá-lo imediatamente, sem precisar aguardar uma configuração ou uma instalação	Quando você cria ou retoma um Codespace, o Codespace é atribuído a uma VM e o contêiner é configurado com base no conteúdo de um arquivo devcontainer.json. Essa configuração leva alguns minutos para criar o ambiente de desenvolvimento.
Computação	Não há nenhuma computação associada, portanto, você não conseguirá criar e executar o código nem usar o terminal integrado.	Com o GitHub Codespaces, você tem a potência de uma VM dedicada para executar e depurar seu aplicativo.
Acesso ao terminal	Nenhum	O GitHub Codespaces fornece um conjunto comum de ferramentas por padrão, o que significa que você pode usar o Terminal exatamente como faria no ambiente local.
Extensões	Apenas um subconjunto de extensões que podem ser executadas na Web aparecerão na visualização de extensões e poderão ser instaladas	Com o GitHub Codespaces, você pode usar a maioria das extensões do Marketplace do Visual Studio Code.
Continuar trabalhando em Codespaces
Você pode começar seu fluxo de trabalho no GitHub.dev e continuar em um Codespace. Se você tentar acessar a Exibição de Execução e Depuração ou o terminal, receberá uma mensagem de que eles não estão disponíveis no GitHub.dev.

Para continuar o trabalho em um Codespace, selecione Continuar Trabalhando.... Selecione Criar Codespace para criar um Codespace no branch atual. Antes de selecionar esta opção, você precisa fazer commit de quaisquer alterações.

### Exercício – Codificar com o Codespaces e o Visual Studio Code

Agora que você entende o ciclo de vida e os processos do Codespaces, é hora de praticar a codificação no Codespaces e no Visual Studio Code (VS Code). Siga as instruções abaixo para concluir este exercício.

Instruções
Clique com o botão direito do mouse no link do exercício do GitHub para abri-lo em uma nova guia.
Na página inicial do exercício do GitHub, clique com o botão direito do mouse no botão Iniciar curso para abri-lo em uma nova guia.
Na nova guia, a maioria dos prompts é preenchida automaticamente para você.
Para proprietário, escolha sua conta pessoal ou uma organização para hospedar o repositório.
É recomendável criar um repositório público, pois repositórios privados usam minutos do GitHub Actions.
Role para baixo e selecione o botão Criar repositório na parte inferior do formulário.
Após o repositório ser criado, aguarde cerca de 20 segundos e atualize a página. Siga as instruções passo a passo no LEIAME do novo repositório.
Após concluir o exercício no GitHub, volte aqui para:

Concluir uma verificação de conhecimentos.
Revisar um resumo do que você aprendeu neste módulo.
Receber um selo pela conclusão deste módulo.

### Verificação de conhecimentos

1. Em qual diretório é o clone colocado depois de criar um Codespace? 

Diretório /workspaces
Correto. Após você criar um Codespace, o clone é colocado no diretório /workspace.


Diretório /temp

Diretório ~/.bashrc

Diretório Linux
2. Qual é o número máximo de Codespaces que você pode criar por repositório ou branch? 

Você só pode criar dois Codespaces.

Você pode criar um total de dez Codespaces.

Você pode criar um total de trinta Codespaces.

Você pode criar um número ilimitado de Codespaces por repositório ou branch, dependendo do espaço disponível. Quando você atinge uma quantidade superior de recursos, uma mensagem informa que um Codespace existente precisa ser removido/excluído antes que um Codespace possa ser criado.
Correto. Você pode ter um número ilimitado de Codespaces por repositório ou até mesmo por branch. No entanto, há limites quanto ao número de Codespaces que você pode criar e o que você pode executar ao mesmo tempo.

3. O que acontece quando o Codespace perde a conectividade com a Internet? 

Se a conexão com a Internet for perdida durante seu trabalho em um Codespace, você não poderá acessar o Codespace.
Correto. Um Codespace requer uma conexão com a Internet. Se a conexão com a Internet for perdida durante seu trabalho em um Codespace, você não poderá acessar o Codespace.


O Codespace não exige uma conexão com a Internet. Posso acessar meu Codespace independentemente de perder a conectividade.
Incorreto. Um Codespace requer uma conexão com a Internet.


Se você perder a conexão com a Internet ao trabalhar no Codespace, suas alterações não serão salvas.
4. O que define o início do ciclo de vida de um Codespace? 

O ciclo de vida de um Codespace começa quando você cria um Codespace e termina quando você o exclui.
Correto. O ciclo de vida de um Codespace começa quando você cria um Codespace e termina quando você o exclui.


O ciclo de vida de um Codespace começa imediatamente quando o GitHub é aberto e termina quando o software é fechado.

O ciclo de vida de um Codespace começa quando um repositório é criado e termina quando ele é excluído.

###  Resumo

Neste módulo, você aprendeu sobre o GitHub Codespaces, um ambiente de desenvolvimento totalmente configurado hospedado na nuvem.

Agora você deve estar apto a:

Descreva o GitHub Codespaces.
Explique o ciclo de vida do GitHub Codespaces e como executar cada etapa.
Defina as diferentes personalizações que você pode fazer com o GitHub Codespaces.
Identifique as diferenças entre GitHub.dev e o GitHub Codespaces.

## Introdução ao GitHub Copilot


### Introdução


O GitHub Copilot é a primeira ferramenta de desenvolvedor de IA em escala do mundo que pode ajudar você a escrever código mais rapidamente com menos trabalho. O GitHub Copilot supõe o contexto a partir de comentários e código para sugerir linhas individuais e funções inteiras instantaneamente.

Pesquisas descobriram que o GitHub Copilot ajuda os desenvolvedores a codificar mais rapidamente, se concentrar em resolver problemas maiores, permanecer no fluxo por mais tempo e se sentir mais satisfeito com seu trabalho.

Com tecnologia do Codex da OpenAI, o modelo de linguagem pré-treinado generativo do GitHub Copilot é criado pela OpenAI. Uma extensão está disponível para Visual Studio Code, Visual Studio, Neovim e o pacote JetBrains de IDEs (ambientes de desenvolvimento integrados).

Objetivos de aprendizagem
Ao final deste módulo, você saberá como:

Explique o que é o GitHub Copilot e as vantagens que ele oferece.
Entenda a disponibilidade do GitHub Copilot para pessoas e negócios.
Debata sobre o futuro do GitHub Copilot com o Copilot X.
Saber como começar a usar o GitHub Copilot e algumas configurações comuns.
Desenvolva usando o GitHub Copilot com Visual Studio Code usando exercícios práticos.


###  GitHub Copilot, programador de par de IA

Não é segredo que a IA está causando uma disrupção no cenário tecnológico. A IA está mudando profundamente a maneira como o mundo funciona e como cada organização e equipe operam. Esses avanços na IA servem como um catalisador e melhoram drasticamente a produtividade dos desenvolvedores em todo o mundo à medida que são usados e bem aplicados.

Quando se trata de desenvolvedores, adicionar recursos de IA às ferramentas que os desenvolvedores usam e adoram ajuda na colaboração, no desenvolvimento, teste e na entrega dos produtos com mais rapidez e eficiência do que nunca.

O GitHub Copilot é um serviço que fornece um programador em pares de IA que funciona com todas as linguagens de programação populares e acelera drasticamente a produtividade geral do desenvolvedor. Em pesquisas recentes, o GitHub e a Microsoft descobriram que os desenvolvedores experimentam um aumento significativo de produtividade ao trabalhar em projetos e tarefas do mundo real ao usar o GitHub Copilot. Na verdade, em menos de dois anos desde seu lançamento, os desenvolvedores obtiveram o seguinte ao usar o GitHub Copilot:

46% do novo código agora é escrito por IA
55% mais rapidez na produtividade geral do desenvolvedor
74% dos desenvolvedores se sentem mais focados em um trabalho mais satisfatório
Desenvolvido em colaboração com a OpenAI, o GitHub Copilot é alimentado pelo Codex da OpenAI, um sistema de IA criado pela OpenAI. O Codex da OpenAI tem amplo conhecimento de como as pessoas usam código e tem mais capacidade do que o GPT-3 na geração de código, em parte, porque foi treinado em um conjunto de dados que inclui uma maior concentração de código-fonte público.

O GitHub Copilot está disponível como uma extensão para Visual Studio Code, Visual Studio, Neovim e o pacote JetBrains de IDEs (ambientes de desenvolvimento integrados).

GitHub Copilot X
O GitHub Copilot iniciou uma nova era de desenvolvimento de software como um programador em pares de IA que mantém os desenvolvedores no fluxo por meio do preenchimento automático de comentários e código. Mas a preenchimento automático alimentado por IA é apenas o ponto de partida. O GitHub Copilot X é a visão para o futuro do desenvolvimento de software com tecnologia de IA que adota os modelos GPT-4 mais recentes da OpenAI.

O GitHub Copilot X se estende para além do editor e em um assistente de IA prontamente acessível durante todo o ciclo de vida do desenvolvimento.

Estes são alguns recursos que você pode esperar do GitHub Copilot X em breve:

Uma experiência semelhante ao ChatGPT no seu editor com o GitHub Copilot Chat
O Copilot X traz uma interface de chat para o editor focada em cenários de desenvolvedor e se integra nativamente ao VS Code e ao Visual Studio. Ele reconhece qual código um desenvolvedor digitou, quais mensagens de erro são mostradas e está profundamente inserido no IDE. Um desenvolvedor pode obter análises detalhadas e explicações sobre o que os blocos de código devem fazer, gerar testes de unidade e até mesmo obter propostas de correções para bugs.

Copilot para solicitações de pull
Essa nova funcionalidade tem tecnologia do novo modelo GPT-4 da OpenAI e adiciona suporte a tags alimentadas por IA em descrições de PR (solicitação de pull) por meio de um aplicativo GitHub que os administradores da organização e proprietários de repositórios individuais podem instalar. Essas tags são preenchidas automaticamente pelo GitHub Copilot com base no código alterado. Em seguida, os desenvolvedores podem examinar ou modificar a descrição sugerida.

Respostas geradas por IA sobre documentação
O GitHub está lançando o GitHub Copilot for Docs, uma ferramenta experimental que usa uma interface de chat para fornecer aos usuários respostas geradas por IA a perguntas sobre documentação, incluindo perguntas que os desenvolvedores têm sobre as linguagens, estruturas e tecnologias que estão usando.

Copilot para a CLI (interface de linha de comando)
Ao lado do editor e da solicitação de pull, o terminal é o local onde os desenvolvedores passam mais tempo. Mas mesmo os desenvolvedores mais proficientes precisam percorrer muitas páginas para lembrar a sintaxe precisa de muitos comandos. A CLI do GitHub Copilot pode compor comandos e loops e gerar sinalizadores de localização obscuros para satisfazer sua consulta.

GitHub Copilot for Business
O GitHub Copilot está disponível por meio de contas pessoais do GitHub com o GitHub Copilot for Individuals ou por meio de contas corporativas ou de organização com o GitHub Copilot for Business.

Com o Copilot for Business, você pode gerenciar o acesso ao GitHub Copilot para organizações internas da sua empresa. Depois de conceder a uma organização acesso ao GitHub Copilot, os administradores dela podem conceder acesso a indivíduos e equipes.

Com o GitHub Copilot for Business, o GitHub Copilot fica aberto a todos os desenvolvedores, equipes, organizações e empresas.

Focado em tornar as organizações mais produtivas, seguras e satisfeitas, o GitHub Copilot for Business permite que os desenvolvedores codifiquem mais rapidamente e se concentrem em um trabalho mais satisfatório.

Aqui estão alguns recursos que você pode esperar do Copilot for Business:

Um modelo de IA mais poderoso: novos algoritmos de modelagem melhoram a qualidade das sugestões de código.
Filtragem de vulnerabilidade de segurança baseada em IA: o GitHub Copilot bloqueia automaticamente sugestões comuns de código inseguro, direcionando problemas como credenciais codificadas, injeções de SQL e injeções de caminho.
Suporte a proxy de VPN: o GitHub Copilot funciona com VPNs, inclusive com certificados autoassinados, para que os desenvolvedores possam usá-lo em qualquer ambiente de trabalho.
Inscrição simples: qualquer empresa pode comprar rapidamente licenças do Copilot for Business online e atribuir estações facilmente, mesmo que não usem a plataforma GitHub para seu código-fonte.
Para saber mais sobre o GitHub Copilot for Business, confira os links relacionados no final do módulo.

Na próxima unidade, aprenderemos como começar a usar o GitHub Copilot e algumas configurações comuns.

###  Instalar, configurar e solucionar problemas do GitHub Copilot
Nesta unidade, discutiremos como se inscrever no GitHub Copilot, como configurar o GitHub Copilot usando Visual Studio Code e algumas etapas para solucionar problemas do GitHub Copilot usando Visual Studio Code.

Inscrever-se no GitHub Copilot
Antes de começar a usar o GitHub Copilot, você precisará configurar uma avaliação gratuita ou assinatura para sua conta pessoal.

Você pode fazer isso selecionando sua foto de perfil e selecionando Configurações. O Copilot está no menu à esquerda em Código, planejamento e automação.

Depois de se inscrever, você precisará instalar uma extensão para seu ambiente preferido. O GitHub Copilot dá suporte a GitHub.com, Visual Studio Code, Visual Studio, IDEs JetBrains e Neovim como uma extensão discreta.

Para este módulo específico, vamos apenas examinar extensões e configurações para Visual Studio Code, pois o exercício que concluímos neste módulo usa Visual Studio Code.

Se estiver usando um ambiente diferente, você poderá encontrar links específicos para configurar esses ambientes na seção Referências no final deste módulo.

Configurar o GitHub Copilot no Visual Studio Code
Adicionar a extensão do Visual Studio Code
Siga estas etapas para adicionar a extensão do Visual Studio Code para o GitHub Copilot.

No Marketplace do Visual Studio Code, acesse a página de extensão do GitHub Copilot e selecione Instalar.
Aparece um pop-up solicitando a abertura do Visual Studio Code. Selecione Abrir.
Na guia Extensão: GitHub Copilot no Visual Studio Code, selecione Instalar.
Se você não autorizou anteriormente o Visual Studio Code na sua conta do GitHub, será solicitado que você entre no GitHub no Visual Studio Code. Selecione Entrar no GitHub.
O GitHub Copilot pode preencher código automaticamente conforme você digita ao usar o Visual Studio Code. Após a instalação, você pode habilitar ou desabilitar o GitHub Copilot e definir configurações avançadas no Visual Studio Code.

Habilitar ou desabilitar o GitHub Copilot no Visual Studio Code
Para habilitar ou desabilitar o GitHub Copilot, selecione o ícone de status no painel inferior da janela do Visual Studio Code

Captura de tela do ícone de status do GitHub Copilot no painel inferior da janela do Visual Studio Code. A cor da tela de fundo corresponde à cor da barra de status quando habilitado.

Ao desabilitar o GitHub Copilot, será exibida uma mensagem questionando se você deseja desabilitar as sugestões globalmente ou para a linguagem do arquivo que está editando no momento.

Para desabilitar as sugestões do GitHub Copilot globalmente, selecione Desabilitar globalmente.
Para desabilitar as sugestões do GitHub Copilot para uma linguagem especificada, selecione Desabilitar para LINGUAGEM.
Habilitar ou desabilitar sugestões embutidas no Visual Studio Code
No menu Arquivo, vá até Preferências e clique em Configurações.

Captura de tela do menu Arquivo no Visual Studio Code. O submenu suspenso Preferências está aberto com Configurações selecionadas.

No painel esquerdo da guia de configurações, selecione Extensões e selecione Copilot.

Em Sugestão embutida: Habilitar, marque ou desmarque a caixa de seleção para habilitar ou desabilitar sugestões embutidas

Além disso, você pode optar por habilitar ou desabilitar as sugestões embutidas e especificar para quais linguagens deseja habilitar ou desabilitar o GitHub Copilot.

Como solucionar problemas do GitHub Copilot no Visual Studio Code
No Visual Studio Code, os arquivos de log são úteis para diagnosticar problemas de conexão. A extensão do GitHub Copilot armazena os arquivos de log no local de log padrão para extensões do Visual Studio Code. Você pode encontrar os arquivos de log por meio da opção de desenvolvedor e da pasta de logs de extensão abertos no Visual Studio Code.

Em casos raros, os erros podem não ser registrados nos locais regulares. Se você encontrar erros e não houver nada nos logs, você pode tentar ver os logs do processo que executa o Visual Studio Code e a extensão. Esse processo permite que você exiba os logs do Electron. Você pode encontrar esses logs no desenvolvedor e em Ajuda>Alternar ferramentas de desenvolvedor no Visual Studio Code.

Restrições de rede, do firewall ou do seu proxy podem causar problemas ao se conectar ao GitHub Copilot. Se isso ocorrer, você poderá seguir as próximas etapas para abrir um novo editor com as informações relevantes que você pode inspecionar por conta própria ou compartilhar com a equipe de suporte.

Abra a paleta de comandos do Visual Studio Code:

Para Mac, use Shift+Command+P
Para Windows ou Linux, use Ctrl+Shift+P
Digite Diagnostics (Diagnóstico) e selecione GitHub Copilot: Collect Diagnostics (GitHub Copilot: Coletar Diagnóstico) na lista.

Para obter mais informações sobre como solucionar problemas em outros ambientes, confira a seção Referências na última unidade deste módulo.

### Exercício – Desenvolver com sugestões de código com IA usando o GitHub Copilot e o VS Code

Este exercício orienta você pelas seguintes etapas:

Instalar o GitHub Copilot usando Codespaces do GitHub
Solicitar sugestões de código ao GitHub Copilot
Aceitar sugestões de código do GitHub Copilot
Introdução
Ao clicar no botão Iniciar o exercício no GitHub, você chegará a um repositório público de modelos do GitHub que solicitará que a conclusão de uma série de pequenos desafios. Para iniciar o exercício, conclua estas tarefas:

Selecione o botão Iniciar curso ou o recurso Usar este modelo no repositório de modelos. Essa ação solicitará que você crie um repositório. É recomendável criar um repositório público, pois repositórios privados usarão minutos do Actions. Depois de criar seu próprio repositório com base no modelo, aguarde cerca de 20 segundos e atualize.

Siga as instruções no README do repositório para entender como o exercício funciona, seus objetivos de aprendizado e como concluir o exercício com êxito.

Quando terminar o exercício no GitHub, retorne a este módulo para:

Uma rápida verificação de conhecimentos
Um resumo do que você aprendeu
Receber o selo de conclusão deste módulo

### Verificação de conhecimentos
1. O que é o GitHub Copilot? 

O GitHub Copilot é um programador em pares de IA que você pode usar para obter sugestões de código.
O GitHub Copilot é um programador em pares de IA que você pode usar para obter sugestões para linhas inteiras ou funções inteiras diretamente dentro do seu editor.


O GitHub Copilot é um Codex da OpenAI, um novo sistema de IA criado pela OpenAI.

O GitHub Copilot é um repositório público JavaScript e é uma das linguagens com melhor suporte.

O GitHub Copilot pode escrever um comentário descrevendo a lógica e você pode adicionar o código sugerido para implementar a solução.
2. Quais são as extensões de ambiente de desenvolvimento integrado com suporte para o GitHub Copilot? 

Visual Studio Code e Visual Studio

GitHub.com, Visual Studio Code, Visual Studio, Neovim e JetBrains
Embora o GitHub.com tenha suporte, ele não precisa de uma extensão.


Visual Studio Code, Visual Studio, Neovim e JetBrains
Correto! Todos os IDEs listados têm suporte para extensões do GitHub.

3. O que é GitHub Copilot X? 

A visão do GitHub para o futuro do desenvolvimento de software com tecnologia de IA.
À medida que o cenário das ferramentas para desenvolvedores de IA muda muito rapidamente, o GitHub queria garantir nossa permanência na vanguarda da inovação e dos aprimoramentos.


Um programador em pares de IA (inteligência artificial) que você pode usar para obter sugestões para linhas inteiras ou funções inteiras diretamente dentro do seu editor.

Um produto focado nas organizações para ajudá-las a serem mais produtivas, seguras e satisfeitas.

### Resumo

Desde ler documentos a escrever código até enviar solicitações de pull e além, o GitHub está trabalhando para personalizar o GitHub Copilot para cada equipe, projeto e repositório em que ele é usado, criando um ciclo de vida de desenvolvimento de software radicalmente aprimorado. Junto com o modelo de conhecimento da Microsoft, o GitHub está aproveitando o reservatório de dados e insights existentes em todas as organizações para fortalecer a conexão entre todos os trabalhadores e desenvolvedores. Esses insights permitem que todas as ideias passem do código para a realidade sem atritos. Ao mesmo tempo, o GitHub continua inovando e atualizando o coração do GitHub Copilot, o programador em pares de IA que iniciou tudo.

O GitHub Copilot X está no horizonte e, com ele, uma nova geração de desenvolvedores mais produtivos, satisfeitos e felizes que entregam um software melhor para todos.

Agora que você concluiu este módulo, você deverá estar apto a:

Entender as diferenças entre GitHub Copilot, GitHub Copilot X e GitHub Copilot for Business.
Aprenda a usar e configurar o GitHub Copilot.
Desenvolver usando o GitHub Copilot e o Visual Studio Code.
Referências
Recursos do GitHub Copilot
Sobre o GitHub Copilot
Como usar o GitHub Copilot
Sobre os IDEs do GitHub Copilot e JetBrains
Sobre o GitHub Copilot e o Neovim
Sobre o GitHub Copilot e o Visual Studio
Solução de problemas do GitHub Copilot no ambiente