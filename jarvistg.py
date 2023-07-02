#!/usr/bin/python3
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram import InlineKeyboardMarkup , InlineKeyboardButton
from telegram.ext import CallbackQueryHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.commandhandler import CommandHandler
import wikipedia , soundfile , telegram , requests
import speech_recognition as sr
import instaloader, os


#telegram bot informations
#test-bot = 5871752348:AAFgKQhhaTmvJ4Dy2HiUHt9ROpa5E7tMgXA
#real-bot = 5943158276:AAEpC32sYWKa40rY2LPhgKo5Ga7brKopUR4
bot_token = "5943158276:AAEpC32sYWKa40rY2LPhgKo5Ga7brKopUR4"
updater = Updater(bot_token , use_context = True)
loader = instaloader.Instaloader()
loader.login("telaitel" , "telegramaitel.99*")
bad_words = ["فاک" , "جنده" , "قهبه" , "کیر" , "سکس" , "خایه" , "کص" , "کس" , "کوس" , "کوص" , "دیک"]

def markups():
    buttons = [
        [InlineKeyboardButton("راهنمای استفاده" , callback_data = "help")],
        [InlineKeyboardButton("تبلیغات" , callback_data = "ads")],
        [InlineKeyboardButton("درباره ربات" , callback_data = "about")],
        [InlineKeyboardButton("سازندگان" , callback_data = "creator")],
        [InlineKeyboardButton("پشتیبانی" , callback_data = "support")],
        [InlineKeyboardButton("اخبار و امکانات جدید" , callback_data = "news_options")],
        [InlineKeyboardButton("کانال اخبارات ربات" , callback_data = "channel")],
        [InlineKeyboardButton("بستن پنل" , callback_data = "close")],
    ]
    reply_markrup = InlineKeyboardMarkup(buttons)
    return reply_markrup

def close_marksup():
    buttons = [
        [InlineKeyboardButton("نمایش پنل" , callback_data = "panel")]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)
    return reply_markup

def start(update : Update , context : CallbackContext):
    try:
        update.message.reply_text("سلام اسم من مستر هست.با من میتونی به راحتی هرچیزی که لازم داری رو پیدا کنی و با اعضای گروه در میان بذاری.من از الگوریتم های یادگیری عمیق استفاده میکنم تا بهترین اطلاعات رو در اختیارتون بذار همچنین قابلیت جستجو با ویس هم اضافه شده کافیه گزینه راهنمای استفاده رو بزنی تا ببینی چطوری میتونی استفاده کنی.چه کاری از دستم بر میاد؟" , reply_markup = markups())

    except telegram.error.BadRequest:
        pass

def abide(update : Update , context : CallbackContext):
    try:
        user_Text = update.message.text
        text_Split = user_Text.split()
        chat = update.message.chat_id
        msg = update.message.message_id

        x = len(text_Split)

        for i in text_Split[0:x+1]:
            if i in bad_words:
                context.bot.delete_message(chat , msg)

        if user_Text == "سلام مستر":
            try:
                update.message.reply_text("سلام اسم من مستر هست.با من میتونی به راحتی هرچیزی که لازم داری رو پیدا کنی و با اعضای گروه در میان بذاری.من از الگوریتم های یادگیری عمیق استفاده میکنم تا بهترین اطلاعات رو در اختیارتون بذار همچنین قابلیت جستجو با ویس هم اضافه شده کافیه گزینه راهنمای استفاده رو بزنی تا ببینی چطوری میتونی استفاده کنی.چه کاری از دستم بر میاد؟" , reply_markup = markups())         
            
            except telegram.error.BadRequest:
                pass

        if text_Split[0] == "مستر":
            if text_Split[1] ==  "سرچ":
                search_value = ' '.join(text_Split[2:])

                try:
                    wiki_lang = wikipedia.set_lang('fa')
                    result = wikipedia.summary(search_value , sentences = 6)

                    update.message.reply_text(f"{result} \n\n Channel : @Mr_parviniii")
                except wikipedia.exceptions.PageError:
                    try:
                        update.message.reply_text("همچین چیزی نتونستم پیدا کنم و در سطح اینترنت درمورد این چیزی نبود" , reply_markup = markups())

                    except telegram.error.BadRequest:
                        pass

            elif text_Split[1] == "مقالات":
                about_for = ' '.join(text_Split[2:])

                wiki_lang = wikipedia.set_lang('fa')
                result = wikipedia.search(about_for)
                
                convert = ' - '.join(result)

                update.message.reply_text(f"کدوم رو میخوای? ({convert})")
            
            elif text_Split[1] == "فال":
                url = "https://hafez.p.rapidapi.com/fal"

                headers = {
                    "X-RapidAPI-Key": "b7396a63f8msh95706042732f682p1ffc4ejsn68390b6f5158",
                    "X-RapidAPI-Host": "hafez.p.rapidapi.com"
                }

                response = requests.get(url, headers=headers)

                resp_json = response.json()

                update.message.reply_text(f"{resp_json['poem']} \n\n Channel : @Mr_parviniii", reply_markup = markups())
            
            elif text_Split[1] == "اینستاگرام":
                try:
                    page_username = text_Split[2]

                    page = instaloader.Profile.from_username(loader.context, str(page_username))
                    page_picture = loader.download_profile(str(page_username), profile_pic_only = True)
                    page_followers = page.followers
                    page_followings = page.followees
                    page_posts_number = page.get_posts().count
                    page_name = page.full_name
                    page_bio = page.biography
                    page_private = page.is_private

                    os.system(f"mv {page_username}/*.jpg {page_username}/pic.jpg")

                    picture_file = open(f"{page_username}/pic.jpg", "rb")

                    if page_private == True:
                    
                        update.message.reply_photo(picture_file, caption = f"نام کاربری : {page_username}\nنام پیج : {page_name}\nبیوگرافی : {page_bio}\nتعداد فالوورها : {page_followers}\nتعداد فالویینگ ها : {page_followings}\nتعداد پست ها : {page_posts_number}\nوضعیت پیج : خصوصی")

                    else:
                        update.message.reply_photo(picture_file, caption = f"نام کاربری : {page_username}\nنام پیج : {page_name}\nبیوگرافی : {page_bio}\nتعداد فالوورها : {page_followers}\nتعداد فالویینگ ها : {page_followings}\nتعداد پست ها : {page_posts_number}\nوضعیت پیج : عمومی")
                    
                    os.system(f"rm -rf {text_Split[2]}")
                
                except instaloader.exceptions.ProfileHasNoPicsException:
                    if page_private == True:
                        update.message.reply_text(f"نام کاربری : {page_username}\nنام پیج : {page_name}\nبیوگرافی : {page_bio}\nتعداد فالوورها : {page_followers}\nتعداد فالویینگ ها : {page_followings}\nتعداد پست ها : {page_posts_number}\nوضعیت پیج : خصوصی")
                    
                    else:
                        update.message.reply_text(f"نام کاربری : {page_username}\nنام پیج : {page_name}\nبیوگرافی : {page_bio}\nتعداد فالوورها : {page_followers}\nتعداد فالویینگ ها : {page_followings}\nتعداد پست ها : {page_posts_number}\nوضعیت پیج : عمومی")
                
                except instaloader.exceptions.ProfileNotExistsException:
                    update.message.reply_text("ببخشید رفیق همچین پیجی نیست.")

            else:
                pass   
        
        
        elif text_Split[0] == "راهنما":
            try:
                update.message.reply_text("سلام اسم من مستر هست.با من میتونی به راحتی هرچیزی که لازم داری رو پیدا کنی و با اعضای گروه در میان بذاری.من از الگوریتم های یادگیری عمیق استفاده میکنم تا بهترین اطلاعات رو در اختیارتون بذارم همچنین قابلیت جستجو با ویس هم اضافه شده کافیه گزینه راهنمای استفاده رو بزنی تا ببینی چطوری میتونی استفاده کنی.چه کاری از دستم بر میاد؟")

            except telegram.error.BadRequest:
                pass

        else:
            pass
        
    
    except ArithmeticError:
        pass

def voice_text(update : Update , context : CallbackContext):

    user_voice = update.message.voice.file_id
    file_get = context.bot.get_file(user_voice)
    file_get.download("voice.wav")


    data, samplerate = soundfile.read('voice.wav')
    soundfile.write('sound.wav', data, samplerate, subtype='PCM_16')


    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile("sound.wav")

    with audio_file as source:
        audio = recognizer.record(source)

    
    try:
        word = recognizer.recognize_google(audio , language = "fa-IR" )
        convertor = str(word)
        splited  = convertor.split()
        chat = update.message.chat_id
        msg = update.message.message_id

        x = len(splited)

        for i in splited[0:x+1]:
            if i in bad_words:
                context.bot.delete_message(chat , msg)

        if splited[0] == "سرچ":
            try:
                wikipedia.set_lang("fa")
                result = wikipedia.summary(splited[1] , sentences = 6)
                update.message.reply_text(f"{result} \n\n Channel : @Mr_parviniii")
            except wikipedia.exceptions.PageError:
                try:
                    update.message.reply_text("همچین چیزی نتونستم پیدا کنم و در سطح اینترنت درمورد این چیزی نبود" , reply_markup = markups())

                except telegram.error.BadRequest:
                    pass
        
        elif splited[0] == "مستر":
            try:
                update.message.reply_text("سلام اسم من مستر هست.با من میتونی به راحتی هرچیزی که لازم داری رو پیدا کنی و با اعضای گروه در میان بذاری.من از الگوریتم های یادگیری عمیق استفاده میکنم تا بهترین اطلاعات رو در اختیارتون بذارم. کافیه گزینه راهنمای استفاده رو بزنی تا ببینی چطوری میتونی استفاده کنی.چه کاری از دستم بر میاد؟" , reply_markup = markups())
            
            except telegram.error.BadRequest:
                pass

        elif splited[0] == "راهنما":
            try:
                update.message.reply_text("سلام اسم من مستر هست.با من میتونی به راحتی هرچیزی که لازم داری رو پیدا کنی و با اعضای گروه در میان بذاری.من از الگوریتم های یادگیری عمیق استفاده میکنم تا بهترین اطلاعات رو در اختیارتون بذارم. کافیه گزینه راهنمای استفاده رو بزنی تا ببینی چطوری میتونی استفاده کنی.چه کاری از دستم بر میاد؟" , reply_markup = markups())

            except telegram.error.BadRequest:
                pass
        
        elif splited[0] == "فال":
            url = "https://hafez.p.rapidapi.com/fal"

            headers = {
                "X-RapidAPI-Key": "b7396a63f8msh95706042732f682p1ffc4ejsn68390b6f5158",
                "X-RapidAPI-Host": "hafez.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers)

            resp_json = response.json()

            update.message.reply_text(f"{resp_json['poem']} \n\n Channel : @Mr_parviniii" , reply_markup = markups())

        else:
            pass

    except sr.UnknownValueError:
        update.message.reply_text("واضح تر بگو رفیق اینطوری : گوگل" , reply_markup = markups())
    

def button(update : Update , context : CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == "help":
        try:
            query.message.edit_text("برای سرچ اطلاعات  : \n مستر سرچ [چیزی که میخوای رو اینجا بنویس]. \n\n بهترین مقاله های مرتبط : \n\n مستر مقالات [چیزی که میخوای اینجا بنویس]\n\nبرای سرچ مقالات انگلیسی به صورت فارسی :\nمستر سرچ [کلمه انگلیسی یا هر زبانی].\n\nبرای سرچ با ویس کافیه تو ویس  کلمه رو واضح بگی مثلا:\nسرچ گوگل \n\nبرای گرفتن فال :\n مستر فال\n\nبرای گرفتن فال به صورت ویس : \nکافیه تو ویس کلمه فال رو بگی : فال\n\nفعال سازی ربات با استفاده از ویس :\nکافیه تو ویس یکی از کلمات مستر یا راهنما رو بگی (فقط مستر یا راهنما)\n\n برای دانلود عکس و اطلاعات پیج اینستاگرامی : \nمستر اینستاگرام (یوزرنیم)\n\n موفق باشی رفیق :)" , reply_markup = markups())

        except telegram.error.BadRequest:
            pass

    elif query.data == "ads":
        try:
            query.message.edit_text("برای تبلیغات به ایدی زیر پیام دهید :‌\n @Mr_p100 \n کانال اخبارات جدید ربات : @‌masterbot_channel_news" , reply_markup = markups())
        
        except telegram.error.BadRequest:
            pass


    elif query.data == "about":
        try:
            query.message.edit_text("این ربات با استفاده ار الگوریتم های یادگیری عمیق در تلاش است که بهترین نتایج را در اختیار همگان بگذارد.از جمله ویژگی های ربات ترجمه متون زبان های مختلف به فارسی و در اختیار گذاشتن بهترین اطلاعات موجود در اختیار شماست.در تلاشیم ویژگی تشخیص متون انگلیسی از عکس و پیدا کردن اطلاعات مهم درمورد آن را به زودی ارائه دهیم.در نظر داشته باشید این ربات فقط بهترین  اطلاعات موجود در سطح اینترنت را برای شما به نمایش میگذارد که درک آن برای عموم راحت باشد. \n کانال اخبارات جدید ربات : @‌masterbot_channel_news" , reply_markup = markups())

        except telegram.error.BadRequest:
            pass

    elif query.data == "creator":
        try:
            query.message.edit_text("سازنده و طراح الگوریتم ها : @worldcinnection" , reply_markup = markups())

        except telegram.error.BadRequest:
            pass

    elif query.data == "support":
        try:
            query.message.edit_text("پشتیبانی:‌\n@worldcinnection\n@Mr_p100" , reply_markup = markups())

        except telegram.error.BadRequest:
            pass

    elif query.data == "news_options":
        try:
            query.message.edit_text("امکانات جدید ربات :\n\n 1.اضافه شدن سرچ با ویس\n\n 2. اضافه شدن گزینه بستن پنل\n\n 3. اضافه شدن ویس(به صورت تایپ و ویس)\n\n 4.قابلیت فعال سازی مستر با ویس(با کلمات راهنما یا مستر)\n\n5.اضافه شدن دریافت اطلاعات کلی از یک پیج در اینستا(به زودی دانلود پست نیز اضافه خواهد شد)\n\nبرای آموزش استفاده از ربات و قابلیت های ربات روی گزینه راهنمای استفاده کلیک کنید." , reply_markup = markups())

        except telegram.error.BadRequest:
            pass
    
    elif query.data == "close":
        try:
            query.message.edit_text("پنل بسته شد" , reply_markup = close_marksup())

        except telegram.error.BadRequest:
            pass
    
    elif query.data == "channel":
        try:
            query.message.edit_text("کانال اخبارات جدید ربات : @‌masterbot_channel_news", reply_markup = markups())
        
        except telegram.error.BadRequest:
            pass

    elif query.data == "panel":
        try:
            query.message.edit_text("سلام اسم من مستر هست.با من میتونی به راحتی هرچیزی که لازم داری رو پیدا کنی و با اعضای گروه در میان بذاری.من از الگوریتم های یادگیری عمیق استفاده میکنم تا بهترین اطلاعات رو در اختیارتون بذار همچنین قابلیت جستجو با ویس هم اضافه شده کافیه گزینه راهنمای استفاده رو بزنی تا ببینی چطوری میتونی استفاده کنی.چه کاری از دستم بر میاد؟" , reply_markup = markups())

        except telegram.error.BadRequest:
            pass


updater.dispatcher.add_handler(CommandHandler('start' , start))
updater.dispatcher.add_handler(MessageHandler(Filters.text , abide))
updater.dispatcher.add_handler(MessageHandler(Filters.voice , voice_text))
updater.dispatcher.add_handler(CallbackQueryHandler(button))


updater.start_polling()