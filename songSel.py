#Selects a random song from a list of songs
#To be used by the bash sript to select a random song
#Author: Abhinav Dhere

import random

def getSongList():
	songList=[]
	inFile=open("/home/abhinav/songList",'r')
	for line in inFile:
		line=line[:-1]
		if line[-3:]==".rm" or line[-3:]=="mp3":
			songList.append(line)
	return songList

def selSong():
	songList=getSongList()
	song=random.choice(songList)
	return song

def giveSong():
	song=selSong()
	outFile=open("/home/abhinav/temp",'w')
	outFile.write(song)
	outFile.close()

giveSong()
