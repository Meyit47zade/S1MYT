#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import speedtest
from YukkiMusic.utils import close_key
from pyrogram import filters
from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**İndirme Testini Çalıştırma .**")
        test.download()
        m = m.edit("**Yükleme Testini Çalıştırma .**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**SpeedTest Paylaşma .**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("**Hız Testini Çalıştırma .**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**Speedtest Sonuçları**
    
<u>**Müşteri :**</u>
**Şirket :** {result['client']['isp']}
**Ülke :** {result['client']['country']}
  
<u>**Sunucu :**</u>
**İsim :** {result['server']['name']}
**Ülke :** {result['server']['country']}, {result['server']['cc']}
**Sponsor :** {result['server']['sponsor']} 
**Ping :** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output,
        reply_markup=close_key,
    )
    await m.delete()
