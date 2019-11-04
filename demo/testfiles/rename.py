import os,re,shutil

# Create a regex that matches files with the American date format.
dataPattern = re.compile(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20|\d)\d\d)
(.*?)$""", re.VERBOSE)


