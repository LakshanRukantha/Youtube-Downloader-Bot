from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "Report Bugs", url="https://t.me/Lakshan_Rukantha")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n\n💠 /help - How to use this Bot"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
