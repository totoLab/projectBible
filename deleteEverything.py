import shutil
import os
import re
import fileinput

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
            removeOldFiles(processedFile)
            removeHtmlJunk(newFile, "{}/load1{}.txt".format(entirePath, i+1), ['<[^>]+>', ''])
            removeHtmlJunk("{}/load1{}.txt".format(entirePath, i+1), "{}/load2{}.txt".format(entirePath, i+1), ['((?<=\d)\s+|\s+$)', ' ']) #it shows errors but has none
            removeHtmlJunk("{}/load2{}.txt".format(entirePath, i+1), "{}/load3{}.txt".format(entirePath, i+1), ['$', '</section>'])
            removeHtmlJunk("{}/load3{}.txt".format(entirePath, i+1), "{}/chapter{}.txt".format(entirePath, i+1), ['^', '    <section>'])


def removeLines(logfile, word, outfile):
    with open(logfile) as f_in:
        lines = (l for l in f_in if word in l)
        with open(outfile, 'w') as f_out:
            f_out.writelines(lines)

def removeOldFiles(oldFile):
    os.remove("{}".format(oldFile))

def removeHtmlJunk(fileToModify, outfile, regex):
    with open (fileToModify, 'r' ) as f:
        content = f.read()
        content_new = re.sub(regex[0], regex[1], content, flags = re.M)
        with open(outfile, 'w') as out:
            out.write(content_new)

    removeOldFiles(fileToModify)
        

def copyAndRenamePattern(path, bookName):
    shutil.copy(path, bookName + ".html")
    print("Renamed {}".format(bookName + ".html"))
    return bookName

#TODO test, copied from stackoverflow
def replaceContent(path, bookName, bookIndex):
    listOfFiles = []
    titleOfTheDoc = ['bookTitle', bookName]
    removeHtmlJunk("{}{}.html".format(path, bookName), "{}firsttest{}.html".format(path, bookName), titleOfTheDoc) #add in this case
    for i in range(len([name for name in os.listdir("{}{}".format(path1, bookName))])):
        listOfFiles.append("{}/{}{}.txt".format(path1 + bookName, "chapter", i+1))
        
    joinFiles(listOfFiles, bookIndex)

def joinFiles(filesToJoin, bookIndex):
    #read content of every file, join together in a string
    #(add dividers between files - chapters) and substitute to the string actual verses
    with open('{}.txt'.format(arrayDir[bookIndex]), 'w') as outfile:
        outfile.write("<section>{}</section>\n\n".format(arrayDir[bookIndex]))
        for names in filesToJoin: 
            with open(names) as infile:
                outfile.write("<section>{} Capitolo {}\n    <section></section>\n".format(arrayDir[bookIndex], filesToJoin.index(names)+1))
                outfile.write(infile.read()) 
                outfile.write("\n</section>\n")

            outfile.write("\n")

#TODO
def copyVersesToFinalFiles(bookName, verses):
    print("Copied {}".format(bookName))

path1 = "/home/antonio/Documents/VScode/webDev/testProjectBible/bibbiaHtmlTest/"
path2 = "/home/antonio/Documents/VScode/webDev/testProjectBible/example.html"
path3 = "/home/antonio/Documents/VScode/webDev/newProjectBible/"
arrayDir = ['1.Genesi','2.Esodo','3.Levitico','4.Numeri','5.Deuteronomio','6.Giosuè','7.Giudici','8.Rut','9.Samuele1','10.Samuele2','11.Re1','12.Re2','13.Cronache1','14.Cronache2','15.Esdra','16.Neemia','17.Ester','18.Giobbe','19.Salmi','20.Proverbi','21.Ecclesiaste','22.CanticodeiCantici','23.Isaia','24.Geremia','25.Lamentazioni','26.Ezechiele','27.Daniele','28.Osea','29.Gioele','30.Amos','31.Abdia','32.Giona','33.Michea','34.Naum','35.Abacuc','36.Sofonia','37.Aggeo','38.Zaccaria','39.Malachia','40.Matteo','41.Marco','42.Luca','43.Giovanni','44.Atti','45.Romani','46.Corinzi1','47.Corinzi2','48.Galati','49.Efesini','50.Filippesi','51.Colossesi1','52.Colossesi2','53.Tessalonicesi1','54.Tessalonicesi2','55.Timoteo','56.Tito','57.Filemone','58.Ebrei','59.Giacomo','60.Pietro1','61.Pietro2','62.Giovanni1','63.Giovanni2','64.Giovanni3','65.Giuda','66.Apocalisse']
def mainFunc():
    deleteFromTo(arrayDir, path1)
    for i in range(1):#len(arrayDir)):
        bookName = copyAndRenamePattern(path2, arrayDir[i]) #copy example.html and rename with a bookname
        replaceContent(path3, bookName, i)


mainFunc()
