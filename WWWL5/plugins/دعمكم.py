#اشهد أن لا إله إلا الله واشهد أن محمدًا عبده ورسوله 
from WWWL5 import WWWL5
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
import asyncio
from telethon import events
c = requests.session()
bot_username = '@MARKTEBOT'
tepthon = ['yes']


@WWWL5.on(admin_cmd(pattern="تجميع دعمكم"))
async def _(event):
    await event.edit("**᯽︙سيتم تجميع النقاط من بوت دعمكم , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await WWWL5.get_entity(bot_username6)
    await WWWL5.send_message('@DamKombot', '/start')
    await asyncio.sleep(4)
    msg0 = await WWWL5.get_messages(bot_username6, limit=1)
    await msg0[0].click(1)
    await asyncio.sleep(4)
    msg1 = await WWWL5.get_messages(bot_username6, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await WWWL5(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات حالياً 🤍') != -1:
            await WWWL5.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        msg_text = msgs.message  # الكود تمت كتابتهُ من قبل سورس الجوكر 
        if "اشترك فالقناة @" in msg_text:
            aljoker_channel = msg_text.split('@')[1].split()[0]
            try:
                entity = await WWWL5.get_entity(aljoker_channel)
                if entity:
                    await WWWL5(JoinChannelRequest(entity.id))
                    await asyncio.sleep(4)
                    msg2 = await WWWL5.get_messages(bot_username6, limit=1)
                    await msg2[0].click(text='اشتركت ✅')
                    chs += 1
                    await event.edit(f"تم الانظمام الى القناة رقم {chs}")
            except:
                await WWWL5.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break

    await WWWL5.send_message(event.chat_id, "تم الانتهاء من التجميع")