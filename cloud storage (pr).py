import os
import dropbox
from dropbox.files import WriteMode 


class TransferData:
    def __init__(self, access_token): 
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox (self.access_token)


        for root, dirs, files in os.walk(file_from):

            for filename in files:
             
                 local_path = os.path.join(root, filename)

                 relative_path = os.path.relpath (local_path, file_from) 
                 dropbox_path = os.path.join(file_to, relative_path)

                 with open(local_path, 'rb') as f:
                     dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
def main():
    access_token = 'sl.BdSsEKFM6iVZ1F2yrQ18e2fLZOOmSOBSUmAuvOugJJY2EyBlPqscyYI7ABqDmwgN4VySHhlKPoghHwb-QLvAOwP4hgKkd1kHx_MHR9tY6z0DKppYb8pwhFzlb-PNHT3xM_RCotU'
    transferData = TransferData(access_token)

    file_from = str(input('Enter the folder path:-'))
    file_to = input('Enter full path:-')

    transfer_data.upload_file(file_from,file_to)
    print('file has been transfer')
    
main()
