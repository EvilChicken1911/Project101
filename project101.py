import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken
    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accesstoken)
        for root, dirs, files in os.walk(fileFrom):
            for fileName in files:
                localPath = os.path.join(root, fileName)
                relatedPath = os.path.relPath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relatedPath)
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode = WriteMode('overwrite'))

def main():
    accesstoken = "sl.A5-ZKYKtOCuLfIUbptoYU4yARQXGwbFdiYrDrrUc6KOZWOcMVHe0r8yhMBb9KJwlxmdu9op_uEytaHXkcC3_pURfIfU9bH_2BvquL3WMpZzzoWBWTpFyIMpDqiefPCJ5Y9N-mxU"
    transferdata = TransferData(accesstoken)
    fileFrom = input("Enter the file that you want to transfer: ")
    fileTo = input("Enter the destination: ")
    transferdata.uploadFile(fileFrom, fileTo)
    print("File has been moved")

main()