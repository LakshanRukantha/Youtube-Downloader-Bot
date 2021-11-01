from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "Report Bugs", url="https://t.me/Lakshan_Rukantha")]
    ])
    welcomed = f"Hello <b>{message.from_user.first_name}</b> Welcome to <b>YT Downloader</b> Bot. I can download YouTube Videos and download Audio Files from any of YouTube Video.\n\n💠 /help - How to use this Bot"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
