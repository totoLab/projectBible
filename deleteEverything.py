import shutil
import os
import re

def deleteFromTo(dir, path):
    for j in range(1, len(dir)+1):
        selectedDir = dir[j-1]
        entirePath = "{}{}".format(path, selectedDir)
        print(selectedDir)
        for i in range(len([name for name in os.listdir(entirePath)])): #loop for number of files
            processedFile = "{}/{}.txt".format(entirePath, i+1)
            with open('{}/verses{}.txt'.format(entirePath, i+1), 'w') as fp: 
                pass
            newFile = '{}/{}'.format(entirePath, ('verses{}.txt'.format(i+1)))
            removeLines(processedFile, 'verse', newFile)
            removeOldFiles(entirePath, processedFile)
            removeHtmlJunk(newFile)


def removeLines(logfile, word, outfile):
    with open(logfile) as f_in:
        lines = (l for l in f_in if word in l)
        with open(outfile, 'w') as f_out:
            f_out.writelines(lines)

def removeOldFiles(path, oldFile):
    os.remove("{}".format(oldFile))

#TODO
def removeHtmlJunk(fileToClean):
    print("remove html junk")

def copyAndRename(path, bookName):
    shutil.copy(path, bookName + ".html")
    print("Renamed {}".format(bookName + ".html"))
    return bookName + ".html"

#TODO test, copied from stackoverflow
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

#TODO
def copyVersesToFinalFiles(bookName, verses):
    print("Copied {}".format(bookName))

path = "/home/antonio/Documents/VScode/webDev/testProjectBible/bibbiaHtmlTest/"
path2 = "/home/antonio/Documents/VScode/webDev/testProjectBible/example.html"
arrayDir = ['1.Genesi','2.Esodo','3.Levitico','4.Numeri','5.Deuteronomio','6.Giosuè','7.Giudici','8.Rut','9.Samuele1','10.Samuele2','11.Re1','12.Re2','13.Cronache1','14.Cronache2','15.Esdra','16.Neemia','17.Ester','18.Giobbe','19.Salmi','20.Proverbi','21.Ecclesiaste','22.CanticodeiCantici','23.Isaia','24.Geremia','25.Lamentazioni','26.Ezechiele','27.Daniele','28.Osea','29.Gioele','30.Amos','31.Abdia','32.Giona','33.Michea','34.Naum','35.Abacuc','36.Sofonia','37.Aggeo','38.Zaccaria','39.Malachia','40.Matteo','41.Marco','42.Luca','43.Giovanni','44.Atti','45.Romani','46.Corinzi1','47.Corinzi2','48.Galati','49.Efesini','50.Filippesi','51.Colossesi1','52.Colossesi2','53.Tessalonicesi1','54.Tessalonicesi2','55.Timoteo','56.Tito','57.Filemone','58.Ebrei','59.Giacomo','60.Pietro1','61.Pietro2','62.Giovanni1','63.Giovanni2','64.Giovanni3','65.Giuda','66.Apocalisse']
def mainFunc():
    deleteFromTo(arrayDir, path)
    #for i in range(len(arrayDir)):
        #bookName = copyAndRename(path2, arrayDir[i]) #copy example.html and rename with a bookname
        #replaceContent(bookName, versesFromFiles)


mainFunc()