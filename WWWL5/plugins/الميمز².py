#الملف بحقوق سورس سبايدر @FLS_44 بواسطة @WWWL5
import asyncio
import os
from secrets import choice
import random
from urllib.parse import quote_plus
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterVoice

from WWWL5 import WWWL5

from WWWL5.core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, mention
from ..helpers import get_user_from_event
from ..helpers.utils import _format

from . import reply_id


@WWWL5.on(admin_cmd(outgoing=True, pattern="ياساتر يارب$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/133"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="ياختااي$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/134"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="لا تقتل المتعه ي مسلم$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/135"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="خخ اماال$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/136"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="تاخد نفس عميق$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/137"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="بيكدب$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/138"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="عيب يجدعان$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/139"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سبحانه$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/140"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="خلصانه$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/141"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="ضحك$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/142"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="صحيت من النوم$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/143"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="شفيق يا راجل$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/144"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="الحقونا$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/145"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="عاوزين نعملك بني ادم$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/146"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="انا رحت العياط$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/147"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="اتكلم بادب يولد$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/148"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="اماااال$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/149"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="فلوسي فين$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/150"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="في رمضان$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/151"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="لو معايا خنجرين$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/152"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="بطنااي$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/153"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مش عارف اقوم$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/154*"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="دا احنا هنضحك ضوحك$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/155"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="مينفعش$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/156"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="نعم انهاء المخدرات$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/157"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="دمك خفيف اوي$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/158"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="ليه كده يلا$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/159"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="يا حوستي السوده$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/160"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="احترمي نفسك يوليه$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/161"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="اخلاقك العاليه دي$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/162"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="احنا جامدين اوي$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/163"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="انا اتهزأت يا اخوانا$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/164"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="انا بيه ابن بيه$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/165"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="انا رمضان جانا يعم$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/166"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="انا عملت ايه$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/167"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="انا في دوامه$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/168"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="انت اي حكايتك$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/169"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="انت مين يلا$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/170"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="ايه يسطا$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/171"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="خبر اي ي مرا$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/172"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="الحاج ابراهيم$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/173"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="اي الهبل دا$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/174"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="ايه ده$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/175"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="يا لاهوي$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/176"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="انا تعبان ي حامد$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/177"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="ياحلو يا جميل$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/178"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="يالهوي$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/179"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="دي عيلة زبالة ياراجل$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/180"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="ربنا نصرني$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/181"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="متحلوش$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/182"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="يا بنت الوسخه$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/183"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="ما تجرب يا اخي$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/184"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="اجمد كده$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/185"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="انت مقتنع$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/186"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="بطني بتتحرق$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/187"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="ضحكك$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/188"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="يا تافهه$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/189"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="عيب عيب$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/190"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="انا انطلقت في البطيخ$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/199"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="هتتحرقو في نار جهنم$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/192"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="فاشل فاشل$"))
async def jepvois(Voice):
  url = f"https://t.me/Memes264/193"
  await Voice.client.send_file(Voice.chat_id,url,caption="    . ᯏ𝖲᥆υᖇᥴᥱ - 𝖥𝗅ᥲ᥉𝗁 ᭡ .\n✦┅━╍━╍╍━━╍━━╍━┅✦\n قناة سورس فلاش @FLS_44",parse_mode="html")
  await Voice.delete()
