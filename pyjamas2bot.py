#! /usr/bin/python3
# -*- coding: utf-8 -*-

# pyTelegramBotAPI
# https://github.com/eternnoir/pyTelegramBotAPI
# pip3 install pyTelegramBotAPI

import telebot
import feedparser
import time
import configparser

CONFIGFILE = ".pyjamas2botrc"

cfg = configparser.ConfigParser()
cfg.read(CONFIGFILE)

KEY = cfg.get("TELEGRAM", "PYJAMAS2BOT_KEY")


bot = telebot.TeleBot(KEY)

@bot.message_handler(commands=["oi"])
def funcao_oi(session):
    print(session)
    bot.reply_to(session, "oi querido")

@bot.message_handler(commands=["tchau"])
def funcao_oi(session):
    print(session)
    bot.reply_to(session, "tchau")

@bot.message_handler(commands=["cafe", "pipoca", "diego"])
def carinhosa(session):
    if session.text == "/cafe":
        gif = "https://media.giphy.com/media/3owvK3nt6hDUbcWiI0/giphy.gif"
    elif session.text == "/pipoca":
        gif = "https://media.giphy.com/media/MSapGH8s2hoNG/giphy.gif"
    else:
        # Agradecimentos ao Diego Neves
        gif = "https://media.giphy.com/media/QN451Wg12SilkyRU3l/giphy.gif"
    print(session.text)
    bot.send_document(session.chat.id, gif)
    print(dir(bot))

@bot.message_handler(func=lambda m: True)
def WhatEver(session):
    print("WhatEver:", session.text)
    if session.text == "oi":
        bot.reply_to(session, "oi querido")
    elif session.text == "talkei":
        bot.reply_to(session, "que horror!")

bot.send_message(64457589, "Restart: ", time.ctime(time.time()))

SITE = "https://linux-br.org/index.php?format=feed&type=rss"

d = feedparser.parse(SITE)
for rss in d['entries']:
    title = u"%s" % rss.title.encode("utf-8")
    link = u"%s" % rss.link.encode("utf-8")

    print(f"Novo post: {title} {link}")
    bot.send_message(64457589, u"%s %s" % (title, link))
bot.polling()
