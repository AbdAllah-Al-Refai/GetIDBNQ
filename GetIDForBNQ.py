from telegram.ext import Updater, CommandHandler
from run import server


# تعريف وظيفة التحكم في الأمر /start
def start(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(
        chat_id=chat_id,
        text=
        f"يرجى تعديل الرسالة التالية وفق المعلومات المطلوبة (مع الحفاظ على الرقم الظاهر في الرسالة) وارسالها الى الرقم التالي : 0999501581"
    )
    context.bot.send_message(
        chat_id=chat_id,
        text=f"اسم الطالب:......\nالعمر:....\nالحلقة:....\nChat ID: {chat_id}")

    context.bot.send_message(
        chat_id=chat_id,
        text=
        f" :بعد تعديل الرسالة السابقة وارسالها الى الحساب المطلوب يرجى الذهاب الى الحساب التالي https://t.me/KolokmRaa_bot والضغط على زر البدء لاستلام الملاحظات المتعلقة بالطالب"
    )


# تعريف وظيفة التحكم في الأمر /help
def help(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="أنا بوت تليجرام!")


def main():
    # تعيين رمز المطور الخاص بك هنا
    token = "7369844945:AAEuN4mZk6wv9-JDHzsMdjEzqnTJ3cm3w1U"

    # إنشاء مثيل Updater وتمريره رمز الوصول الخاص بك
    updater = Updater(token, use_context=True)

    # الحصول على معرف النص المستقبل عند الأمر /start
    updater.dispatcher.add_handler(CommandHandler('start', start))

    # الحصول على معرف النص المستقبل عند الأمر /help
    updater.dispatcher.add_handler(CommandHandler('help', help))

    # بدء الاستماع إلى التحديثات
    updater.start_polling()

    # استدعاء البوت للعمل حتى يتم إيقافه يدويًا
    updater.idle()


if __name__ == '__main__':
    server()
    main()
