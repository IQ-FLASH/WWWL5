import random

from WWWL5 import WWWL5
from WWWL5.core.managers import edit_or_reply
from WWWL5.helpers import get_user_from_event
from razan.strings.fun import *

from . import *


@WWWL5.ar_cmd(pattern="رفع قلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه قلبك 🖤 "
    )


@WWWL5.ar_cmd(pattern="رفع زوجي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعه زوجك روحوا خلفوا 😂",
    )


@WWWL5.ar_cmd(pattern="رفع ليفه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ طـول عـمـره لـيـفـه اثـبـت يـالـيـفـه 🔪😹 "
    )

@WWWL5.ar_cmd(pattern="رفع اهبل(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ طـول عـمـره اهـبـل اي الـجـديـد 🙊😹😹 "
    )


@WWWL5.ar_cmd(pattern="رفع حمار(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفـعـة حـمـار 🦓 "
    )


@WWWL5.ar_cmd(pattern="رفع زوجتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 676943:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃  تـم رفعها زوجتك روحو خلفو 😹🤤",
    )


@WWWL5.ar_cmd(pattern="رفع كلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203485:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعـه كلب خليه ينبح 😂🐶",
    )


@WWWL5.ar_cmd(pattern="كت(?: |$)(.*)")
async def mention(mention):
    reza = random.choice(kttwerz)
    await edit_or_reply(mention, f"**- {reza}**")


@WWWL5.ar_cmd(pattern="هينه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(hena)
    await edit_or_reply(mention, f"{sos} .")


@WWWL5.ar_cmd(pattern="نسبة الحب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ 101% ده مطوري كده عيب 🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ 101% ده مطوري كده عيب 🤌😹**")
    if user.id == 203485:
        return await edit_or_reply(mention, f"**❃ 101% ده مطوري كده عيب 🤌😹**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(kz)
    await edit_or_reply(
        mention, f"❃ نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {sos} 🖤"
    )


@WWWL5.ar_cmd(pattern="نسبة الانوثة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"- نسبة الانوثة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@WWWL5.ar_cmd(pattern="نسبة الجمال(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ 101% ده مطوري كده عيب 🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ 101% ده مطوري كده عيب 🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ 101% ده مطوري كده عيب 🤌😹**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"نـسـبـة الـجـمـال [{muh}](tg://user?id={user.id}) هـي {sos} 🫣🖤"
    )


@WWWL5.ar_cmd(pattern="نسبة الغباء(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ 0% ده مطوري كده عيب 🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ 0% ده مطوري كده عيب 🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ 0% ده مطوري كده عيب 🤌😹**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"نـسـبـة الـغـبـاء [{muh}](tg://user?id={user.id}) هـي {sos} 😂🖤"
    )


@WWWL5.ar_cmd(pattern="رفع تاج(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعـه تاج 👑🔥"
    )


@WWWL5.ar_cmd(pattern="رفع قرد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203445:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعـه قرد واعطائه موزة 🐒🍌",
    )


@WWWL5.ar_cmd(pattern="اوصف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(osfroz)
    await edit_or_reply(mention, f"{rzona}")


@WWWL5.ar_cmd(pattern="شغله(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ مبرمج السورس - بطل لعب 🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ مبرمج السورس - بطل لعب 🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ مبرمج السورس - بطل لعب 🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{muh}](tg://user?id={user.id}) شغله هو {rezw}"
    )


@WWWL5.ar_cmd(pattern="نسبة الرجولة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ 101% ده مطوري كده عيب 🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ 101% ده مطوري كده عيب 🤌😹**")
    if user.id == 203485:
        return await edit_or_reply(mention, f"**❃ 101% ده مطوري كده عيب 🤌😹**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(kz)
    await edit_or_reply(
        mention, f"- نسبة الرجولة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@WWWL5.ar_cmd(pattern="نسبة التناحه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"❃ نسبة التناحه -0% ده مطوري كده عيب 🤌😹")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"❃ نسبة التناحه -0% ده مطوري كده عيب 🤌😹")
    if user.id == 203485:
        return await edit_or_reply(mention, f"❃ نسبة التناحه -0% ده مطوري كده عيب 🤌😹")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(kz)
    await edit_or_reply(
        mention, f"- نسبة التناحه في دمه [{muh}](tg://user?id={user.id})هـي {sos} 🫣😹"
    )


@WWWL5.ar_cmd(pattern="رفع حيوان(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعـه حيوان 🐏"
    )


@WWWL5.ar_cmd(pattern="رفع قطه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعـه قطه 🐈"
    )


@WWWL5.ar_cmd(pattern="رفع ثعبان(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعـه ثعبان تث تث 🐍😂"
    )


@WWWL5.ar_cmd(pattern="رفع خنزير(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفـعـه خـنـزيـر يـلا مـن هـنـا بـسـرعـه عـشـان بـقـرف 🙊😹😹"
    )


@WWWL5.ar_cmd(pattern="زواج(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم الزواج منه 🌚💞"
    )


@WWWL5.ar_cmd(pattern="طلاق(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم طـلاقـك منه 😂😂"
    )


@WWWL5.ar_cmd(pattern="خلع(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم خـلـعـك مـنـه مـن قـبـل محـكـمـة [ܦ࠭ߺࡋߺוࡅࠦࡅࡅࡅߺ](t.me/FLS_44) 😂"
    )


@WWWL5.ar_cmd(pattern="رفع اخويا(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعه اخوك 🌚♥️"
    )


@WWWL5.ar_cmd(pattern="رفع اختي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفعها اختك 🌚♥️"
    )


@WWWL5.ar_cmd(pattern="رفع شلحف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفع هذا الكائن شلحف كبير 😹😹"
    )


@WWWL5.ar_cmd(pattern="رفع حكاك(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6456641797:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 5627420357:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**❃ اتلم وبطل لعب ده مطوري كده عيب🤌😹**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"❃ المستخدم [{tag}](tg://user?id={user.id}) \n❃ تـم رفع هذا الكائن حكاك كبير 😹"
    )


@WWWL5.ar_cmd(pattern="الفارات$")
async def _(event):
    zzevent = await edit_or_reply(event, "❃ عزيزي \n❃ انضم الي القناة وستجد جميع الفارات \n❃ [اضغط هنا للانضمام](t.me/FLS_46)   ➪➪➪")


@WWWL5.ar_cmd(pattern="البوب$")
async def _(event):
    zzevent = await edit_or_reply(event, "❃ عزيزي المستخدم\n❃ البوب هو مطوري للتواصل معه @P_O28\n❃ شڪرا لستخدامڪ سورس [ܦ࠭ߺࡋߺוࡅࠦࡅࡅࡅߺ](t.me/FLS_44) 💞🌚")


@WWWL5.ar_cmd(pattern="مازن$")
async def _(event):
    zzevent = await edit_or_reply(event, "❃ عزيزي المستخدم\n❃ مازن هو مطوري للتواصل معه @M_LR1\n❃ شڪراً لاستخدامڪ سورس [ܦ࠭ߺࡋߺוࡅࠦࡅࡅࡅߺ](t.me/FLS_44) ♥️")