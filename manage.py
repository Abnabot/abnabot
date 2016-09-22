# -*- coding: utf-8 -*-
TOKEN = '113955046:AAHuX-rGMzW5MB4_MNTal_MvWx4PXcS3j4k'
 
bot = telebot.TeleBot(TOKEN)
 
def listener(messages):
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text': 
            if cid > 0:
                mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text
            else:
                mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text 
            f = open('log.txt', 'a')
            f.write(mensaje + "\n")
            f.close()
            print (mensaje)
            
 
bot.set_update_listener(listener) 

#Funciones

@bot.message_handler(commands=['help']) 
def command_help(m): 
    cid = m.chat.id 
    bot.send_message( cid, 'Comandos disponibles (Ver. 0.2.0 - RANDOM COMMANDS UPDATE):  \n/help \n/moemoekyun \n/kyoani \n/lewd \n/noticeme \n/patriarcado \n/matriarcado \n/coin \n/anicrap \n/morisummer \n/vashapproves \n/teamonodera \n/yuruyuri \n/mugi') 

@bot.message_handler(commands=['moemoekyun']) 
def command_moemoekyun(m): 
    cid = m.chat.id 
    bot.send_document( cid, open('moemoekyun.mp4', 'rb'))
 
@bot.message_handler(commands=['lewd'])
def command_lewd(m):
    cid = m.chat.id
    number = random.randrange(1,10,1)
    if number == 1:
        bot.send_photo( cid, open( 'lewd/1.jpg', 'rb'))
    elif number == 2:
         bot.send_photo( cid, open( 'lewd/2.png', 'rb'))
    elif number == 3:
         bot.send_photo( cid, open( 'lewd/3.jpg', 'rb'))
    elif number == 4:
         bot.send_photo( cid, open( 'lewd/4.jpg', 'rb'))
    elif number == 5:
         bot.send_photo( cid, open( 'lewd/5.jpg', 'rb'))
    elif number == 6:
         bot.send_photo( cid, open( 'lewd/6.jpg', 'rb'))
    elif number == 7:
         bot.send_photo( cid, open( 'lewd/7.jpg', 'rb'))
    elif number == 8:
         bot.send_photo( cid, open( 'lewd/8.jpg', 'rb'))
    elif number == 9:
         bot.send_photo( cid, open( 'lewd/9.jpg', 'rb'))
    elif number == 10:
         bot.send_photo( cid, open( 'lewd/10.jpg', 'rb'))

@bot.message_handler(commands=['kyoani']) 
def command_kyoani(m): 
    cid = m.chat.id 
    bot.send_message( cid, 'KyoAni power up!') 
    bot.send_photo( cid, open( 'kyoani.jpg', 'rb'))
    
@bot.message_handler(commands=['patriarcado'])
def command_patriarcado(m):
    cid = m.chat.id
    bot.send_document( cid, open('patriarcado.mp4', 'rb'))
    
@bot.message_handler(commands=['matriarcado'])
def command_matriarcado(m):
    cid = m.chat.id
    bot.send_document( cid, open('matriarcado.mp4', 'rb'))
    
@bot.message_handler(commands=['anicrap'])
def command_anicrap(m):
    cid = m.chat.id
    bot.send_message(cid, ('This is for you, otakus', 'rb'))
    bot.send_document( cid, open('animation.mp4', 'rb'))
    
@bot.message_handler(commands=['morisummer'])
def command_morisummer(m):
    cid = m.chat.id
    bot.send_document( cid, open('morisummer.mp4', 'rb'))
    
@bot.message_handler(commands=['yuruyuri'])
def command_yuruyuri(m):
    cid = m.chat.id
    bot.send_document( cid, open('yuruyuri.mp4', 'rb'))
    
@bot.message_handler(commands=['teamonodera'])
def command_teamonodera(m):
    cid = m.chat.id
    bot.send_document( cid, open('teamonodera.mp4', 'rb'))
    
@bot.message_handler(commands=['kokakoladhamistad'])
def command_kokakola(m):
    cid = m.chat.id
    bot.send_document( cid, open('kokakola.mp4', 'rb'))
    
@bot.message_handler(commands=['mugi'])
def command_mugi(m):
    cid = m.chat.id
    number = random.randrange(1,4,1)
    if number == 1:
        bot.send_document( cid, open( 'Mugi.mp4', 'rb'))
    elif number == 2:
         bot.send_document( cid, open( 'Mugi2.mp4', 'rb'))
    elif number == 3:
         bot.send_document( cid, open( 'Mugi3.mp4', 'rb'))
    elif number == 4:
         bot.send_document( cid, open( 'Mugi4.mp4', 'rb'))
    
@bot.message_handler(commands=['vashapproves'])
def command_vashapproves(m):
    cid = m.chat.id
    bot.send_document( cid, open('vashapproves.mp4', 'rb'))
    

@bot.message_handler(commands=['noticeme']) 
def command_noticeme(m):
    cid = m.chat.id
    user = str(m.chat.first_name)
    user_group = str(m.from_user.first_name)
    if cid > 0:
        bot.send_message(cid, 'I have noticed you, ' + user)
    else:
        bot.send_message(cid, 'I have noticed you, ' + user_group)
        
        
@bot.message_handler(commands=['coin'])
def command_coin(m):
    cid = m.chat.id
    number = random.randrange(1,3,1)
    if number == 1:
        bot.send_message(cid, ('Cara!', 'rb'))
    elif number == 2:
        bot.send_message(cid, ('Cruz!', 'rb'))
    
#############################################
 
bot.polling(none_stop=True)
