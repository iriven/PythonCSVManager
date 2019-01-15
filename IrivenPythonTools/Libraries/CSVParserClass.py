#coding: utf-8
import sys
import os
import csv
import inspect
class Iriven_CSVParser(object):
    ERROR_INVALID_NAME = 123

    def __init__(self, csvFile, delimiter=',', quoting=csv.QUOTE_NONE):
        self.csvFile = csvFile
        self._Data = []
        self.delimiter = delimiter
        self.quoting = quoting
        
    def getNumRows(self):
        return self._Data.__len__()
    
    def __isValidPathname(self, pathname: str)->bool:
        try:
            if not isinstance(pathname, str) or not pathname:
                return False
            _, pathname = os.path.splitdrive(pathname)
            root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
                if sys.platform == 'win32' else os.path.sep
            assert os.path.isdir(root_dirname)
            root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep
            for pathname_part in pathname.split(os.path.sep):
                try:
                    os.lstat(root_dirname + pathname_part)
                except OSError as exc:
                    if hasattr(exc, 'winerror'):
                        if exc.winerror == self.ERROR_INVALID_NAME:
                            return False
                    elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                        return False
        except TypeError as exc:
            return False
        else:
            return True

    def load(self, csvFile, delimiter=',', quoting=csv.QUOTE_NONE):
        try:
            if self.__isValidPathname(csvFile) and os.path.exists(csvFile):
                self.__init__(csvFile, delimiter, quoting)
                self.prepare()
        except IOError  as e:
            sys.exit('I/O error(%s): %s' % (e.errno, e.strerror))
        
    def prepare(self):
        try:
            csv.register_dialect('readingdialect', delimiter=self.delimiter, quoting=self.quoting)
            with open(self.csvFile,'r') as f:
                for row in csv.reader(f, 'readingdialect'):
                    if row.__len__():
                        self._Data.append(row)
                return self._Data
        except IOError  as e:
            sys.exit('I/O error(%s): %s' % (e.errno, e.strerror))
            
    def searchRows(self, values=None, unique = True):
        out = []
        if values:
            if type(values).__name__ not in ('list', 'tuple'):
                values = [values]
            if self.getNumRows():
                for i in range(self.getNumRows()):
                    for j in values:
                        if j in self._Data[i]:
                            if not unique:
                                out.append(self._Data[i])
                            else:     
                                if self._Data[i] not in out:
                                    out.append(self._Data[i]) 
        return out

    def setDelimiter(self, delim):
        self.delimiter = delim

    def traverse(self):
        return self._Data


if __name__ == "__main__":
    sys.exit(main())
