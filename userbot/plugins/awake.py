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
        KANNADIGA_caption += f"     π KANNADIGA BOT β€οΈ\n"
        KANNADIGA_caption += f"β’π₯β’ πΊπ°π½π½π°π³πΈπΆπ° π±πΎπ     : Ξ½3.0\n"
        KANNADIGA_caption += f"β’π₯β’ ππ΄π»π΄ππ·πΎπ½      : `{version.__version__}`\n"
        KANNADIGA_caption += f"β’π₯β’ ππΏππΈπΌπ΄         : `{uptime}`\n"
        KANNADIGA_caption += (
            f"β’π₯β’ πΎππ½π΄π        : [KING OF KARNATAKA](t.me/Karunada_king)\n"
        )
        KANNADIGA_caption += (
            f"β’π₯β’ SUPPORT BASE : [TERITORRY](t.me/KARUNADA_KINGS_AND_QUEENS)\n"
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
            f"β’β‘β’ TELETHON    : `{version.__version__}`\n"
            f"β’π?π³β’ KANNADIGA BOT  : `{KANNADIGAversion}`\n"
            f"β’π?π³β’ UPTIME        : `{uptime}`\n"
            f"β’π±β’ MASTER        : {mention}\n"
            f"β’πβ’ OWNER         : [KING OF KARNATAKA](t.me/KARUNADA_KING)\n",
        )


CmdHelp("awake").add_command("awake", None, "ΟΡΡ Ξ±ΠΈβ ΡΡΡ").add_info(
    "Same Like Alive"
).add_type("Official").add()
