import datetime as dt
import time
import quick_start
import Events_storage as EVENTS_STORAGE

def add_events(events):
    for event in events:
        # start = event['start'].get('dateTime', event['start'].get('date'))
        # print(start, event['summary'])
        # print(event)
        date_time_event_all = event['start']['dateTime'] #'2020-10-17T14:00:00+07:00'
        date_time_event_1 = date_time_event_all[0:-6]
        # timezone = date_time_event_all[20:22]
        # print(timezone)
        # timezone_ts = timezone.timetuple()
        # print(timezone_ts)

        # print(date_time_event_1)
        date_time_event_2 = dt.datetime.strptime(date_time_event_1, "%Y-%m-%dT%H:%M:%S")
        date_time_event_ts = time.mktime(date_time_event_2.timetuple())
        # print(date_time_event_ts)

        text_event = event['summary']
        print(text_event)

        if date_time_event_ts not in EVENTS_STORAGE.EVENTS_STORAGE.keys():
            EVENTS_STORAGE.EVENTS_STORAGE[date_time_event_ts] = {"msg": text_event, 'isPush': False}
            oiyopgououo