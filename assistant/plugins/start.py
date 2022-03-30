from assistant import Sammy
from telethon import events, Button

PM_START_TEXT = """
**Hi {}**
I am a bot who works for @TeamDeCoDe and can detect spammers in groups can protect groups from then

**Click the below button for getting help menu!**
"""

@Sammy.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=[
        [Button.inline("Help & Commands", data="help")],
        [Button.url("CreDits", "https://t.me/DeCoDeDevs")]])
        

    
