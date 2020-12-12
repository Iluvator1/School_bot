import datetime as dt
import time

# date_time_event = dt.datetime.strptime("2020-10-28T13:00:00", "%Y-%m-%dT%H:%M:%S")
# date_time_event_ts = time.mktime(date_time_event.timetuple())
# print(date_time_event_ts)

# timestamp_now = dt.datetime.now()
# print(timestamp_now)

# now = dt.datetime.utcnow() #.isoformat()
# print(now)


# date_time_event_1 = '2020-10-17T14:00:00+07:00'
# timezone = dt.datetime.strptime(date_time_event_1[20:22], '%H')
# print(timezone)

# # timezone_ts = time.mktime(timezone.timetuple()) 
# timezone_ts = time.mktime(timezone.timetuple())

# print(timezone_ts)

EVENTS_STORAGE = {
    "1602166418": { 
        "msg": 'Первое сообщение',
        "isPush": False
    },
    "1602166518": { 
        "msg": 'Второе сообщение',
        "isPush": False
    }
}
print(EVENTS_STORAGE.keys())
# if EVENTS_STORAGE[date_time_event_ts] not in EVENTS_STORAGE:
#             EVENTS_STORAGE[date_time_event_ts] = {"msg": text_event, 'isPush': False