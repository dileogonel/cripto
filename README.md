# Sistema de Criptomoeda Distribuída Simplificada

O objetivo do sistema é desenvolver uma criptomoeda distribuída simplificada, voltada a fins acadêmicos, capaz de demonstrar conceitos fundamentais de sistemas distribuídos por meio de uma rede composta por cinco nós cooperantes. O sistema deverá permitir que usuários criem carteiras, consultem saldo e enviem moedas entre si, mantendo o registro das operações em um ledger replicado entre todos os nós participantes da rede.

A proposta do projeto é reproduzir, de forma controlada e simplificada, o funcionamento básico de uma infraestrutura de criptomoeda, sem a complexidade de redes públicas abertas e sem mecanismos avançados de mineração. Em vez disso, o foco estará na distribuição do estado, na replicação dos dados, na ordenação consistente das transações e na continuidade do sistema mesmo diante de falhas parciais.

Cada transação realizada no sistema deverá ser assinada digitalmente pelo remetente, garantindo autenticidade e integridade. Um dos cinco nós atuará inicialmente como líder, sendo responsável por organizar a ordem das transações recebidas e propor sua confirmação. Os demais nós atuarão como replicadores e validadores, armazenando cópias atualizadas do ledger e confirmando as operações recebidas. Caso um dos nós falhe, o sistema deverá continuar operando por meio dos nós restantes, preservando a disponibilidade e a integridade dos dados replicados.

Além das funções básicas de uma criptomoeda, o sistema também incorpora o conceito de custódia de chaves, permitindo representar dois modelos distintos de uso. No primeiro modelo, o próprio usuário mantém sob sua responsabilidade suas chaves privadas, de forma semelhante ao uso de carteiras frias ou carteiras de software. No segundo modelo, a custódia das chaves pode ser delegada a uma entidade intermediária, representando o comportamento de uma corretora ou exchange. Essa funcionalidade amplia o valor conceitual do projeto ao introduzir uma distinção importante do ecossistema real de criptoativos.

Realizado como projeto para a disciplina ACH2147 - Desenvolvimento de Sistemas de Informação Distribuídos-, orientado pelo Prof. Renan Alves.

## Especificações do sistema

### 1. Arquitetura

A arquitetura foi estruturada seguindo dois níveis diferentes:

- Arquitetura externa: a rede distribuída dentre os nós é do tipo peer-to-peer estruturada, mas de forma simplificada e controlada.
- Arquitetura interna: em cada nó da rede, é construida um arquitetura em camadas, permitindo uma melhor separação de responsabilidades, maior clareza de implementação e mais facilidade de testes.

### 2. Comunicação

A comunicação do sistema é composta de dois modelos: RPC e Pub/Sub.

- RPC é utilizado na comunicação do cliente com seu nó de entrada, e também internamente entre nós para operações síncronas como sincronização de ledger e peer discovery.
- Pub/Sub é utilizado na propagação assíncrona de transações e blocos entre os nós da rede, onde cada nó atualiza seu estado local ao receber uma mensagem.

O protocolo de transporte adotado é o TCP, garantindo entrega confiável e ordenada das mensagens.

### 3. Nomeação e Processos

A definir.

### 4. Coordenação

Em questão de coordenação, foram tomadas as seguintes considerações:

- Sincronização é essencial no sistema, dado que os nós devem manter o estado local em concordância entre si. Para alcançar esta propriedade, foi utilizado no sistema um mecanismo de coordenação centralizada, em que um nó central define a ordem global dos eventos.
- No momento, o sistema foi projetado para que o líder seja fixo.
- A implementação do Pub/Sub no sistema é realizada por mensagens HTTP diretas entre os nós. 

## Autores

Diogo Leonel dos Santos	

Eric Isin Wang Chou

Jéssica Miranda Carvalho

Jonatan Zhan
