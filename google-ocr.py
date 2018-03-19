import glob
import os
import re
import sys

script, file = sys.argv
print file
#textfiles= []
#for filename in glob.glob('*.txt'):
#	files.append(filename.split(".")[0]

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

files = []
for filename in glob.glob('*.jpg'):
  files.append(filename)

#textfiles=[]
#for filename in glob.glob('.txt'):
#	textfiles.append(filename)
#
files.sort(key=alphanum_key)
#textfiles.sort(key=alphanum_key)
#print files
for image in files:
	#im_file_id=image.split(".")[0]
	#txt_file_id=text.split(".")[0]
	#if im_file_id == txt_file_id:
	#	continue;
	#
	print "uploading " + image
	command = "gdput.py -t ocr  " + image + " > result.log"
	print "running " + command
	os.system(command)
	resultfile = open("result.log","r").readlines()
	for line in resultfile:
		if "id:" in line:
			fileid = line.split(":")[1].strip()
			filename = image.split(".")[0] + ".txt"
			get_command = "gdget.py -f txt -s " + filename + " " + fileid
			print "running "+ get_command
			os.system(get_command)
			os.system("gdrm.py " + fileid)


#print "Merging all text files into ocr-result.txt"
#print "zipping all files"
#os.system("zip -q " + file + ".zip *.txt")
#files2 = glob.glob('*.txt')
#files2.sort(key=alphanum_key)
#with open('ocr-result.txt', 'w' ) as result:
#    for textfile in files2:
#        for line in open( textfile, 'r' ):
#            result.write( line )
#os.system("touch " + file)
os.system("cat `ls -v *.txt` >> " + file + ".md")
print "Done"
