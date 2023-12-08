import os

from pyrogram import filters
from pyrogram.types import Message

from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils import close_key
from strings import get_command
from config import OWNER_ID
from YukkiMusic import app

CLEAN_COMMAND = get_command("CLEAN_COMMAND")


@app.on_message(filters.command(CLEAN_COMMAND) & SUDOERS)
async def clear_misc(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    downloads = os.path.realpath("downloads")
    down_dir = os.listdir(downloads)
    pth = os.path.realpath(".")
    os_dir = os.listdir(pth)

    if down_dir:
        for file in down_dir:
            os.remove(os.path.join(downloads, file))
    if os_dir:
        for lel in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg *.png")
    await message.reply_text("»** ᴏ̈ɴᴇᴍsɪᴢ ᴠᴇʀɪʟᴇʀɪ ᴛᴇᴍɪᴢʟᴇᴅɪᴍ ...\n» ʙᴏᴛ ᴀʀᴛɪᴋ ʜɪᴢʟɪ ᴠᴇ ᴛᴇᴍɪᴢ ...**",reply_markup=close_key,)
