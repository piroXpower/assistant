from assistant import Sammy
from telethon import events, Button
from assistant.Conf import Config

RULES = Config.RULES

@Sammy.on(events.NewMessage(pattern="^[!?/]rules"))
async def rules(event):

    msg = await event.get_reply_message()
    if not msg and event.is_group:
        await event.delete()
        await event.respond("Please read the rules before chatting here!", buttons=[
        [Button.url("Chat Rules", "t.me/{}?start=rules".format(Config.BOT_USERNAME))
        ]])
        return
        
    re = (await event.get_reply_message()).id
    await event.delete()
    await Sammy.send_message(event.chat_id, "Please read the rules before chatting here!", buttons=[
    [Button.url("Chat Rules", "t.me/{}?start=rules".format(Config.BOT_USERNAME))
    ]], reply_to=re)
    return

    await event.reply(RULES)

@Sammy.on(events.NewMessage(pattern="^/start rules"))
async def rules(event):

    if event.is_group:
       await event.reply("Please read the rules before chatting here!", buttons=[
       [Button.url("Chat Rules", "t.me/{}?start=rules".format(Config.BOT_USERNAME))
       ]])
       return

    await event.reply(RULES)

@Sammy.on(events.callbackquery.CallbackQuery(data="rules"))
async def _(event):

    await event.edit(RULES, buttons=[
    [Button.inline("« Bᴀᴄᴋ", data="start")]
    ])
