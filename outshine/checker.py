import discum
import time
import random
import asyncio

channelsToCheck = [
  "876163316429492254", 
  "876164299863765043", 
  "876270267796684830", 
  "876270439314391050" 
]
talkedRecently = []

async def check(tn, de):
    bot = discum.Client(token=tn, log=False)

    @bot.gateway.command
    def create_checker(resp):
        if resp.event.ready_supplemental: # ready_supplemental is sent after ready
            user = bot.gateway.session.user
            print("outSHINE module online.", de)

        if resp.event.message: # On message...
            # Variables to help search for stuff
            msg = resp.parsed.auto()
            guildID = msg["guild_id"] if "guild_id" in msg else None # because DMs are technically channels too
            channelID = msg["channel_id"]
            userid = msg["author"]["id"]
            content = msg["content"]
            embed = msg["embeds"]

            if channelID in channelsToCheck:
                if userid == "716390085896962058":
                    if "Whoa there. Please tell us" in content:
                        actualCaptcha = content.split(" ")[7]
                        groupNum = "null"
                        if "880776005273387058" in actualCaptcha:
                            groupNum = "GROUP 1 CATCHER"
                        elif "881512816505401365" in actualCaptcha:
                            groupNum = "GROUP 1 HINTER"

                        if userid in talkedRecently:
                            return
                        else:
                            # DM SATIRE # user.send(getRandomInt(1, 100000) + " GROUP: " + groupNum + " CAPTCHA: " + actualCaptcha);
                            # Send email
                            # Add to talked recently
                            talkedRecently.append(userid)
                            # Removed from talkedRecently in 120s (use sleep)
                            time.sleep(120)
                            talkedRecently.remove(userid)


    bot.gateway.run(auto_reconnect=True)

