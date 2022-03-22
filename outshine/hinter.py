import time  
import asyncio
# import nest_asyncio
# nest_asyncio.apply()
import discord
from discord.ext import commands
import random

class MyHinter(discord.Client):

    # def __init__(self, name):
    #     self.name = name
    #     print(f"{name} has started")
    #     super().__init__()

    async def on_ready(self):
        print("outSHINE module active. Designation:", "Hinter")
           
    async def on_message(self, message):
        if message.author.id == 716390085896962058: # If Poketwo...
            await message.channel.send("P2 detected")
            if message.embeds and message.embeds[0].title: # If message is an embed and has a title...
                if "pokémon has appeared!" in message.embeds[0].title: # If message is a spawn message...
                    asyncio.sleep(0.2)
                    await message.channel.send("p!hint")
                else:
                    return

async def run_hinter(name):
    print(random.randint(0, 100))
    hinterClient = MyHinter()
    hinterClient.run(name)

    

async def main():
    await asyncio.gather(
        run_hinter("OTU0Mjk2NTM0MTE0MTI3OTIy.YjRELg.ynxl7xuT3EDJ3gD6mTjzIs-yyTw"),
        run_hinter("ODYwNTU3OTc0MTE1MzE5ODc4.YN8_Vg.y9Bj3_J-8oJ3l7DrKitLUgvWff4")
    )

asyncio.run(main())





    



