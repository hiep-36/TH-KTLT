print("Le Hoa Hiep")
print("235752021610073")
import sys
import os
def file_read_from_tail(fname, lines):
    bufsize = 8192  
    fsize = os.stat(fname).st_size  
    iter = 0
    data = [] 
    with open(fname, 'r') as f:
        if bufsize > fsize:
            bufsize = fsize  
        while True:
            iter += 1
            f.seek(fsize - bufsize * iter)
            chunk = f.readlines()  
            data.extend(chunk)  
            
            if len(data) >= lines or f.tell() == 0:  
                  print(''.join(data[-lines:]))
                  break
file_read_from_tail('test.txt', 2)
