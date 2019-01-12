#coding: utf-8
import sys 
import os
IrivenPackageLocation = "../../IrivenPythonTools"
sys.path.append(os.path.abspath(IrivenPackageLocation))
from IrivenBootstrap import *
if __name__ == "__main__":
    fileloader = Iriven_CSVParser("./testFile.csv")
    '''
    to test with a non standard delimiter, just call the setDelimiter() method:
    fileloader = Iriven_CSVParser("./nonStd_testFile.csv")
    fileloader.setDelimiter(":")
    '''
    fileloader.parse()
    print(fileloader.getNumRows())
    print(fileloader.fetchRows(("osadmin" , "root")))
    print(fileloader.getRows())
    CSVParserProp = Iriven_ClassInfos(fileloader)
    print(CSVParserProp.GetMethods())

    filecreator = Iriven_CSVDumper()
    filecreator.setDestination('./fileCreated1.csv')
    filecreator.save(fileloader.fetchRows(("osadmin" , "root")))
    s = "----------------------------------------------------------" + eol
    for row in fileloader.fetchRows(("osadmin" , "admplat")):
        s += "Server : " + row[0] + eol
        s += "User : " + row[1] + eol
        s += "Password : " + row[2] + eol
        s += "----------------------------------------------------------" + eol
        print(s)
