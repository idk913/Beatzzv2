"""COMMAND : .join , .pay , .work , .push , .aag , .climb, .m1, .g1, .ftext"""
from telethon.tl.types import ChannelParticipantsAdmins

from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@borg.on(admin_cmd(pattern="join$"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`━━━━━┓ \n┓┓┓┓┓┃\n┓┓┓┓┓┃　ヽ○ノ ⇦ Me When You Joined \n┓┓┓┓┓┃.     /　 \n┓┓┓┓┓┃ ノ) \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd(pattern="pay$"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`█▀▀▀▀▀█░▀▀░░░█░░░░█▀▀▀▀▀█\n█░███░█░█▄░█▀▀░▄▄░█░███░█\n█░▀▀▀░█░▀█▀▀▄▀█▀▀░█░▀▀▀░█\n▀▀▀▀▀▀▀░▀▄▀▄▀▄█▄▀░▀▀▀▀▀▀▀\n█▀█▀▄▄▀░█▄░░░▀▀░▄█░▄▀█▀░▀\n░█▄▀░▄▀▀░░░▄▄▄█░▀▄▄▄▀▄▄▀▄\n░░▀█░▀▀▀▀▀▄█░▄░████ ██▀█▄\n▄▀█░░▄▀█▀█▀░█▄▀░▀█▄██▀░█▄\n░░▀▀▀░▀░█▄▀▀▄▄░▄█▀▀▀█░█▀▀\n█▀▀▀▀▀█░░██▀█░░▄█░▀░█▄░██\n█░███░█░▄▀█▀██▄▄▀▀█▀█▄░▄▄\n█░▀▀▀░█░█░░▀▀▀░█░▀▀▀▀▄█▀░\n▀▀▀▀▀▀▀░▀▀░░▀░▀░░░▀▀░▀▀▀▀`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd(pattern="climb$"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`😏/\n/▌ \n/ \\n████\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\😦\n╬╬/▌\n╬╬/\`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd(pattern="aag$"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`😲💨  🔥\n/|\     🔥🔥\n/ \   🔥🔥🔥`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd(pattern="push$"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`.      😎\n          |\👐\n         / \\\n━━━━━┓ ＼＼ \n┓┓┓┓┓┃\n┓┓┓┓┓┃ ヽ😩ノ\n┓┓┓┓┓┃ 　 /　\n┓┓┓┓┓┃  ノ)　 \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd(pattern="work$"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`📔📚             📚\n📓📚📖  😫  📚📚📓\n📕📚📚  📝  📗💻📘\n📖⁣📖📖📖📖📖📖📖📖`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
    
@bot.on(admin_cmd(outgoing=True, pattern="g1 ?(.*)"))
@bot.on(sudo_cmd(pattern="g1 ?(.*)", allow_sudo=True))
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
    )
    await edit_or_reply(event, pay)
    
    
@bot.on(admin_cmd(pattern="ftext (.*)"))
@bot.on(sudo_cmd(pattern="ftext (.*)", allow_sudo=True))
async def payf(event):
    paytext = event.pattern_match.group(1)
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
    await edit_or_reply(event, pay)
    
@bot.on(admin_cmd(pattern="ml (.*)"))
@bot.on(sudo_cmd(pattern="ml (.*)", allow_sudo=True))
async def kakashi(beats):
    message = beats.pattern_match.group(1)
    await edit_or_reply(
        beats,
        "`\n█████████`"
        "`\n█▄█████▄█`"
        "`\n█▼▼▼▼▼`"
        f"`\n█  {message}`"
        "`\n█▲▲▲▲▲`"
        "`\n█████████`"
        "`\n ██   ██`",
    )
