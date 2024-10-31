Asteroids Game

Um jogo simples de nave espacial inspirado no clássico "Asteroids". Desenvolvido com Python e Pygame, este jogo permite que o jogador controle uma nave que dispara contra asteroides e acumula pontos ao evitar colisões.
Demonstração

Índice

    Instalação
    Como Jogar
    Estrutura do Código
    Funcionalidades
    Melhorias Futuras

Instalação

Para rodar o jogo em sua máquina, siga estes passos:

    Clone este repositório:

    bash

git clone https://github.com/seuusuario/AsteroidsGame.git

Instale as dependências: Este jogo foi desenvolvido com Python e Pygame. Para instalar o Pygame, execute:

bash

pip install pygame

Execute o jogo: Navegue até o diretório onde está o código e execute:

bash

    python asteroids.py

Como Jogar

    Movimento da Nave: Use as setas Esquerda e Direita para mover a nave.
    Atirar: Pressione a Barra de Espaço para disparar contra os asteroides.
    Objetivo: Evite colisões com os asteroides e destrua o maior número possível para aumentar sua pontuação.
    Fim de Jogo: O jogo termina quando você perder todas as vidas (5 vidas inicialmente).

Estrutura do Código

Este projeto está dividido em algumas classes principais:

    NaveEspacial: Gerencia o movimento da nave, disparo e verificação de colisões.
    Asteroide: Define os asteroides, que se movem em direção à parte inferior da tela e desaparecem ao atingir o final.
    Tiro: Representa os tiros disparados pela nave, movendo-se para cima e desaparecendo ao sair da tela ou colidir com asteroides.

O código também inclui funções de:

    Desenho de Pontuação e Vidas: Exibe a pontuação acumulada e os corações restantes no canto superior da tela.
    Verificação de Colisões: Reduz uma vida ao colidir com um asteroide e, caso as vidas acabem, remove todos os sprites e exibe a mensagem “GAME OVER”.

Funcionalidades

    Background Animado: O fundo se move para dar a impressão de movimento constante.
    Pontuação: A pontuação é atualizada automaticamente com a distância percorrida pela nave.
    Gerenciamento de Vidas: Cada colisão com um asteroide reduz as vidas em 1. Quando as vidas se esgotam, todos os sprites desaparecem, e apenas a mensagem “GAME OVER” é exibida.

Melhorias Futuras

    Melhorias Gráficas: Substituir a nave e os asteroides por imagens de alta qualidade.
    Aprimoramento do Jogo: Adicionar níveis de dificuldade e diferentes tipos de asteroides.
    Sons e Efeitos Visuais: Sons de disparo e explosão ao destruir asteroides e perder vidas.
    Modo de Pontuação Online: Salvar pontuações em um banco de dados online para um placar global.

Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

Divirta-se jogando!
