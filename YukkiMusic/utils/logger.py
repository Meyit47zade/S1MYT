from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Gizli Grup"
        logger_text = f"""**+ Grup : {message.chat.title} 
+ Grup ID : `{message.chat.id}`
+ Kullanıcı : {message.from_user.mention}
+ Kullanıcı Adı : @{message.from_user.username}
+ Kullanıcı ID : `{message.from_user.id}`
+ Grup Link : {chatusername}

✦ Aranan : `{message.text}`**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
