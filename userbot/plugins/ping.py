import asyncio
import datetime
import os

from .. import ALIVE_NAME
from ..cmdhelp import CmdHelp
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND User"
legend = borg.uid
LEGEND_IMG = os.environ.get(
    "PING_PIC", "https://te.legra.ph/file/4eba78d12030ad7ad7f04.mp4"
)

start = datetime.datetime.now()
end = datetime.datetime.now()
ms = (end - start).microseconds / 1000


@bot.on(admin_cmd(pattern=f"hbping$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"hbping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 26)
    await edit_or_reply(event, "ping....")
    animation_chars = [
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ ",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ ",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n \n My 🇵 🇮 🇳 🇬  Is : Calculating...",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 26])
    await edit_or_reply(
        event,
        "‎‎‎‎‎‎‎‎‎⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛📶📶📶📶📶📶📶⬛\n⬛⬛⬛⬛📶⬛⬛📶⬛\n⬛⬛⬛⬛📶⬛⬛📶⬛\n⬛⬛⬛⬛📶⬛⬛📶⬛\n⬛⬛⬛⬛⬛📶📶⬛⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛⬛📶📶📶📶📶⬛⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛⬛📶📶📶📶📶⬛⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛📶📶📶📶📶📶📶⬛\n⬛⬛⬛⬛⬛⬛📶⬛⬛\n⬛⬛⬛⬛⬛📶⬛⬛⬛\n⬛⬛⬛⬛📶⬛⬛⬛⬛\n⬛📶📶📶📶📶📶📶⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛⬛📶📶📶📶📶⬛⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛📶⬛⬛⬛📶⬛\n⬛⬛📶📶⬛⬛📶⬛⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛📶⬛📶📶📶📶📶⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n‎‎‎‎‎‎‎‎‎ \n \n My 🇵 🇮 🇳 🇬  Is : {} ms".format(
            ms
        ),
    )


@bot.on(admin_cmd(pattern="ping$", outgoing=True))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "**(❛ ᑭσɳց ❜!**")
    if LEGEND_IMG:
        legend_caption = (
            f"**💞Pong💞**\n\n   🔸️ {ms}\n   🔹️ **𝙼𝚢** **𝙼𝚊𝚜𝚝𝚎𝚛** ~『{legend_mention}』"
        )
        await event.client.send_file(event.chat_id, LEGEND_IMG, caption=legend_caption)
        await event.delete()


CmdHelp("ping").add_command(
    "ping", None, "Shows you the ping speed of server"
).add_command(
    "hbping", None, "Shows you the ping speed of server with an animation"
).add_type(
    "Official"
).add()
