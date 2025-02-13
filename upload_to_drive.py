#!/usr/bin/env python3
import os
import sys
import base64
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def main():
    service_account_json_base64 = os.environ.get("INPUT_SERVICE_ACCOUNT_JSON")
    file_path = os.environ.get("INPUT_FILE_PATH")
    folder_id = os.environ.get("INPUT_FOLDER_ID", "").strip()
    gdrive_file_name = os.environ.get("INPUT_GDRIVE_FILE_NAME", "").strip()

    if not service_account_json_base64:
        print("Error: 'service_account_json' is not provided.")
        sys.exit(1)

    if not file_path:
        print("Error: 'file_path' is not provided.")
        sys.exit(1)

    service_account_info = json.loads(base64.b64decode(service_account_json_base64).decode("utf-8"))
    creds = Credentials.from_service_account_info(service_account_info, scopes=["https://www.googleapis.com/auth/drive.file"])
    drive_service = build("drive", "v3", credentials=creds)

    file_name = gdrive_file_name if gdrive_file_name else os.path.basename(file_path)
    file_metadata = {
        "name": file_name # Name on Google Drive
    }
    if folder_id:
        file_metadata["parents"] = [folder_id]
    media = MediaFileUpload(file_path, resumable=True)

    uploaded_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()

    file_id = uploaded_file.get("id")

    print(f"Uploaded file ID: {file_id}")
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        print(f"file_id={file_id}", file=f)

if __name__ == "__main__":
    main()