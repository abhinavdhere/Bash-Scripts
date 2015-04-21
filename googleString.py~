fPath="/home/abhinav/GoogleString"
wPath="/home/abhinav/temp"
def getString(fPath):
    file=open(fPath,'r')
    inString=file.read()
    return inString

def modString():
    inString=getString(fPath)
    inString=inString[:-1]
    inStringL=inString.split()
    inString=inStringL[0]
    i=1
    while i<len(inStringL):
        inString+='+'+inStringL[i]
        i+=1
    return inString

inString= modString()
wFile=open(wPath,'w')
wFile.write(inString)
wFile.close()
