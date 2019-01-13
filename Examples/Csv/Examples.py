#coding: utf-8
import sys 
import os
IrivenPackageLocation = "../../IrivenPythonTools"
sys.path.append(os.path.abspath(IrivenPackageLocation))
from IrivenPyBootstrap import *
if __name__ == "__main__":
    fileloader = Iriven_CSVParser("./testFile.csv")
    '''
    to test with a non standard delimiter, just call the setDelimiter() method:
    fileloader = Iriven_CSVParser("./nonStd_testFile.csv")
    fileloader.setDelimiter(":")
    '''
    fileloader.parse()
    print(fileloader.getNumRows())
    print(fileloader.fetchRows(("user1" , "admin","staff")))
    print(fileloader.getRows())
    
    '''
    the Reflection Class
    '''
    CSVParserinfos = Iriven_ReflectionClass(fileloader)
    print(CSVParserinfos.GetMethods())
    
    '''
    the Dumper Class
    '''
    filecreator = Iriven_CSVDumper()
    filecreator.setDestination('./CreatedFile.csv')
    filecreator.save(fileloader.fetchRows(("admin" , "root")))
    s = "----------------------------------------------------------" + eol
    for row in fileloader.fetchRows(("admin","staff")):
        s += "Server : " + row[0] + eol
        s += "User : " + row[1] + eol
        s += "Password : " + row[2] + eol
        s += "----------------------------------------------------------" + eol
        print(s)
