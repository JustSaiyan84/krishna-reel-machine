import os
import json
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

OUTPUT_FILE = "short.mp4"

# =========================
# 1. Dummy Reel (test ke liye)
# =========================
def create_dummy_reel():
    with open(OUTPUT_FILE, "wb") as f:
        f.write(os.urandom(1024 * 100))  # 100KB dummy file
    print("🎬 Dummy reel created")


# =========================
# 2. Upload to Google Drive
# =========================
def upload_to_drive(file_path):
    print("☁️ Uploading to Google Drive...")

    SCOPES = ['https://www.googleapis.com/auth/drive']

    creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

    creds = service_account.Credentials.from_service_account_info(
        creds_dict, scopes=SCOPES)

    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [1PTPXQKrBXVCmwD7D9kUJ-skKkneMK-Uj]
    }

    media = MediaFileUpload(file_path, resumable=True)

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f"✅ Uploaded: {file.get('id')}")


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    create_dummy_reel()
    upload_to_drive(OUTPUT_FILE)
