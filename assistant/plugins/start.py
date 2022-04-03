from assistant import Sammy as Stark
from telethon import events, Button

PM_START_TEXT = """
**Hi {}**
I am a bot who works for **[@TeamDeCoDe](t.me/TeamDeCode)** and can detect spammers in groups can protect groups from then

**Click the below button for getting help menu!**
"""

@Stark.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name),
 buttons=[
          [
            Button.inline("Commands", data="help"), 
            Button.url("Support", "https://t.me/DeCodeSupport")
          ]
         ]
     )
       return

    if event.is_group:
       await event.reply("**Hehe Am Alive Baby💔**")
       return
