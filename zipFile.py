import zipfile
# from pathlib import Path

newZip = zipfile.ZipFile('new.zip', 'w')

newZip.write('example.txt', compress_type = zipfile.ZIP_DEFLATED)
newZip.close()