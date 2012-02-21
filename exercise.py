import os
import glob  
       
def  files(path):
   	listing = os.listdir(path)
        return listing
def  filestring(line):
     search="N"
     a=line.find(search)
     if a>=0:
	 b=True
     else:
	 b=False
     return b;
def  replace(line):
     nline = line.replace("N","M")
     return nline;		
path='cleandata'
filelist=files(path)
for infile in filelist:
	print "current file is: " + infile 
	for inline in infile:
		print filestring(inline)
		print replace(inline) 
         
