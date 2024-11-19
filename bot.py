from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Token bot Anda
BOT_TOKEN = "API_BOT_FATHER"

# ID channel sumber
SOURCE_CHANNEL_ID = -1001678179757

# Daftar ID channel target
TARGET_CHANNEL_IDS = [
    -1002380898678,  # Channel target 1
    -1002013927555,  # Channel target 2
]

def repost_message(update: Update, context: CallbackContext):
    """Memposting ulang konten dari channel sumber ke channel target."""
    if update.channel_post and update.channel_post.chat.id == SOURCE_CHANNEL_ID:
        message = update.channel_post
        for target_channel_id in TARGET_CHANNEL_IDS:
            try:
                if message.text:  # Jika pesan berupa teks
                    context.bot.send_message(
                        chat_id=target_channel_id,
                        text=message.text,
                        parse_mode="HTML",
                    )
                elif message.photo:  # Jika pesan berupa foto
                    context.bot.send_photo(
                        chat_id=target_channel_id,
                        photo=message.photo[-1].file_id,  # Resolusi foto tertinggi
                        caption=message.caption if message.caption else "",
                        parse_mode="HTML",
                    )
                elif message.video:  # Jika pesan berupa video
                    context.bot.send_video(
                        chat_id=target_channel_id,
                        video=message.video.file_id,
                        caption=message.caption if message.caption else "",
                        parse_mode="HTML",
                    )
                print(f"Pesan berhasil diposting ke channel: {target_channel_id}")
            except Exception as e:
                print(f"Gagal memposting ke channel {target_channel_id}: {e}")

def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Menangani pesan dari channel sumber
    dispatcher.add_handler(MessageHandler(
        Filters.chat(SOURCE_CHANNEL_ID),  # Filter channel sumber
        repost_message
    ))

    print("Bot sedang berjalan...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
