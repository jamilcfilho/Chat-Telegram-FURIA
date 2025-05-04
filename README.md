# Desafio 1: Experiência Conversacional

O objetivo deste projeto é de desenvolver um caso de uso conversacional relacionado à FURIA.

O projeto consiste na criação de um chat para os fâs do time de CS da Furia. O chat fornece informações relevantes para que os fãs possam acompanhar e interagir com o time dando até sugestões.

O chat foi desenvolvido utilizando a linguagem de programação Python e o aplicativo de mensagens Telegram, escolhidos por contas das bibliotecas e frameworks que o Python oferece, além da popularidade e facilidade de uso do Telegram como plataforma de comunicação.


## Funcionalidade

O Chat possui as seguintes funcionalidades:

- Exibição de um termo de uso no início, que o usuário deve aceitar para continuar.
- Após a aceitação, o chat solicita o nome do usuário e pede confirmação antes de seguir.
- O menu principal oferece opções para os fãs acessarem as informações e interagirem com o time, incluindo:
    - Canal de notícias
    - Acompanhar Jogos ao Vivo
    - Calendário de Jogos
    - Discussões sobre Jogos
    - Eventos e Encontros
    - Espaço para Novos Fãs
    - Loja FURIA

### Tecnologias Utilizadas

* [Python](https://www.python.org/): Linguagem principal utilizada para o desenvolvimento.
* [Telegram](https://telegram.org/): Plataforma de mensagens escolhida para interação com os usuários.
* [Visual Studio Code](https://code.visualstudio.com/): Ambiente de desenvolvimento utilizado.


## Dependências e Versões Necessárias

As dependências estão listadas no arquivo "requirements.txt", que facilita a instalação das bibliotecas necessárias, assim conseguindo executar o projeto com êxito.

Segue abaixo uma lista com as principais dependências do projeto:

* Python - Versão: 3.12.2
* python-telegram-bot - Versão: 20.8

## 📌 Processo de desenvolvimento 📌

O desenvolvimento do projeto começou com a elaboração de um passo a passo no bloco de notas do Windows. Isso ajudou a visualizar como o projeto seria estruturado e quais seriam os próximos passos. Esse planejamento inicial foi fundamental para garantir que o código fosse organizado e fácil de entender.

## ⏭️ Criação do Bot no Telegram

Para a preparação do projeto, criei o chatbot no Telegram seguindo estas etapas:
1. Acesse o Telegram (desktop ou web) e no canto superior esquerdo no campo de busca, busque por "BotFather".
2. Inicie uma conversa com o BotFather e utilize o comando "/newbot" para criar um novo bot.
3. Siga as instruções forncedias pelo BotFather, como nomear o bot e escolher um username.
4. Após a criação, o BotFather fornecerá um token. Este token deve ser mantido em segurança, pois será utilizado para acessar a API do Telegram.


Importante: O código contém a frase "USAR TOKEN AQUI", que deve ser substituída pelo Token fornecido pelo BotFather.


## ⏭️ Implementação do Chat

A partir do planejamento, comecei a implementação do chat utilizando Python e a API do Telegram via Token.
A principal interação no chat são feitas utilizando botões interativos, que tornam a experiência do usuário mais dinâmica.

O fluxo do chat funciona da seguinte maneira:
1. O usuário inicia o chat com o comando: "/start";
2. Chat exibe um "termo de uso" que o usuário deve aceitar ou recusar.Caso o usuáio aceite, o chat continua; se recusar, o chat é encerrado;
3. Após a aceitação, o chat solicita o "nome do usuário", que será confirmado. Se o nome estiver correto, o usuário segue para o menu principal; caso contrário, o chat solicita a correção do nome;
4. O menu principal contém as seguintes opções:
    - Canal de notícias = Sinaliza para o usuário o link do "Portal de notícias da FURIA", quais são os jogadores atuais dos times da FURIA CS sendo o time internacional e o time feminino e ainda mostra os resultados dos últimos jogos. 

    - Acompanhar Jogos o Vivo = O chat envia atualizações em tempo real de acontecimentos importantes da partida para que o usuário fique por dentro da partida mesmo sem estar assistindo.

    - Calendário de Jogos = Mostra quais são as próximas partidas que o time da FURIA CS irá enfrentar.

    - Discussões de Jogos = Onde o usuário tem a possibilidade de enviar sugestão de discussão sobre o time e até táticas possíveis de serem utilizadas pelo time da FURIA CS.

    - Eventos e Encontros = Sinaliza ao usuário como ele pode ficar mais próximo do time da FURIA CS através de eventos que o time participa, sendo Watch Party, bate papo após as partidas, etc.

    - Espaço para novos fãs = É onde o chat envia uma mensagem que contém as principais redes sociais da FURIA para que o novo usuário conheça melhor sobre a história da FURIA.

    - Loja da FURIA = Chat envia uma mensagem com o link da loja oficial da FURIA para que o usuário adquira os produtos exclusivos da marca FURIA.

Após a seleção de qualquer uma dessas opções, o chat oferece possibilidade de "Voltar ao menu principal" para continuar a interação do usuário com o chat.

## Observações
- Durante os testes, substituia o texto "USAR TOKEN AQUI" pelo token adquirido pelo BotFather.
- O código é modular, organizado e com funções, facilitando futuras melhorias e manutenções.