#Code to convert given string into form appropriate for google search
#Author: Abhinav Dhere
fPath="/home/abhinav/GoogleString" #read path
wPath="/home/abhinav/temp"	   #write path
def getString(fPath):
    '''
    Reads string from file
    '''
    file=open(fPath,'r')
    inString=file.read()
    return inString

def modString():
    '''
    Convert the string to appropriate form
    '''
    inString=getString(fPath)
    inString=inString[:-1]#to remove newlines
    inStringL=inString.split()
    inString=inStringL[0]
    i=1
    while i<len(inStringL):
        inString+='+'+inStringL[i]
        i+=1
    return inString

inString= modString()
wFile=open(wPath,'w')#write to file
wFile.write(inString)
wFile.close()
