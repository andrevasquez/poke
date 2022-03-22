import discum
import time     
import random
import asyncio

async def create_spammer(tn, ch, delay, de):

    class MySpammer(discord.Client):
        async def on_ready(self):
            print("outSHINE module active. Designation:", de)

            await asyncio.sleep(1.7 * delay)

            while True:
                channel = bot.get_channel(ch)
                await channel.send(random.randint(10000000000000000000, 90000000000000000000))
                await asyncio.sleep(3.4)

    MySpammer().run(tn)

