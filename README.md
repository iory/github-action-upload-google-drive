# Google Drive Upload Action (Python)

This GitHub Action allows you to **upload a file to Google Drive** using a **Google Service Account**.
It supports specifying the destination folder and renaming the file upon upload.

## 🚀 Features
- ✅ Upload any file to **Google Drive**
- ✅ Specify a **destination folder**
- ✅ Set a **custom file name** for the uploaded file
- ✅ Uses a **Service Account** for authentication
- ✅ Outputs the **Google Drive File ID** for further use

---

## 📌 **Inputs**
| Name | Description | Required |
|------|------------|----------|
| `service_account_json` | Base64-encoded Google Service Account JSON credentials. | ✅ Yes |
| `file_path` | The path of the file to upload. | ✅ Yes |
| `input_gdrive_file_name` | (Optional) The name of the file when uploaded to Google Drive. If not provided, the original file name will be used. | ❌ No |
| `folder_id` | The ID of the Google Drive folder where the file should be uploaded. | ✅ Yes |

---

## 📤 **Outputs**
| Name | Description |
|------|------------|
| `file_id` | The ID of the uploaded file in Google Drive. |

---

## 🔧 **Usage Example**
```yaml
name: Upload File to Google Drive

on:
  push:
    branches: [ "main" ]

jobs:
  upload-file:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Upload to Google Drive
        id: upload
        uses: iory/github-action-upload-google-drive@v0.0.3
        with:
          service_account_json: ${{ secrets.GDRIVE_CREDENTIALS }}
          file_path: "test.mp4"
          input_gdrive_file_name: "2024-02-13-1530-1234.mp4"
          folder_id: ${{ secrets.GDRIVE_FOLDER_ID }}

      - name: Comment on PR with File Link
        uses: thollander/actions-comment-pull-request@v3
        with:
          message: "🎬️ [Watch Hardware CI Test Video](https://drive.google.com/file/d/${{ steps.upload.outputs.file_id }}/view)"
