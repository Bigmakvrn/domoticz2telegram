import sys
import requests
import datetime

get_time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

#Put your bot's details here
bot_token = 'YOUR_BOT_TOKEN_HERE'
chat_id = 'YOUR_CHAT_ID'

text_line = (' '.join(sys.argv[1:]))
host_url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text=[{}]: {}".format(bot_token, chat_id, get_time, text_line)

#Put your proxy details here
#http://username:password@ip:port
proxies={
    'http' : "http://username:password@1.0.0.1:4040",
    'https' : "https://username:password@1.0.0.2:4646"
}

#Headers
headers={'Content-Type': 'application/json'}

#Sending
requests.get(host_url, headers=headers, proxies=proxies)
