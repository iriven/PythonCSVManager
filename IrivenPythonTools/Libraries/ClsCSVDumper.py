#coding: utf-8
import sys
import os
import csv
class Iriven_CSVDumper(object):
    ERROR_INVALID_NAME = 123
    '''
    csv.QUOTE_ALL - Quote everything, regardless of type.
    csv.QUOTE_MINIMAL - Quote fields with special characters
    csv.QUOTE_NONNUMERIC - Quote all fields that are not integers or floats
    csv.QUOTE_NONE - Do not quote anything on output
    '''
    def __init__(self, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n'):
        self.csvFile = './fileCreated.csv'
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.quoting = quoting
        self.lineterminator = lineterminator
    
    def save(self, datas, append = False):
        try:
            if type(datas).__name__ not in ('list', 'tuple'):
                datas = [datas]
            csv.register_dialect('writingdialect', delimiter=self.delimiter, quotechar=self.quotechar, quoting=self.quoting, lineterminator=self.lineterminator)
            with open(self.csvFile, 'w') as f:
                writer = csv.writer(f, 'writingdialect')
                for row in datas:
                    writer.writerow(row)
        except IOError  as e:
            sys.exit('I/O error(%s): %s' % (e.errno, e.strerror))
    
    def setDestination(self, csvFile):
        try:
            if self.isValidPathname(csvFile):
                self.csvFile = csvFile
        except IOError  as e:
            sys.exit('I/O error(%s): %s' % (e.errno, e.strerror))
        
    
    def isValidPathname(self, pathname: str)->bool:
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


if __name__ == "__main__":
    sys.exit(main())
