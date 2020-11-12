import discord
import time
prefix='!'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith(prefix+'semaine'):
            ActualTime=time.localtime()
            tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,tm_yday,tm_isdst=ActualTime
            if int((tm_yday+7)/7)%2==0:
                await message.channel.send('On est en semaine A'.format(message))
            else:
                await message.channel.send('On est en semaine B'.format(message))
                
                        
        if message.content.startswith(prefix+'prefix'):
            if len(message.content)==9:
                content_prefix=str(message.content)
                prefix=content_prefix[8]
                await message.channel.send('Prefix changé en '+prefix.format(message))
            else:
                await message.channel.send('pas de changement possible. merci d utiliser la commande '+prefix+'prefix et le caractere souhaité'.format(message))

client = MyClient()
client.run('Nzc2NDAwODY2MTk3NTA0MDIw.X60Vpw.Gyhg8P9mlXkE3Y6hB37bVSpwsv4')
