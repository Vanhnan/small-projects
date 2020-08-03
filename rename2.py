import os
path = "D:\\movies\\witcher\\The.Witcher.S01.COMPLETE.720p.NF.WEBRip.x264-GalaxyTV[TGx]"
os.chdir(path)

for i in os.listdir():
	os.rename(path+"\\"+i, path+"\\"+i+".mkv")
