import os,re,shutil

# Create a regex that matches files with the American date format.
# dataPattern = re.compile(r"""^(.*?)
# ((0|1)?\d)-
# ((0|1|2|3)?\d)-
# ((19|20|\d)\d\d)
# (.*?)$""", re.VERBOSE)
#
# # Loop over the files in the working directory.
# filelist = os.listdir('.')
# for file in filelist:
#     mo = dataPattern.search(file)
#     if mo:
#         res = mo.groups()
#         newFilename= '{}{}-{}-{}{}'.format(res[0],res[3],res[1],res[5],res[-1])
#         shutil.copy(file, 'new/'+newFilename)

# Create a regex that matches files with the American date format.
dataPattern = re.compile(r"""^(?P<beforedata>.*?)
(?P<month>(0|1)?\d)-
(?P<day>(0|1|2|3)?\d)-
(?P<year>(19|20|\d)\d\d)
(?P<afterdata>.*?)$""", re.VERBOSE)

# Loop over the files in the working directory.
filelist = os.listdir('.')
for file in filelist:
    mo = dataPattern.search(file)
    newFilename = re.sub(dataPattern, '\g<beforedata>\g<day>-\g<month>-\g<year>\g<afterdata>', file)
    if mo:
        print(newFilename)
        shutil.copy(file, 'new/'+newFilename)
