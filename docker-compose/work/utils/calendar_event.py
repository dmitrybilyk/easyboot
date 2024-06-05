import datetime
import os
import sys
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def main(event_summary):
    """Shows basic usage of the Google Calendar API.
    Creates a Google Calendar API service object and adds an event.
    """
    creds = None

    # Check if the credentials are available in environment variables
    client_id = '32660785819-rujpth3h7o7ihj7hi5fsj2p68uj0pq4o.apps.googleusercontent.com'
    client_secret = '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'
    refresh_token = os.getenv('GOOGLE_REFRESH_TOKEN')

    if client_id and client_secret and refresh_token:
        creds = Credentials(
            token=None,
            refresh_token=refresh_token,
            token_uri='https://oauth2.googleapis.com/token',
            client_id=client_id,
            client_secret=client_secret,
            scopes=SCOPES
        )
    else:
        # If no valid credentials are available, let the user log in.
        flow = InstalledAppFlow.from_client_secrets_file(
            '/home/dmytro/Dropbox/pers/google_api/calendar/client_secret_32660785819-rujpth3h7o7ihj7hi5fsj2p68uj0pq4o.apps.googleusercontent.com(1).json', SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Calculate start and end times
    now = datetime.datetime.utcnow()
    start_time = now + datetime.timedelta(minutes=40)
    end_time = start_time + datetime.timedelta(days=5)

    # Define the event details
    event = {
        'summary': event_summary,
        'location': 'Location details here',
        'description': '',
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
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    # Call the Calendar API to add the event
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <event_summary>")
        sys.exit(1)
    event_summary = sys.argv[1]
    main(event_summary)
