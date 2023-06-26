from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import requests
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

    def get_file_drive(self,file_name):
        output_file = os.path.join("./downloads/", file_name)

        if not (os.path.isfile(output_file)):
            files = client.ListFile({'q': f"'{self.get_folder()}' in parents and trashed=false and title in '{file_name}'"}).GetList()
            if files:
                file_id = files[0]['id']
                file_url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media"
                
                response = requests.get(
                    file_url, stream=True
                )
                
                with open(output_file, "wb") as output:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            output.write(chunk)
                
                return output_file
            else:
                return False
        
    def upload_file(self,name,file):
        send_file = client.CreateFile({"mimeType": "audio/wav",'title': name,'parents':[{'id':self.get_folder()}]})
        send_file.content = io.BytesIO(file.file.read())
        send_file.Upload()

        if not os.path.exists("./downloads"):
            os.makedirs("./downloads")
        
        with open("./downloads/" + file.name, "wb+") as destination:  
            for chunk in file.chunks():  
                destination.write(chunk)

        return True
    
    def delete_file(self,file_name):
        output_file = os.path.join("./downloads/", file_name)
        if (os.path.isfile(output_file)):
            os.remove(output_file)

        files = client.ListFile({'q': f"'{self.get_folder()}' in parents and trashed=false and title in '{file_name}'"}).GetList()
        if files:
            file_id = files[0]['id']
            file = client.CreateFile({'id': file_id})
            file.Delete()