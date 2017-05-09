#!/usr/bin/env python
# coding: utf-8

from qqbot import QQBotSlot as qqbotslot, RunBot
import time

CONSTANT_LOGFILE = open('./log.txt', 'a')


@qqbotslot
def onQQMessage(bot, contact, member, content):
    global CONSTANT_LOGFILE
    if '@信息记录员' in content:
        bot.SendTo(contact, '大家好，我是智能聊天机器人小小白，由于我刚出生大脑还没发育完全，请大家先不要打扰我/调皮')

    info = ''
    if contact.ctype == 'buddy':
        info = contact.ctype + '`|`' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '`|`' + contact.qq + '`|`' + contact.mark + '`|`' + content
    elif contact.ctype == 'discuss':
        info = contact.ctype + '`|`' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '`|``|`' + contact.name + '`|``|`' + member.name + '`|`' + content
    else:
        info = contact.ctype + '`|`' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '`|`' + contact.qq + '`|`' + contact.name + '`|`' + member.qq + '`|`' + member.name + '`|`' + content

    CONSTANT_LOGFILE.write(info + '\n')
    CONSTANT_LOGFILE.flush()

RunBot()
