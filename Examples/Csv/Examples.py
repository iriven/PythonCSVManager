#coding: utf-8
import sys 
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
RootDirectory = os.path.dirname(os.path.dirname(currentdir))
IrivenPackageLocation = os.path.join(RootDirectory , "IrivenPythonTools")
sys.path.append(os.path.abspath(IrivenPackageLocation))

from IrivenPyBootstrap import *

if __name__ == "__main__":
    ''' 
    get the csv file full path 
    '''
    csvfilePath = os.path.join(currentdir , "Inputs",  "testFile.csv") 
    ParserObject = Iriven_CSVParser(csvfilePath)
    '''
    to test with a non standard delimiter, just call the setDelimiter() method:
    ParserObject = Iriven_CSVParser(os.path.join(currentdir , "nonStd_testFile.csv"))
    ParserObject.setDelimiter(":")
    '''
    ParserObject.prepare()
    ParserObject.load(os.path.join(currentdir ,'Inputs', 'nonStd_testFile.csv'),':')
    print(ParserObject.getNumRows())
    print(ParserObject.searchRows(("user1" , "admin")))
    print(ParserObject.traverse())
    
    '''
    the Reflection Class
    '''
    CSVParserinfos = Iriven_ReflectionClass(ParserObject)
    print(CSVParserinfos.GetMethods())
    
    '''
    the Dumper Class
    '''
    DumperObject = Iriven_CSVDumper()
    destFile = os.path.join(currentdir , 'Outputs',  'CreatedFile.csv')
    DumperObject.setDestination(destFile)
    DumperObject.save(ParserObject.searchRows(("admin" , "root")))
    s = "----------------------------------------------------------" + EOL
    for row in ParserObject.searchRows(("admin","staff")):
        s += "Server : " + row[0] + EOL
        s += "User : " + row[1] + EOL
        s += "Password : " + row[3] + EOL
        s += "HomeDir : " + row[2] + EOL
        s += "----------------------------------------------------------" + EOL
        print(s)
