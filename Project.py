import datetime as dt
import time
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import quick_start
import Get_events
import Add_events
import Events_storage as EVENTS_STORAGE

#Events_storage

USERS = [323694612] #, 262474372, 291193268
COOLDOWN = 5
TOKEN = "daabff639a9211f5cd2e3008cba0ad4cbb59b34c2cd0d9d6fcf4071b9e52d164373c288f0f8c639cc15c5"

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)

Add_events.add_events(Get_events.get_events())

def sender(id, text):
    vk_session.method('messages.send', {
        'user_id': id,
        'message': text,
        'random_id': 0
    })
    print("[LOG][Info] send msg into id:", id, "msg:", text)

def push_msg_all_users(users: list, msg: str):
    for user in users:
        sender(user, msg)

print("[LOG][Info] Bot start")
while (True):

    time.sleep(COOLDOWN)
    Get_events.get_events()
    timestamp_now = int(dt.datetime.now().timestamp())
    print("[LOG][Info] now:", timestamp_now)
    for timestamp in list(EVENTS_STORAGE.EVENTS_STORAGE):
        if int(timestamp) < timestamp_now and EVENTS_STORAGE.EVENTS_STORAGE[timestamp]["isPush"] == False:
            push_msg_all_users(USERS, EVENTS_STORAGE.EVENTS_STORAGE[timestamp]["msg"])
            EVENTS_STORAGE.EVENTS_STORAGE[timestamp]["isPush"] = True


# 1) hardcode нотификаций в вк +
# 2) hardcode получение из гугл календаря +
# 3) hardocode взаимодейтсвие п.1 и п.2 - 

# 4) hardcode -> code

# test case
# 1) запуск -> в вк придет евент с гугл-каленадаря
# 2) заупусе -> добавление евента в календарь -> в вк придет евент с гугл-каленадаря