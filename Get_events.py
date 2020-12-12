import datetime as dt
import time
import quick_start
import Events_storage as EVENTS_STORAGE 

def get_events():
    
    service = quick_start.main()
    # Call the Calendar API
    now = dt.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    # print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        return ''
        print('No upcoming events found.')
    else: return events
    # print(EVENTS_STORAGE)
