# Domoticz2Telegram
Скрипт позволяет отправлять сообщения из Domoticz в Telegram вашему боту, используя ваш proxy.

## Установка
1. Необходимо самостоятельно настроить телеграм-бота через @BotFather, получить TOKEN, а так же получить chat_id (например, через бота @getmyid_bot).

2. Необходимо получить ip-адрес и порт рабочего proxy. Например, это можно сделать через Amazon AWS.

3. Поместить скрипт в папку ~/domoticz/scripts/customscripts/telegram/...

4. Дать права 
```
:~$ sudo chmod +x telegramnotify.py
```

5. В настройках Domoticz
Setup -> Settings -> Notifications -> Custom HTTP/Action:
 - Enabled: on
 - URL/Action: script://customscripts/telegram/telegramnotify.py #MESSAGE
 - Apply Settings

6. У датчиков/сенсоров/переключателей... выбрать метод оповещения 'http'.

## Использование
Domoticz будет запускать скрипт с текстом оповещения, который будет являться аргументом. 
Например:
```
ubuntu:~$ ./telegramnotify.py Температура в помещении превысила 30 градусов!
```
Сообщения будут приходить в формате:
```
[2019-07-31 15:00:00] Температура в помещении превысила 30 градусов!
```
