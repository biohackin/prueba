# Para que 1bot acepte peticiones inline set:
# /setinline y set placeholder in @botfhater
# pip install pyTelegramBotAPI

import os, sys, time, logging
import telebot
from telebot import types

API_TOKEN = os.getenv("API_TOKEN", "")

bot = telebot.TeleBot(API_TOKEN)
telebot.logger.setLevel(logging.DEBUG)

@bot.inline_handler(lambda query: query.query == '6367373737')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result1', types.InputTextMessageContent('hi'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('hi'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)



@bot.inline_handler(lambda query: query.query == 'opencj7')
def query_document(inline_query):
    try:

        r = types.InlineQueryResultDocument('Chat OpenAI by JulioCj7',
                                            document_url='https://JulioCj7.github.io/OpenAI.zip',
                                            title='ChatOpenAI', mime_type="application/zip")
        """
        r2 = types.InlineQueryResultDocument('req.txt',
                                            'https://raw.githubusercontent.com/SimplyTheBest666/nerd-fonts/master/css/requirements.txt',
                                            'https://raw.githubusercontent.com/SimplyTheBest666/nerd-fonts/master/css/requirements.txt',
                                            mime_type="application/pdf")
        """
        #bot.answer_inline_query(inline_query.id, [r, r2], cache_time=1)
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)





@bot.inline_handler(lambda query: query.query == 'photo1bjjdj')
def query_photo(inline_query):
    try:
        r = types.InlineQueryResultPhoto('1',
                                         'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
                                         'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
                                         input_message_content=types.InputTextMessageContent('hi'))
        r2 = types.InlineQueryResultPhoto('2',
                                          'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
                                          'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg')
        bot.answer_inline_query(inline_query.id, [r, r2], cache_time=1)
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'videooijjso')
def query_video(inline_query):
    try:
        r = types.InlineQueryResultVideo('1',
                                         'https://github.com/eternnoir/pyTelegramBotAPI/blob/master/tests/test_data/test_video.mp4?raw=true',
                                         'video/mp4',
                                         'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
                                         'Title'
                                         )
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: len(query.query) == 0)
def default_query(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'SimplyTheBest', types.InputTextMessageContent('Created by: SimplyTheBest'))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

def main_loop():
    bot.infinity_polling()
    while 1:
        time.sleep(3)

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)
