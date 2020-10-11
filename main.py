import telegram as tg
from telegram.ext import Updater as up
import logging as log
from telegram.ext import CommandHandler as CH

bot = tg.Bot(token='1032061895:AAFw6Ge2n9ytkuUgqUFOvnr1BOvUfaNKweQ')
upd = up(token='1032061895:AAFw6Ge2n9ytkuUgqUFOvnr1BOvUfaNKweQ', use_context=True)
dis = upd.dispatcher
log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=log.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Henlo!")


start_handler = CH('start', start)
dis.add_handler(start_handler)
upd.start_polling()


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


from telegram.ext import MessageHandler, Filters

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dis.add_handler(echo_handler)
