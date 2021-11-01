from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Follow these three simple steps.\n\n1) Send URL of YouTube video do you want to download. 😃\n\n2) Select quality of video or audio do you want to download. 🤩\n\n3) Download ✅\n\nContact @Lakshan_Rukantha for report bugs and problems of this bot."
    await message.reply_text(helptxt)

@Client.on_message(Filters.command(["ping"]))
async def start(client, message):
    botStatus = f"I am online... XD"
    await message.reply_text(botStatus)

@Client.on_message(Filters.command(["report"]))
async def start(client, message):
    report = f"Feel free to contact admin for report any bugs or suggestions.\n\nAdmin : @Lakshan_Rukantha"
    await message.reply_text(report)
