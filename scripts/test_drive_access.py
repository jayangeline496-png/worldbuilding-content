import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Config
KEY_PATH = os.path.expanduser("~/.config/gsc_service_account.json")
FOLDER_ID = "1YqaPHRfaVfArvpWG3JFO7bkZ2wo7PMiX"

def test_drive_access():
    print(f"Using service account: jay-gsc@jay-angeline-seo.iam.gserviceaccount.com")
    credentials = service_account.Credentials.from_service_account_file(
        KEY_PATH, 
        scopes=['https://www.googleapis.com/auth/drive']
    )
    service = build('drive', 'v3', credentials=credentials)

    # 1. Try to list files in the folder
    print(f"Attempting to list files in folder: {FOLDER_ID}")
    try:
        results = service.files().list(
            q=f"'{FOLDER_ID}' in parents",
            spaces='drive',
            fields='files(id, name)'
        ).execute()
        files = results.get('files', [])
        print(f"Found {len(files)} files in folder.")
        for f in files:
            print(f"- {f['name']} ({f['id']})")
    except Exception as e:
        print(f"Error listing files: {e}")

    # 2. Try to create a test file
    print("\nAttempting to create a test file...")
    file_metadata = {
        'name': 'Clawdbot Test.txt',
        'parents': [FOLDER_ID]
    }
    
    file_id = None
    try:
        file = service.files().create(body=file_metadata, fields='id').execute()
        file_id = file.get('id')
        print(f"Success! Created file with ID: {file_id}")
    except Exception as e:
        print(f"Error creating file: {e}")

    if file_id:
        print(f"\nAttempting to upload content to file: {file_id}")
        with open('test_upload.txt', 'w') as f:
            f.write('Service account test upload - round 3.')
        media = MediaFileUpload('test_upload.txt', mimetype='text/plain')
        try:
            # Add supportsAllDrives=True just in case, though it's My Drive
            updated_file = service.files().update(
                fileId=file_id, 
                media_body=media,
                supportsAllDrives=True
            ).execute()
            print(f"Success! Updated content for file: {updated_file.get('id')}")
        except Exception as e:
            print(f"Error updating file: {e}")

if __name__ == "__main__":
    test_drive_access()
