#Definindo os imports
import twitch
import keypresser
import keyholder
t = twitch.Twitch();
k = keypresser.Keypresser();

#Coloque o seu username e oauth-key da Twitch abaixo.
#Sua oauth-key pode ser gerada atraves desse link: http://twitchapps.com/tmi/
username = "diogoaraujo";
key = "oauth:";
t.twitch_connect(username, key);
 
#O loop principal
while True:
    #Verificando novas mensagens
    new_messages = t.twitch_recieve_messages();
 
    if not new_messages:
        #Nenhuma mensagem nova
        continue
    else:
        for message in new_messages:
            #Extraindo informacoes da mensagem
            msg = message['message'].lower()
            username = message['username'].lower()
            print(username + ": " + msg.encode('utf-8'));

            #Aqui voce pode modificar as "keys" que podem ser digitadas e interpretadas
            #O codigo abaixo vai simular o comando da "key" 'q' se "q" for digitado no chat por alguem
            #O mesmo para todas as outras letras definidas aqui
            #Modifique aqui para os comandos que mais se adequam ao seu jogo
            if msg == "w": keyholder.holdForSeconds(msg, 0.3);
            if msg == "s": keyholder.holdForSeconds(msg, 0.3);
            if msg == "a": keyholder.holdForSeconds(msg, 0.1);
            if msg == "d": keyholder.holdForSeconds(msg, 0.1);
            if msg == "e": keyholder.holdForSeconds(msg, 0.5);
            if msg == "q": keyholder.holdForSeconds(msg, 0.1);
            if msg == "t": keyholder.holdForSeconds(msg, 0.5);