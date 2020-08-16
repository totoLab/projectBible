import re

def removeHtmlJunk(fn):
    with open(fn, 'r+') as fo: 
        for line in fo:
            text = fo.read()
            text = re.sub('<[^>]+>', '', line)
            fo.write(text)
            print(text)

removeHtmlJunk("/home/antonio/Documents/VScode/webDev/testProjectBible/bibbiaHtmlTest/1.Genesi/verses1.txt")

#!what a piece of s%&* i can't do nothing i'm stupid