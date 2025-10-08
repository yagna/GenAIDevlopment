from pathlib import Path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.auth.transport.requests import Request
import csv
import io

CSV_HEADERS = [
    "full_name","email","phone","contact_type","business_name","street_address",
    "city","country","state","postal_code","website","tags","group_name",
    "created_at","updated_at","contact_source","opportunity_name","lead_value",
    "assigned_to_staff","opportunity_source","date_of_birth",
    "will_yo_xzqcsj","whats_y_rlmyeg"
]

class GoogleAuthProvider:
    def __init__(self, client_secrets_file: str, scopes: list[str], token_file="token.json"):
        self.client_secrets_file = client_secrets_file
        self.scopes = scopes
        self.token_file = Path(token_file)
        self.credentials: Credentials | None = None

    def authenticate(self):
        """Run OAuth flow and save token."""
        flow = InstalledAppFlow.from_client_secrets_file(self.client_secrets_file, self.scopes)
        creds = flow.run_local_server(port=0)
        self.credentials = creds
        self.token_file.write_text(creds.to_json())
        return creds

    def get_credentials(self) -> Credentials:
        """Return valid credentials, authenticate if needed."""
        if self.credentials and self.credentials.valid:
            return self.credentials

        if self.token_file.exists():
            self.credentials = Credentials.from_authorized_user_file(self.token_file, self.scopes)

        # Refresh if expired
        if self.credentials and self.credentials.expired and self.credentials.refresh_token:
            self.credentials.refresh(Request())
            self.token_file.write_text(self.credentials.to_json())

        if not self.credentials or not self.credentials.valid:
            self.credentials = self.authenticate()

        return self.credentials

    def download_file(self, file_id: str, destination: str) -> Path:
        """Download a file from Google Drive."""
        creds = self.get_credentials()
        service = build("drive", "v3", credentials=creds)
        dest_path = Path(destination)

        request = service.files().get_media(fileId=file_id)
        with io.FileIO(dest_path, "wb") as fh:
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                if status:
                    print(f"Download {int(status.progress() * 100)}%")
        return dest_path

    def convert_to_csv(self, input_file: Path, output_file: Path):
        """Convert VCF (vCard) file into CSV with multiple emails/phones supported."""
        rows = []
        contact = {}

        for line in input_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue

            if line.startswith("BEGIN:VCARD"):
                contact = {key: "" for key in CSV_HEADERS}
                contact["_emails"] = []
                contact["_phones"] = []
                contact["_types"] = []

            elif line.startswith("FN:"):
                contact["full_name"] = line[3:]

            elif line.startswith("EMAIL"):
                email = line.split(":", 1)[1]
                contact["_emails"].append(email)

            elif line.startswith("TEL"):
                number = line.split(":", 1)[1]
                contact["_phones"].append(number)
                if "TYPE=" in line:
                    type_part = line.split("TYPE=")[1].split(":")[0]
                    contact["_types"].append(type_part)
                else:
                    contact["_types"].append("")

            elif line.startswith("ORG:"):
                contact["business_name"] = line[4:]

            elif line.startswith("ADR"):
                adr_parts = line.split(":")[1].split(";")
                if len(adr_parts) >= 7:
                    contact["street_address"] = adr_parts[2]
                    contact["city"] = adr_parts[3]
                    contact["state"] = adr_parts[4]
                    contact["postal_code"] = adr_parts[5]
                    contact["country"] = adr_parts[6]

            elif line.startswith("BDAY:"):
                contact["date_of_birth"] = line[5:]

            elif line.startswith("END:VCARD"):
                # Join multiple emails/phones/types
                contact["email"] = ",".join(contact.get("_emails", []))
                contact["phone"] = ",".join(contact.get("_phones", []))
                contact["tags"] ='phone-conatct'
                contact["contact_type"] = ",".join(contact.get("_types", []))

                # Remove helper keys
                contact.pop("_emails", None)
                contact.pop("_phones", None)
                contact.pop("_types", None)

                # Add row
                row = [contact.get(h, "") for h in CSV_HEADERS]
                rows.append(row)

        # Write CSV
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)
            writer.writerows(rows)

        print(f"CSV saved at {output_file}")


if __name__ == "__main__":
    SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
    gauth = GoogleAuthProvider(
        "E:\\AIdevloper-classnotes\\Python\\modules\\cli\\credentials.json", SCOPES
    )

    creds = gauth.get_credentials()
    print("Access token:", creds.token)

    # Step 1: download VCF file
    text_file = gauth.download_file("1UhG7GGXal8KMHcwu85jPKtl3Y6Ignl0O", "downloaded_file.vcf")

    # Step 2: convert VCF to CSV
    gauth.convert_to_csv(text_file, Path("contacts.csv"))
