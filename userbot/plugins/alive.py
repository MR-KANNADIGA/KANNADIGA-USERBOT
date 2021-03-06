import asyncio
import os
import random
import time
from platform import python_version

from telethon import version
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from userbot import *
from userbot import KANNADIGAversion
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from userbot.helpers.events import reply_id
from userbot.helpers.ffunctions.utils import get_readable_time
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd

from . import *

KANNADIGA_IMG = "https://te.legra.ph/file/e1be79e4d3d61f7c85555.jpg"
CUSTOM_YOUR_GROUP = Config.YOUR_GROUP or "@NAAN_1_KANNADIGA"


@bot.on(admin_cmd(outgoing=True, pattern="kannadiga$"))
@bot.on(sudo_cmd(pattern="kannadiga$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = get_readable_time((time.time() - StartTime))
    uptime = uptime
    about = os.environ.get("ALIVE_EMOJI", None) or "✥"
    if about is not None:
        b = about.split()
        c = []
        if len(b) >= 1:
            for d in b:
                c.append(d)
        alive_emoji = random.choice(c)
    if KANNADIGA_IMG:
        KANNADIGA_caption = f"**KANNADIGABOT is Up And Running**\n\n"
        KANNADIGA_caption += f"      🔰Bot Status🔰 \n"
        KANNADIGA_caption += (
            f"{alive_emoji} **KANNADIGABo† version**   ~ {KANNADIGAversion}\n"
        )
        KANNADIGA_caption += (
            f"{alive_emoji} **Telethon version**   ~ `{version.__version__}`\n"
        )
        KANNADIGA_caption += (
            f"{alive_emoji} **Python version**    ~ `{python_version()}`\n"
        )
        KANNADIGA_caption += f"{alive_emoji} **Uptime**           ~ `{uptime}`\n"
        KANNADIGA_caption += (
            f"{alive_emoji} **Master**          ~ `{Config.ALIVE_NAME}`"
        )
        await alive.client.send_file(
            alive.chat_id,
            KANNADIGA_IMG,
            caption=KANNADIGA_caption,
            reply_to=reply_to_id,
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            "Soon new Template Add",
        )


msg = (
    gvarstatus("ALIVE_TEMPLATE")
    or f"""
**  ⚜️ Kannadiga Bot is Online ⚜️**
     {Config.ALIVE_MSG}
    ** Bot Status **
**🔰 Owner   :** **{Config.ALIVE_NAME}**
**✨ KANNADIGABOT  :** {KANNADIGAversion}
**✨ Telethon  :** {version.__version__}
**✨ Abuse    :**  {abuse_m}
**✨ Sudo    :**  {is_sudo}
**✨ Bøt   :** {Config.BOY_OR_GIRL}
"""
)
botname = Config.BOT_USERNAME


@bot.on(admin_cmd(pattern="alive$"))
@bot.on(admin_cmd(pattern="alive$", allow_sudo=True))
async def KANNADIGA_a(event):
    try:
        KANNADIGA = await bot.inline_query(botname, "alive")
        await KANNADIGA[0].click(event.chat_id)
        await event.delete()
        if event.sender_id == Mr_Professor_Agora:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


file1 = "https://te.legra.ph/file/e1be79e4d3d61f7c85555.jpg"
file2 = "https://te.legra.ph/file/e1be79e4d3d61f7c85555.jpg"
file3 = "https://te.legra.ph/file/e1be79e4d3d61f7c85555.jpg"
file4 = "https://te.legra.ph/file/e1be79e4d3d61f7c85555.jpg"
file5 = "https://te.legra.ph/file/e1be79e4d3d61f7c85555.jpg"
"""=======================CONSTANTS====================== """
pm_caption = f"**╭────────────**\n"
pm_caption += f"┣✨ Master   ~ {Config.ALIVE_NAME}\n"
pm_caption += f"┣✨ KANNADIGABOT ~ {KANNADIGAversion}\n"
pm_caption += f"┣✨ Owner   ~ [Mr Kannadiga](https://t.me/Mr_StonedLegend)\n"
pm_caption += f"┣✨ Support ~ [Group](https://t.me/NAAN_1_KANNADIGA)\n"
pm_caption += f"┣✨ Repo   ~ [Repo](https://github.com/MR-KANNADIGA/KANNADIGABOT)\n"
pm_caption += f"**╰────────────**\n"


@borg.on(admin_cmd(pattern=r"about"))
@borg.on(sudo_cmd(pattern="about$", allow_sudo=True))
async def amireallyalive(yes):
    edit_time = 12
    reply_to_id = await reply_id(yes)
    await yes.get_chat()
    on = await borg.send_file(
        yes.chat_id, file=file1, caption=pm_caption, reply_to=reply_to_id
    )
    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file4)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file2)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file1)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file2)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file3)

    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(yes.chat_id, ok10, file=file4)

    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(yes.chat_id, ok11, file=file5)

    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(yes.chat_id, ok12, file=file1)

    await yes.delete()

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command("bot", None, "υѕє αи∂ ѕєє").add_command(
    "KANNADIGA", None, "Its Same Like Alive"
).add_command("about", None, "BEST alive command").add_command(
    "alive", None, "Its Show ur Alive Template"
).add_warning(
    "Harmless Module✅"
).add_info(
    "Checking Alive"
).add_type(
    "Official"
).add()
