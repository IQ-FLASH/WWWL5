from telethon import Button, events

from WWWL5 import WWWL5 

from ..Config import Config

ROZ_PIC = "https://telegra.ph/file/738661f85fe3e4fd54d20.jpg"
RAZAN = Config.TG_BOT_USERNAME
ROZ_T = (
    f"**ܩߺ𐢋ߺ𐬛𐬠 ܚࡅߺ𐬛𐬠ܚࡅߺ ܦ࠭ߺࡋߺוࡅࠦࡅࡅࡅߺ **\n"
  
)

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("المطور") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("❥︎𝕾🅔🅛🅟🅞🅟𝕾", "https://t.me/P_O28"),
                    Button.url(". ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .", "https://t.me/FLS_44"),
                    
                ]
            ]
            
            if ROZ_PIC and ROZ_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ROZ_PIC, text=ROZ_T, buttons=buttons, link_preview=False
                )
            elif ROZ_PIC:
                result = builder.document(
                    ROZ_PIC,
                    title="JMTHON - WWWL5",
                    text=ROZ_T,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="JMTHON - WWWL5",
                    text=ROZ_T,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@WWWL5.ar_cmd(pattern="المطور")
async def repo(event):
    RR7PP = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(RR7PP, "المطور")
    await response[0].click(event.chat_id)
    await event.delete()


# edit by ~ @WWWL5
