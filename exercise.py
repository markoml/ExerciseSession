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
for infile in glob.glob(os.path.join(path, '*.*')):
	print "current file is: " + infile 
	f=open(infile,'r')
	lines = f.readlines()
	f.close()
	for i in range(len(lines)):
		print filestring(lines[i])
		print replace(lines[i]) 
         
