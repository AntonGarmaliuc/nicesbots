#IMPORT
import discord
from discord.ext import commands
from discord.utils import get

#BOT 1
class NiceBot(discord.Client):
    async def on_ready(NiceBot):
        print('Бот активирован:', NiceBot.user)

#COMMAND 1

    async def on_message(NiceBot, text):
        if text.author == NiceBot.user:
            return

        if text.content == '!!id':
            await text.channel.send('`id: 126999366`')

        if text.content == '!!rules':
            await text.channel.send('`Правила:\n1.0 Спам = Мут на 2 часа!\n1.1 Реклама = Бан навсегда по ип!\n1.2 Маты = Мут на 1 час!\n1.3 Попытка обмана игрока/админа = Бан навсегда по ип!\n1.4 Попрошайничество = Бан 1 день!\n1.5 Кидать файлы/сылки/програмы игрокам в лс = Бан навсегда по ип!\n1.6 Бан/Кик/Мут без причины = Снятие!\n1.7 Выдали Бан/Кик/Мут без докозательств = Снятие!`')

        if text.content == '!!help':
            await text.channel.send('`Информация:\nСоздатель: NiceSkill#0852\nМой друг: By Morendi#9361\nКоманды:\n1)!!id #Мой айди\n2)!!rules #Правила\n3)!!admins #Права админов\n4)!!commands #Команды админов\n5)!!hello #Бот скажет тебе Привет\n6)!!play #Включить музыкального бота\n7)!!leave / !!skip #Отключить музыкального бота`')
   
        if text.content == '!!admins':
            await text.channel.send('`Права админов:\n@│Модератор│ \n1)/tempban #Временно банит пользователя на сервере\n2)/infractions #Показывает нарушения пользователя\n3)/kick #Выгоняет пользователся с сервера\n4)/tempmute #Временно заглушает пользователя на сервере\n5)/unban #Разбанивает пользователя на сервере\n6)/unmute #Снимает заглушение с пользователя\n7)Изменять сервер, добавлять ботов\n@│Хелпер│ \n1)/tempban #Временно банит пользователя на сервере\n2)/infractions #Показывает нарушения пользователя\n3)/kick #Выгоняет пользователся с сервера\n4)/tempmute #Временно заглушает пользователя на сервере\n5)/unban #Разбанивает пользователя на сервере\n6)/unmute #Снимает заглушение с пользователя\n@│Мл-Хелпер│ \n1)/kick #Выгоняет пользователся с сервера\n2)/tempmute #Временно заглушает пользователя на сервере\n3)/unmute #Снимает заглушение с пользователя`')

        if text.content == '!!commands':
            await text.channel.send('`Команды для админа:\n1)/tempban #Временно банит пользователя на сервере\n2)/infractions #Показывает нарушения пользователя\n3)/kick #Выгоняет пользователся с сервера\n4)/tempmute #Временно заглушает пользователя на сервере\n5)/unban #Разбанивает пользователя на сервере\n6)/unmute #Снимает заглушение с пользователя`')
   
        if text.content == '!!hello':
            author = text.author
            await text.channel.send( f' { author.mention } Привет!' )

#RUN BOT NiceBot
NiceBot = NiceBot()
NiceBot.run('OTQzNDgzMzgzMTUyMDAxMDc2.YgztXw.UBiki1Pc7RnHYqLrOhK4bvNOQWo')
