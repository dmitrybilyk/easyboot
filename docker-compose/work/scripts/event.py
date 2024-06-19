import datetime
import os
import sys
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def get_credentials():
    """Get credentials, either by loading from token.json or performing OAuth2 flow."""
    creds = None

    # Check if token.json exists and load credentials from it
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '~/dev/projects/easyboot/docker-compose/work/utils/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def main(event_summary):
    """Creates a Google Calendar API service object and adds an event."""
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)

    # Calculate start and end times
    now = datetime.datetime.utcnow()
    start_time = now + datetime.timedelta(minutes=12)
    end_time = start_time + datetime.timedelta(days=2, hours=14)  # Event duration is 2 days and 14 hours

    # Define the event details
    event = {
        'summary': event_summary,
        'location': 'Lviv, Ukraine',
        'description': 'This event will be lasting for 2 days unless you swipe it',
        'start': {
            'dateTime': start_time.isoformat() + 'Z',  # 'Z' indicates UTC time
            'timeZone': 'Europe/Kiev',
        },
        'end': {
            'dateTime': end_time.isoformat() + 'Z',  # 'Z' indicates UTC time
            'timeZone': 'Europe/Kiev',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 1},
                {'method': 'popup', 'minutes': 10}
            ],
        },
        'visibility': 'public',
        'colorId': '9'  # Magenta color
    }

    # Call the Calendar API to add the event
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event is added to a Google Calendar')

if __name__ == '__main__':
    event_summary = ' '.join(sys.argv[1:])
    if not event_summary:
        print("Usage: python script_name.py <event_summary>")
        sys.exit(1)
    main(event_summary)
