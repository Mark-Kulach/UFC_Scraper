from common import * 

SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]

creds = None
  
def get_service():
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
      
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  global service
  service = build("drive", "v3", credentials=creds)