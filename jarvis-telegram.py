from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram import InlineKeyboardMarkup , InlineKeyboardButton
from telegram.ext import CallbackQueryHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
import wikipedia

#telegram bot informations
bot_token = "5943158276:AAFCwbeaK_lumjXlP3XMSbpJ9hI9-9Awzvw"
updater = Updater(bot_token , use_context = True)

#Bot owners and managers and restrictions
bio = "Hello everyone. My name is jarvis. Im AI bot and I give you best result about what you want.For example you can search many articles and I show best results to you with my Deep learning ALG. send me guid to help you how you can search with me"

def abide(update : Update , context : CallbackContext):
    user_username = update.message.from_user.username
    user_Text = update.message.text
    text_Split = user_Text.split()
    if user_Text.lower() == "jari":
        update.message.reply_text("Hi. My name is jarvis. Im AI bot and I give you best result about what you want.For example you can search many articles and I show best results to you with my Deep learning ALG. send me 'guid' to help you how you can search with me")
    if text_Split[0].lower() == "jarvis":           
        if text_Split[1].lower() == "search":
            search_value = text_Split[2]
            wiki_lang = wikipedia.set_lang('fa')
            result = wikipedia.summary(search_value , sentences = 6)
            update.message.reply_text(result)
        elif text_Split[1].lower() == "same":
            about_for = text_Split[2]
            wiki_lang = wikipedia.set_lang('en')
            result = wikipedia.search(about_for)
            convert = ''.join(result)
            update.message.reply_text(f"Which one do you want sir ? ({convert})")
        else:
            update.message.reply_text("send like : jarvis search iran or jarvis same iran")
    
    elif text_Split[0].lower() == "guid":
        keyboards = [
            [InlineKeyboardButton("For members" , callback_data = "members")]
        ]
        update.message.reply_text("For which user you want a bot guid ?" , reply_markup = InlineKeyboardMarkup(keyboards))

def button(update : Update , context : CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == "members":
        query.message.edit_text("Informations about article : \n\n jarvis search [article name in english].\n\n For find same articles with your name do this : \n\n jarvis same iran[article name in english]. You can test it now :)")

updater.dispatcher.add_handler(MessageHandler(Filters.text , abide))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()