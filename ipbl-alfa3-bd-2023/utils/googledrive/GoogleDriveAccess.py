from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import io
import os

gauth = GoogleAuth(settings_file=os.path.abspath("utils/googledrive/main_settings.yaml"))
client = GoogleDrive(gauth)

class GoogleDriveAccess:
    def __init__(self) -> None:
        super().__init__()
    
    def get_folder(self):
        folder_id = ''
        folder_list = client.ListFile({"q": "mimeType='application/vnd.google-apps.folder' and trashed=false and 'root' in parents"}).GetList()
        for f in folder_list:
            if f['title']=='alfa3BD-audios':
                folder_id = f['id']
                return folder_id

       

    def get_file(self,file_name):
        file = client.ListFile({'q': f"'{self.get_folder()}' in parents and trashed=false and title in '{file_name}'"}).GetList()
        client.GetContentFile(file[0], mimetype='text/html')

        
    def upload_file(self,name,file):

        send_file = client.CreateFile({"mimeType": "audio/wav",'title': name,'parents':[{'id':self.get_folder()}]})
        send_file.content = io.BytesIO(file.file.getvalue())
        send_file.Upload()

        return True