import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Authenticate and authorize Google API
SCOPES = ['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/keep']

# Path to the credentials JSON file downloaded from Google Cloud Console
SERVICE_ACCOUNT_FILE = '~/dev/projects/easyboot/docker-compose/work/utils/credentials.json'

# Path to save the JSON file locally
LOCAL_JSON_FILE_PATH = 'local_file.json'

# Content of the note to be added to Google Keep
KEEP_NOTE_CONTENT = 'This is a note added from Python script.'

def authenticate():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def save_json_to_drive(service):
    # Create a JSON file locally
    data = {'example': 'data'}
    with open(LOCAL_JSON_FILE_PATH, 'w') as f:
        json.dump(data, f)

    # Upload the file to Google Drive
    file_metadata = {'name': 'example.json'}
    media = MediaFileUpload(LOCAL_JSON_FILE_PATH, mimetype='application/json')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f'File ID: {file.get("id")}')

def add_note_to_keep(service):
    # Add a note to Google Keep
    service.notes().create(
        parent='keep',
        body={
            'text': KEEP_NOTE_CONTENT
        }
    ).execute()
    print('Note added to Google Keep.')

def main():
    # Authenticate
    creds = authenticate()

    # Create Drive and Keep service instances
    drive_service = build('drive', 'v3', credentials=creds)
    keep_service = build('keep', 'v1', credentials=creds)

    # Save JSON file to Drive
    save_json_to_drive(drive_service)

    # Add note to Google Keep
    add_note_to_keep(keep_service)

    # Clean up: Remove the local JSON file
    if os.path.exists(LOCAL_JSON_FILE_PATH):
        os.remove(LOCAL_JSON_FILE_PATH)
        print(f'Removed {LOCAL_JSON_FILE_PATH}')

if __name__ == '__main__':
    main()
