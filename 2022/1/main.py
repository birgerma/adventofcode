# importing sys
import sys
 
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '../')
 
from common.io import *

if __name__=='__main__':
    print("Hello world!")
