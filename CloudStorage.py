import dropbox

class TransferData:
  def __init__(self, access_token):
    self.access_token = access_token
  
  def upload_file(self, file_from, file_to):
    dbx = dropbox.Dropbox(self.access_token)
    with open(file_from, 'rb') as f:
      dbx.files_upload(f.read(), file_to)

def main():
  access_token = 'MCkARkfOUaMAAAAAAAAAAfJFax80hVeYO2Wleuak9yi-dfuBYnfMrzX82QN8YXA_'
  transferData = TransferData(access_token)

  file_from = input("Enter the path of the file you want to transfer: ")
  file_to = input("Enter the full path to send to dropbox: ")

  transferData.upload_file(file_from, file_to)
  print("File has been moved.")

main()