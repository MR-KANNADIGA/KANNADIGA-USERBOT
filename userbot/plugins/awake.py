import time

from telethon import version

from userbot import KANNADIGAversion, StartTime
from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd

from . import *


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


KANNADIGA_IMG = Config.AWAKE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "Kaannadigaru"
CUSTOM_YOUR_GROUP = Config.YOUR_GROUP or "@karunada_Kings_and_queens"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def amireallyalive(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)

    if KANNADIGA_IMG:
        KANNADIGA_caption = f"**{KANNADIGA_mention}**\n"

        KANNADIGA_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        KANNADIGA_caption += f"     💛 KANNADIGA BOT ❤️\n"
        KANNADIGA_caption += f"•🔥• 𝙺𝙰𝙽𝙽𝙰𝙳𝙸𝙶𝙰 𝙱𝙾𝚃     : ν3.0\n"
        KANNADIGA_caption += f"•🔥• 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽      : `{version.__version__}`\n"
        KANNADIGA_caption += f"•🔥• 𝚄𝙿𝚃𝙸𝙼𝙴         : `{uptime}`\n"
        KANNADIGA_caption += (
            f"•🔥• 𝙾𝚆𝙽𝙴𝚁        : [KING OF KARNATAKA](t.me/Karunada_king)\n"
        )
        KANNADIGA_caption += (
            f"•🔥• SUPPORT BASE : [TERITORRY](t.me/KARUNADA_KINGS_AND_QUEENS)\n"
        )

        await event.client.send_file(
            event.chat_id,
            KANNADIGA_IMG,
            caption=KANNADIGA_caption,
            reply_to=reply_to_id,
        )
        await event.delete()
    else:
        await edit_or_reply(
            awake,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         BOT STATUS\n"
            f"•⚡• TELETHON    : `{version.__version__}`\n"
            f"•🇮🇳• KANNADIGA BOT  : `{KANNADIGAversion}`\n"
            f"•🇮🇳• UPTIME        : `{uptime}`\n"
            f"•🔱• MASTER        : {mention}\n"
            f"•👑• OWNER         : [KING OF KARNATAKA](t.me/KARUNADA_KING)\n",
        )


CmdHelp("awake").add_command("awake", None, "υѕє αи∂ ѕєє").add_info(
    "Same Like Alive"
).add_type("Official").add()
