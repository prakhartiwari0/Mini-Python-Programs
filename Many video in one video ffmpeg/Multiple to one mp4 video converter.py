import os

l = os.listdir()
l.remove("Multiple to one mp4 video converter.py")


##print(l)

t = ""
i = 0
for a in l:
    c = f"file '{l[i]}'\n"
    t = t+c
    i = i+1


file = open("list.txt", "w")
file.write(t)
file.close()

file2 = open("Merger.bat", "w")
file2.write("ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4")
file2.close()

os.startfile("Merger.bat")
    
