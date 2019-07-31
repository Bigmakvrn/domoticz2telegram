# Domoticz2Telegram
Sending Domoticz notifies to Telegram through proxy.

#### Installation
1. You need to get TOKEN for Telegram Bot (@BotFather can help you). Also you need to get chat_id (i.e. @getmyid_bot)

2. You need to get IP and proxy-port. (i.e. on Amazon AWS)

3. Create folder ~/domoticz/scripts/customscripts/telegram/... and create file telegramnotify.py

4. Add permissions for this file: 
```
:~$ sudo chmod +x telegramnotify.py
```

5. In Domoticz Settings:
Setup -> Settings -> Notifications -> Custom HTTP/Action:
* Enabled: on
* URL/Action: script://customscripts/telegram/telegramnotify.py #MESSAGE
* Apply Settings

6. In sensor/switch/... "Notifications" choose method of notify - 'http'.

#### Usage
Domoticz will start script with text of notify. Ths text will be the argument.
For example:
```
ubuntu:~$ ./telegramnotify.py Temperature in the main room is higher than 30 C!
```

In Telegram chat you will get a message:
```
[2019-07-31 15:00:00] Temperature in the main room is higher than 30 C!
```

## Requirements
* Requests v2.21.0 (installing: pip install requests)

## License
MIT License (MIT)
