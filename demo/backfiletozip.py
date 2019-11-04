import os,zipfile

###
def backupToZip(folder):
    folder = os.path.abspath(folder)
    num = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(num) +'.zip'
        if not os.path.exists(zipFilename):
            break
        num += 1

    #create zip file.
    backupZipfile = zipfile.ZipFile(zipFilename, 'w')
    for foldername, subfolders, filenames in os.walk(folder):
        # write current folder to zip file.
        backupZipfile.write(foldername)
        # compress the files in each folder
        for filename in filenames:
            # don't compress backup zip file
            if filename.startswith(os.path.basename(folder+'_')) and filename.endswith('.zip'):
                continue
            backupZipfile.write(os.path.join(foldername, filename))

    backupZipfile.close()

if __name__ == '__main__':
    backupToZip('D:\\tmp')
