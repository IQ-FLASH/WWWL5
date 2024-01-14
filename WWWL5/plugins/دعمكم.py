@WWWL5.on(events.NewMessage(outgoing=True,pattern='.تجميع دعمكم'))
async def StartCollect(event):
    global collect

    if collect == True:
        await event.reply('عملية الجمع جارية')
    else:
        collect, notice = True, await event.reply('سيتم بدء الجمع قريبا')
        await AddTaksDamKom(event, "@DamKombot")


collect = False
# STOP COLLECT
@WWWL5.on(events.NewMessage(outgoing=True,pattern='.ايقاف تجميع دعمكم'))
async def StopCollect(event):
    global collect

    if collect == False:
        await event.reply('عملية الجمع متوقفة')
    else:
        collect = False
        await event.reply('سيتم ايقاف الجمع قريبا')



# JOIN PUBLIC
async def JoinChannel(event, username):
    try:
        Join = await event.client(JoinChannelRequest(channel=username))
        return [True, Join]
    except errors.UserAlreadyParticipantError:
        return [True, Join]
    except errors.FloodWaitError as error:
        return [False, f'تم حظر هذا الحساب من الانضمام للقنوات لمدة : {error.seconds} ثانية']
    except errors.ChannelsTooMuchError:
        return [False, 'هذا الحساب وصل للحد الاقصى من القنوات التي يستطيع الانضمام لها']
    except errors.ChannelInvalidError:
        return [False, False]
    except errors.ChannelPrivateError:
        return [False, False]
    except errors.InviteRequestSentError:
        return [False, False]
    except Exception as error:
        return [False, f'حدث خطأ غير متوقع, اذا كان الحساب يجمع بشكل طبيعي تجاهل هذه الرسالة {error}']
    

# JOIN PRIVATE
async def JoinChannelPrivate(event, username):
    try:
        Join = await event.client(ImportChatInviteRequest(hash=username))
        return [True, Join]
    except errors.UserAlreadyParticipantError:
        return [True, Join]
    except errors.UsersTooMuchError:
        return [False, False]
    except errors.ChannelsTooMuchError:
        return [False, 'هذا الحساب وصل للحد الاقصى من القنوات التي يستطيع الانضمام لها']
    except errors.InviteHashEmptyError:
        return [False, False]
    except errors.InviteHashExpiredError:
        return [False, False]
    except errors.InviteHashInvalidError:
        return [False, False]
    except errors.InviteRequestSentError:
        return [False, False]
    except errors.FloodWaitError as error:
        return [False, f'تم حظر هذا الحساب من الانضمام للقنوات لمدة : {error.seconds} ثانية']
    except Exception as error:
        return [False, f'حدث خطأ غير متوقع, اذا كان الحساب يجمع بشكل طبيعي تجاهل هذه الرسالة {error}']


# Tasks to do
async def AddTaksDamKom(event, bot_username):
    global collect

    while collect != False:
        if collect == False:
                break
        try:
            # start conversation with WWWL5
            async with event.client.conversation(bot_username, timeout=20) as conv:
                try:
                    # make sure the WWWL5 working
                    while True:
                        start_msg1 = await conv.send_message("/start")
                        resp = await conv.get_response()
                        
                        # check for must join
                        if "يجب عليك الاشتراك" in resp.message:
                            matches = re.findall(r'@(\w+)', resp.message)
                            if matches:
                                channel_url = matches[0]
                                if "+" in channel_url:
                                    result = await JoinChannelPrivate(event, channel_url)
                                else:
                                    result = await JoinChannel(event, channel_url)
                            else:
                                break
                        else:
                            break
                except Exception as error:
                    print ("ERROR (1) :", error)
                    if str(error).startswith('A wait of'):
                        banned_for = ((str(error).split("A wait of")[1]).split("seconds")[0]).strip()
                        await event.reply(f"**محظور من ارسال الرسائل للبوت لمدة : {banned_for}\n\nسيتم ايقاف الجمع لهذه المدة و البدأ من جميع**")
                        try:
                            sleep_seconds = int(banned_for.strip())
                        except:
                            sleep_seconds = 120
                        await asyncio.sleep(sleep_seconds)
                    elif str(error).startswith("cannot access local variable 'resp'"):
                        await event.reply(f'يبدو أن البوت لا يستجيب.. قد يكون محظور أو متوقف حاليا, سيتم ايقاف الجمع راجع البوت يدويا')
                        collect = False
                        break

                try:
                    # go to collect page
                    start_msg1 = await conv.send_message("/start")
                    resp = await conv.get_response()
                    click_collect = await resp.click(1)
                    resp2 = await conv.get_edit()
                    start_collect = await resp2.click(0)
                except Exception as error:
                    print ("ERROR (2) :", error)
                    if str(error).startswith("cannot access local variable 'resp'"):
                        await event.reply(f'يبدو أن البوت لا يستجيب.. قد يكون محظور أو متوقف حاليا, سيتم ايقاف الجمع راجع البوت يدويا')
                        collect = False
                        break

                channel_details = await conv.get_edit()

                # collect now
                for x in range(10):
                    if collect == False:
                        break

                    channel_details = channel_details
                    while True:
                        if collect == False:
                            break

                        matches = re.findall(r'@(\w+)', channel_details.message)
                        if matches:
                            channel_url = matches[0]
                            if "+" in channel_url:
                                result = await JoinChannelPrivate(event, channel_url)
                            else:
                                result = await JoinChannel(event, channel_url)

                            # check next move
                            if result[0] == False:
                                if result[1] == False:
                                    await channel_details.click(1)
                                else:
                                    await event.reply(f"**{result[1]}**")
                                    if str(result[1]).startswith('تم حظر هذا الحساب من الانضمام للقنوات لمدة :'):
                                        seconds = str(result[1]).replace('تم حظر هذا الحساب من الانضمام للقنوات لمدة :', '').replace('ثانية', '')
                                        await event.reply(result[1])
                                        try:
                                            sleep_seconds = int(seconds.strip())
                                        except:
                                            sleep_seconds = 500
                                        await asyncio.sleep(sleep_seconds)
                            else:
                                # check inside WWWL5
                                cc = await channel_details.click(0)
                                channel_details = await conv.get_edit()
                        else:
                            pass
                        await asyncio.sleep(3.2)

        except Exception as error:
            if str(error) == " ":
                await event.reply(f"**البوت لا يستجيب بسرعه. حاول مراجعته يدويا.. الجمع سيستمر**")
            elif str(error).startswith('Nobody is using this username'):
                await event.reply('يبدو أن هذا البوت محظور, تم ايقاف الجمع')
                collect = False
                break
            elif str(error).startswith("cannot access local variable 'resp'"):
                await event.reply(f'يبدو أن البوت لا يستجيب.. قد يكون محظور أو متوقف حاليا, سيتم ايقاف الجمع راجع البوت يدويا')
                collect = False
                break
            elif str(error) == "Cannot send requests while":
                await event.reply(f"**هذا الرقم غير متصل, الحل.. قم بحذفه و اضافته مرة اخرى بعدها سيبدأ بالجمع عندما يصل دوره**")
                break
            elif str(error).startswith("Cannot open exclusive conversation "):
                pass
            
            print ("conversation (error) :", error)
            await asyncio.sleep(1)