from telethon import version

from userbot import *
from userbot.cmdhelp import CmdHelp
from userbot.utils import *

# -------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "KANNADIGA"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

KANNADIGA = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={KANNADIGA})"


PM_IMG = "https://te.legra.ph/file/c085085b63638ae1ba5cf.jpg"
pm_caption = "**πΊππ½πππ³ππΆπ ππΎπ πΈπ ππ½πππ½π**\n\n"

pm_caption += f"**βπ₯πππππππππ ππππ₯β**\n"
pm_caption += f"**β£π πΌπ°πππ΄π:{mention}**\n"
pm_caption += f"**β£β‘ ππ΄π»π΄ππ·πΎπ½ : `{version.__version__}`**\n"
pm_caption += f"**β£π πΊπ°π½π½π°π³πΈπΆπ°π±πΎπ :{KANNADIGAversion}**\n"
pm_caption += f"**β£π πππ³πΎ     : `{sudou}`**\n"
pm_caption += f"**β£π¨βπ« πΎππ½π΄π     : [πΊπ°π½π½π°π³πΈπΆπ°](https://t.me/Mr_Professor_Agora)**\n"
pm_caption += f"**β[ππΆππΎππΏβ€οΈ](https://t.me/NAAN_1_KANNADIGA)β**\n"

pm_caption += "    [β¨ ππ΄πΏπΎ β¨](https://github.com/MR-KANNADIGA/KANNADIGABOT) πΉ [πLicenseπ](https://github.com/MR-KANNADIGA/KANNADIGABOT/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="bot$"))
@bot.on(sudo_cmd(pattern="bot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alv").add_command(
    "alive", None, "Check weather the bot is alive or not"
).add_command(
    "bot",
    None,
    "Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg",
).add_warning(
    "Harmless Module"
).add_info(
    "Are u alive?"
).add_type(
    "Official"
).add()
