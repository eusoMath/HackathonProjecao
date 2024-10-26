
# NinjaMatic

NinjaMatic é um jogo interativo que desafia o jogador a resolver problemas de matemática para ajudar o personagem ninja a avançar. Com um visual retrô e elementos animados, o jogador tem um minuto para responder corretamente e garantir que o ninja não caia de sua plataforma.

## Estrutura do Projeto

O projeto possui os seguintes arquivos:

- index.html: Página inicial do jogo, com opções para iniciar o jogo ou acessar o tutorial.
- jogo.html: Tela onde o jogo será exibido e as interações ocorrerão.
- tutorial.html: Página com instruções e regras detalhadas do jogo.
- style.css: Folha de estilos que define a aparência do jogo e das animações.

## Funcionalidades

- *Página Inicial*: Contém um título animado e dois botões: um para iniciar o jogo e outro para visualizar o tutorial.
- *Tutorial*: Explica as regras do jogo e oferece uma descrição detalhada de como o jogo funciona.
- *Tela do Jogo*: Onde o jogo será implementado.

## Regras do Jogo

1. *Início do Jogo*: O ninja começa no topo de uma casa.
2. *Perguntas*: São apresentadas perguntas de matemática.
3. *Escolha da Resposta*: O jogador tem 1 minuto para escolher a resposta correta entre três alternativas.
4. *Acerto*: Ao responder corretamente, o ninja avança para a próxima casa.
5. *Erro*: A resposta certa será destacada em verde, e o tempo continuará contando.
6. *Tempo Esgotado*: Caso o tempo termine, o ninja cairá da plataforma.

## Tecnologias Utilizadas

- *HTML5*: Estrutura das páginas.
- *CSS3*: Estilo visual do jogo, com animações e efeitos para botões e texto.
- *JavaScript*: (Planejado para ser adicionado) Manipulação de lógica e interação no jogo.

## Estrutura de Arquivos

```plaintext
NinjaMatic/
│
├── index.html        # Página inicial com título e links para iniciar ou ver o tutorial
├── jogo.html         # Tela principal do jogo
├── tutorial.html     # Página com o tutorial e as regras do jogo
├── style.css         # Arquivo de estilos para a aparência e animações
└── img/              # Pasta para imagens utilizadas no jogo
    ├── casa.jpg
    └── ninja-inicio.png

Como Executar o Projeto
Clone o repositório ou baixe o projeto.
Abra o arquivo index.html em um navegador para acessar a página inicial.
Clique em "Comece a jogar" para acessar a tela do jogo ou em "Tutorial" para ver as instruções.
Planejamentos Futuros
Implementação do Jogo: A lógica do jogo será desenvolvida para interagir com o jogador, usando JavaScript.
Animações e Interatividade: Adicionar efeitos de movimento para o personagem e temporizador para as respostas.
Desenvolvido com ❤️ por NinjaMatic Team.
