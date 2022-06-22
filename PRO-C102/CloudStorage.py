import dropbox
class TranferData:

    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, src, dst):
        dbx = dropbox.Dropbox(self.access_token)

        with open(src, 'rb') as f:
            dbx.files_upload(f.read(), dst)

    