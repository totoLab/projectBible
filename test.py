import re

def removeHtmlJunk(logfile, outfile):
    with open (logfile, 'r' ) as f:
        content = f.read()
        content_new = re.sub('<[^>]+>', '', content, flags = re.M)
        with open(outfile, 'w') as out:
            out.write(content_new)


path = "/home/antonio/Documents/VScode/webDev/testProjectBible/bibbiaHtmlTest/1.Genesi/"
with open('{}/newFile.txt'.format(path), 'w') as fp: 
    pass

removeHtmlJunk(path + "verses1.txt", path + "newFile.txt")
#!what a piece of s%&* i can't do nothing i'm stupid