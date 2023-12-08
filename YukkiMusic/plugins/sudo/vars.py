#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio

from pyrogram import filters

import config
from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database.memorydatabase import get_video_limit
from YukkiMusic.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "**~ Lütfen bekleyin .**"
    )
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = f"[Repo]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "Evet"
    else:
        ass = "Hayır"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "Evet"
    else:
        pvt = "Hayır"
    if config.AUTO_SUGGESTION_MODE == str(True):
        a_sug = "Evet"
    else:
        a_sug = "Hayır"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "Evet"
    else:
        down = "Hayır"

    if not config.GITHUB_REPO:
        git = "Hayır"
    else:
        git = f"[REPO]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "Hayır"
    else:
        start = f"[RESİM]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "Hayır"
    else:
        s_c = f"[KANAL]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "Hayır"
    else:
        s_g = f"[GRUP]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "Hayır"
    else:
        token = "Evet"
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        sotify = "Hayır"
    else:
        sotify = "Hayır"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**MÜZİK BOT AYARLARI:**

**<u>Temel Değişken:</u>**
`MUSIC_BOT_NAME` : **{bot_name}**
`DURATION_LIMIT` : **{play_duration} dk**
`SONG_DOWNLOAD_DURATION_LIMIT` :** {song} dk**
`OWNER_ID` : **{owner_id}**
    
**<u>Özel Repo Değişkeni:</u>**
`UPSTREAM_REPO` : **{up_r}**
`UPSTREAM_BRANCH` : **{up_b}**
`GITHUB_REPO` :** {git}**
`GIT_TOKEN `:** {token}**


**<u>Bot Değişkeni:</u>**
`AUTO_LEAVING_ASSISTANT` : **{ass}**
`ASSISTANT_LEAVE_TIME` : **{auto_leave} saniye**
`AUTO_SUGGESTION_MODE` :** {a_sug}**
`AUTO_SUGGESTION_TIME` : **{auto_sug} saniye**
`AUTO_DOWNLOADS_CLEAR` : **{down}**
`PRIVATE_BOT_MODE` : **{pvt}**
`YOUTUBE_EDIT_SLEEP` : **{yt_sleep} saniye**
`TELEGRAM_EDIT_SLEEP` :** {tg_sleep} saniye**
`CLEANMODE_MINS` : **{cm} dk**
`VIDEO_STREAM_LIMIT` : **{v_limit} Grup**
`SERVER_PLAYLIST_LIMIT` :** {playlist_limit}**
`PLAYLIST_FETCH_LIMIT` :** {fetch_playlist}**

**<u>Spotify Değişkeni:</u>**
`SPOTIFY_CLIENT_ID` :** {sotify}**
`SPOTIFY_CLIENT_SECRET` : **{sotify}**

**<u>BOYUT DEĞİŞKENİ:</u>**
`TG_AUDIO_FILESIZE_LIMIT` :** {tg_aud}**
`TG_VIDEO_FILESIZE_LIMIT` :** {tg_vid}**

**<u>BAĞLANTI DEĞİŞKENİ:</u>**
`SUPPORT_CHANNEL` : **{s_c}**
`SUPPORT_GROUP` : ** {s_g}**
`START_IMG_URL` : ** {start}**
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
