import nekos

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="ftext ?(.*)"))
@bot.on(sudo_cmd(pattern="ftext ?(.*)", allow_sudo=True))
async def payf(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str:
        paytext = input_str
        pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
            paytext * 8,
            paytext * 8,
            paytext * 2,
            paytext * 2,
            paytext * 2,
            paytext * 6,
            paytext * 6,
            paytext * 2,
            paytext * 2,
            paytext * 2,
            paytext * 2,
            paytext * 2,
        )
    else:
        pay = "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯\n"

    await event.edit(pay)


@bot.on(admin_cmd(pattern="cat$"))
@bot.on(sudo_cmd(pattern="cat$", allow_sudo=True))
async def hmm(KANNADIGA):
    if KANNADIGA.fwd_from:
        return
    reactcat = nekos.textcat()
    await edit_or_reply(KANNADIGA, reactcat)


@bot.on(admin_cmd(pattern="why$"))
@bot.on(sudo_cmd(pattern="why$", allow_sudo=True))
async def hmm(KANNADIGA):
    if KANNADIGA.fwd_from:
        return
    whyKANNADIGA = nekos.why()
    await edit_or_reply(KANNADIGA, whyKANNADIGA)


@bot.on(admin_cmd(pattern="fact$"))
@bot.on(sudo_cmd(pattern="fact$", allow_sudo=True))
async def hmm(KANNADIGA):
    if KANNADIGA.fwd_from:
        return
    factKANNADIGA = nekos.fact()
    await edit_or_reply(KANNADIGA, factKANNADIGA)


CmdHelp("funtxts").add_command(
    "cat", None, "Sends you some random cat facial text art"
).add_command("why", None, "Asks some random funny questions").add_command(
    "fact", None, "Sends you some random facts"
).add_command(
    "ftext", "<text>", 'Writes your text in "F" format'
).add()
