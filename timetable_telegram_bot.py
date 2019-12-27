from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import pytz
from datetime import datetime
import schedule
tz = pytz.timezone('Asia/Kolkata')
now = datetime.now(tz)
current_day = now.strftime("%A")
current_time = int(now.strftime("%H%M"))
current_time_next_hour = int(now.strftime("%H"))+1
key_to_find = current_day[0:2].lower()+ str(current_time_next_hour)
def next(bot, update):
    daily_schedule ={"mo09":"French Class in SJT 105","mo10":"NoSQL Class in SJT 606","mo11":"Operations Class in SJT 522","mo14":"OS Class in MGB 105",
    "mo16":"Digital Class in MB 123","mo18":"Soft Skills in MGB 106","tu08":"Operations Class in SJT 522","tu11":"Virtual OS lab in MGB 107A",
    "tu14":"Machine Learing in MGB 106","tu15":"SoftSkills in MGB 106","tu16":"IOT Class in MGB 106","tu17":"IOT Lab in SJT 218",
    "we10":"French Class in SJT 105","we15":"OS Class in MGB 105","we17":"Digital Systems Class in MB 213","th08":"NoSQL Class in SJT 606","th09":"Operations Class in SJT 522",
    "th14":"Digital Systems Class in MB 213","th15":"Machine Learning Class in MGB 106","th16":"Soft Skills Class in MGB 106",
    "fr11":"Machine Learning Lab in SJT 216","fr14":"IOT Class in MGB 106","fr16":"NoSQL Lab in SJT 122"}
    if key_to_find in daily_schedule:
        message = daily_schedule.get(key_to_find)
    else:
        x = requests.get("https://api.telegram.org/bot1069722915:AAGwLWDoog259j8ejRvlsWpTuqL_tAtB8z8/sendMessage?chat_id=921740638&parse_mode=Markdown&text=No period next hour. Enjoy :)")

#    message = schedule.get(key_to_find)

    get_request(message)
def get_request(messagedata):
    x = requests.get("https://api.telegram.org/bot1069722915:AAGwLWDoog259j8ejRvlsWpTuqL_tAtB8z8/sendMessage?chat_id=921740638&parse_mode=Markdown&text="+messagedata)

def main():
    updater = Updater('1069722915:AAGwLWDoog259j8ejRvlsWpTuqL_tAtB8z8')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('next',next))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()




