import shutil
import os
import re
def copyAndRename(bookName):
    shutil.copy('example.html', bookName + ".html")
    return bookName + ".html"

def replaceContent(title, actualVerses):
    toSub = ['title', 'actualVerses']
    substitutions = [title, actualVerses]
    for i in range(2):
        with open(title + ".html", 'r+') as f:
            text = f.read()
            text = re.sub(toSub[i], substitutions, text)
            f.seek(0)
            f.write(text)
            f.truncate()

bookName = copyAndRename()
replaceContent(bookName, versesFromFiles)