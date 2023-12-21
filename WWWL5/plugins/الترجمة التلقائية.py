# ملف جمثون
import os

from telethon import events

from ..sql_helper.globals import addgvar, delgvar, gvarstatus

os.system("pip install googletrans")
from googletrans import Translator

from WWWL5 import WWWL5

translator = Translator()


@WWWL5.ar_cmd(pattern="تفعيل الترجمة")
async def traenjm(event):
    if gvarstatus("translateen"):
        await edit_delete(event, "❃ **الترجمة التلقائية مفعلة بالأصل ✅**")
        return
    if not gvarstatus("translateen"):
        addgvar("translateen", "Done")
        await edit_delete(
            event, "❃ **تم بنجاح تفعيل الترجمة التلقائية ✅**"
        )
        return


@WWWL5.ar_cmd(pattern="تعطيل الترجمة")
async def stoptraenjm(event):
    if not gvarstatus("translateen"):
        await edit_delete(event, "❃ **الترجمة التلقائية غير مفعلة بالأصل ❌**")
        return
    if gvarstatus("translateen"):
        delgvar("translateen")
        await edit_delete(event, "❃ **تم تعطيل الترجمة التلقائية ❌**")
        return


@WWWL5.on(events.NewMessage(outgoing=True))
async def translateen(event):
    if gvarstatus("translateen"):
        if event.message.message.startswith(("!", ".", "/", "http", "@")):
            return
        try:
            translation = translator.translate(
                event.message.message, src="ar", dest="en"
            )
            if translation.text != event.message.message:
                await WWWL5.edit_message(event.message, translation.text)
        except:
            pass
