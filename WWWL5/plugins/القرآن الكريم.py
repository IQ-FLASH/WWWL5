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


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الفاتحة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/26"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الفاتحة\n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره البقرة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/27"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره البقرة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره آل عمران$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/28"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره آل عمران \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره النساء$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/29"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره النساء \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره المائدة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/30"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره المائدة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الأنعام$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/31"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الأنعام \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الأعراف$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/32"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الأعراف \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الأنفال$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/33"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الأنفال \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره التوبة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/34"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره التوبة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره يونس$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/35"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره يونس \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره هود$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/36"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره هود \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره يوسف$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/37"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره يوسف \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الرعد$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/38"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الرعد \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره إبراهيم$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/39"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره إبراهيم \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الحجر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/40"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الحجر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره النحل$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/41"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره النحل \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الإسراء$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/42"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الإسراء \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الكهف$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/43"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الكهف \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره مريم$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/44"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره مريم \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره طه$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/45"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره طه \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الأنبياء$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/46"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الأنبياء \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الحج$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/47"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الحج \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره المؤمنون$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/48"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره المؤمنون \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره النور$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/49"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره النور \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الفرقان$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/50"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الفرقان \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الشعراء$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/51"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الشعراء \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره النمل$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/52"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره النمل \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره القصص$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/53"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره القصص \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره العنكبوت$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/54"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره العنكبوت \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الروم$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/55"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الروم \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره لقمان$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/56"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره لقمان \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره السجدة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/57"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره السجدة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الأحزاب$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/58"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الأحزاب \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره سبأ$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/59"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره سبأ \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره فاطر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/60"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره فاطر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره يس$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/61"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره يس \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الصافات$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/62"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الصافات \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره ص$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/63"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره ص \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الزمر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/64"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الزمر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره غافر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/65"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره غافر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره فصلت$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/66"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره فصلت \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الشورى$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/67"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الشورى \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الزخرف$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/68"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الزخرف \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الدخان$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/69"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الدخان \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الجاثية$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/70"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الجاثية \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الأحقاف$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/71"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الأحقاف \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره محمد$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/72"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره محمد \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الفتح$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/73"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الفتح \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الحجرات$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/74"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الحجرات \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره ق$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/75"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره ق \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الذاريات$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/76"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الذاريات \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الطور$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/77"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الطور \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره النجم$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/78"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره النجم \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره القمر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/79"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره القمر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الرحمن$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/80"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الرحمن \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الواقعة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/81"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الواقعة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الحديد$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/82"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الحديد \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره المجادلة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/83"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره المجادلة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الحشر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/84"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الحشر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الممتحنة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/85"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الممتحنة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الصف$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/86"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الصف \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الجمعة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/87"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الجمعة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره المنافقون$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/88"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره المنافقون \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره التغابن$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/89"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره التغابن \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الطلاق$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/90"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الطلاق \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره التحريم$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/91"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره التحريم \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الملك$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/92"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الملك \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره القلم$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/93"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره القلم \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الحاقة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/94"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الحاقة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره المعارج$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/95"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره المعارج \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره نوح$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/96"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره نوح \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الجن$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/97"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الجن \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره المزمل$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/98"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره المزمل \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره المدثر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/99"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره المدثر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره القيامة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/100"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره القيامة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الإنسان$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/101"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الإنسان \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره المرسلات$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/102"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره المرسلات \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره النبأ$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/103"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره النبأ \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره النازعات$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/104"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره النازعات \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره عبس$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/105"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره عبس \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره التكوير$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/106"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره التكوير \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الإنفطار$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/107"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الإنفطار \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره المطففين$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/108"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره المطففين \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الإنشقاق$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/109"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الإنشقاق \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره البروج$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/110"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره البروج \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الطارق$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/111"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الطارق \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الأعلى$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/112"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الأعلى \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الغاشية$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/113"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الغاشية \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الفجر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/114"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الفجر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره البلد$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/115"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره البلد \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الشمس$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/116"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الشمس \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الليل$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/117"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الليل \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الضحى$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/118"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الضحى \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الشرح$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/119"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الشرح \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره التين$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/120"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره التين \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره العلق$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/121"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره العلق \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره القدر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/122"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره القدر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره البينة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/123"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره البينة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الزلزلة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/124"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الزلزلة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره العاديات$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/125"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره العاديات \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره القارعة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/126"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره القارعة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره التكاثر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/127"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره التكاثر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره العصر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/128"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره العصر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الهمزة$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/129"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الهمزة \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الفيل$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/130"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الفيل \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره قريش$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/131"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره قريش \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الماعون$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/132"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الماعون \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الكوثر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/133"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الكوثر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الكافرون$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/134"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الكافرون \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره النصر$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/135"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره النصر \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره المسد$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/136"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره المسد \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الإخلاص$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/137"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الإخلاص \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الفلق$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/138"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الفلق \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الناس$"))
async def jepvois(Voice):
  url = f"https://t.me/EE_SPID/139"
  await Voice.client.send_file(Voice.chat_id,url,caption="❃︙ سوره الناس \n❃︙ بصوت القارئ ماهر المعيقلي\n❃︙ BY : @FLS_44 🌺",parse_mode="html")
  await Voice.delete()
