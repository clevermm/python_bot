#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json, os
from time import sleep
import sys
import re
import urllib
import methods as bot
reload(sys)
sys.setdefaultencoding("utf-8")
"""
handler message              _____'_____
start & copy right Clever
                           |______'______|
"""
def run ():
    last_update = 0
    while True:
        get_updates = bot.getUpdates()
        for update in get_updates['result']:
            if last_update < update['update_id']:
                last_update = update['update_id']
                if 'message' in update or 'text' in update:
                    try:
                        chat_id = update['message']['chat']['id']
                        text = update['message']['text']
                        message = update['message']
                        command = text
                        if(command == '/start' or command == '/help'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'typing')
                            key = json.dumps(
                            {'inline_keyboard':[[
                            {'text':'Developer 👓','url':'https://telegram.me/cleverm'},
                            {'text':'VainGlory 🔌','url':'https://telegram.me/vainglory_ir'}
                            ],
                            [
                            {'text':'Your Info 🕶','url':'https://telegram.me/clever_test_bot?start=info'}
                            ],
                            [
                            {'text':'Clever team Inline','switch_inline_query':'Clever'}
                            ]
                            ]
                            })
                            bot.send_msg(chat_id,'<b>Clever Team Development</b>\ncommands : \n/time',reply_markup=key)
                        if(command == '/time'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'typing')
                            time = urllib.urlopen('http://api.gpmod.ir/time/').read()
                            data = json.loads(time)
                            en = data['ENtime']
                            msgg = '<b>Time Tehran :</b> {}'.format(en)
                            bot.send_msg(chat_id,msgg,reply_to_message_id=update['message']['message_id'])
                        if(command == '/about'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'upload_photo')
                            markup = json.dumps({
                            'inline_keyboard':[
                            [
                            {'text':'👇 Clever Team 👇','callback_data':'1'}
                            ],
                            [
                            {'text':'Developer 🕶','url':'https://telegram.me/Cleverm'},
                            {'text':'Channel','url':'https://telegram.me/Vainglory_fa'}
                            ]
                            ]
                            })
                            bot.send_photo(chat_id,open('sex.jpg'),caption='@VainGlory_fa',reply_markup=markup)
                        if(command == '/info' or command == '/start info'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'typing')
                            user_id = update['message']['from']['id']
                            username = update['message']['from']['username']
                            s = bot.getUserProfilePhotos(update['message']['from']['id'])
                            markup = json.dumps(
                            {
                            'inline_keyboard':[
                            [
                            {'text':'{}'.format(username),'url':'https://telegram.me/{}'.format(username)}
                            ]
                            ]
                            }
                            )
                            bot.send_photo_file_id(chat_id,photo=s['result']['photos'][0][2]['file_id'],caption='ID : {}\nUsername : @{}\n@VainGlory_ir'.format(user_id,username),reply_markup=markup)
                        if(command == '/type'):
                            if(update['message']['reply_to_message']['entities'][0]['type']):
                                msg = update['message']['reply_to_message']['entities'][0]['type']
                                bot.send_msg(chat_id,'<b>{}</b>'.format(msg))
                    except KeyError:
                        print 'error'
                if 'callback_query' in update:
                    bot.getUpdates(last_update+1)
                    data = update['callback_query']['data']
                    call_id = update['callback_query']['id']
                    message_idd = update['callback_query']['message']['message_id']
                    id_from = update['callback_query']['message']['chat']['id']
                    if(data == '1'):
                        bot.answerCallbackQuery(call_id,text='👇👇👇\nDeveloper: Clever\nTeam : Clever Team\ncommands :\n/time\n/help',show_alert=True)
                if 'inline_query' in update:
                    bot.getUpdates(last_update+1)
                    inline_query_idd = update['inline_query']['id']
                    inline_query_query = update['inline_query']['query']
                    jso = json.dumps([{'type':'photo','id':'1','photo_url':'http://uupload.ir/files/37fh_20160912_210408.jpg','thumb_url':'http://uupload.ir/files/37fh_20160912_210408.jpg','caption':'@VainGlory_ir'}])
                    bot.answerInlineQuery(inline_query_id=inline_query_idd,results=[jso],cache_time=1)

run()
