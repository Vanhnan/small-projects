import os
path = "D:\\movies\\witcher\\The.Witcher.S01.COMPLETE.720p.NF.WEBRip.x264-GalaxyTV[TGx]"
os.chdir(path)

for i in os.listdir():
        name, extension = os.path.splitext(i)
        label = name.split(".")[2][:-2]
        print(label)
        os.rename(path+"\\"+i, path+"\\"+label)
        
