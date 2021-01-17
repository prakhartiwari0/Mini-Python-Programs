import os

file1 = input("Name of file 1 -  ")
file2 = input("Name of file 2 -  ")
file3 = input("Name of file 3 -  ")
file4 = input("Name of file 4 -  ")
file5 = input("Name of file 5 -  ")
file6 = input("Name of file 6 -  ")
file7 = input("Name of file 7 -  ")
file8 = input("Name of file 8 -  ")
file9 = input("Name of file 9 -  ")
file10 = input("Name of file 10 -  ")

if ".mp3" in file1:
    ext = "_.mp3"
    new_name_file1 = file1.replace(".mp3", "")
elif ".mp4" in file1:
    ext = "_.mp4"
    new_name_file1 = file1.replace(".mp4", "")
elif ".wmv" in file1:
    ext = "_.mp4"
    new_name_file1 = file1.replace(".wmv", "")
new_name_file1 = new_name_file1+ext

if ".mp3" in file2:
    ext = "_.mp3"
    new_name_file2 = file2.replace(".mp3", "")
elif ".mp4" in file2:
    ext = "_.mp4"
    new_name_file2 = file2.replace(".mp4", "")
elif ".wmv" in file2:
    ext = "_.mp4"
    new_name_file2 = file2.replace(".wmv", "")
new_name_file2 = new_name_file2+ext

if ".mp3" in file3:
    ext = "_.mp3"
    new_name_file3 = file3.replace(".mp3", "")
elif ".mp4" in file3:
    ext = "_.mp4"
    new_name_file3 = file3.replace(".mp4", "")
elif ".wmv" in file3:
    ext = "_.mp4"
    new_name_file3 = file3.replace(".wmv", "")
new_name_file3 = new_name_file3+ext

if ".mp3" in file4:
    ext = "_.mp3"
    new_name_file4 = file4.replace(".mp3", "")
elif ".mp4" in file4:
    ext = "_.mp4"
    new_name_file4 = file4.replace(".mp4", "")
elif ".wmv" in file4:
    ext = "_.mp4"
    new_name_file4 = file4.replace(".wmv", "")
new_name_file4 = new_name_file4+ext

if ".mp3" in file5:
    ext = "_.mp3"
    new_name_file5 = file5.replace(".mp3", "")
elif ".mp4" in file5:
    ext = "_.mp4"
    new_name_file5 = file5.replace(".mp4", "")
elif ".wmv" in file5:
    ext = "_.mp4"
    new_name_file5 = file5.replace(".wmv", "")
new_name_file5 = new_name_file5+ext

if ".mp3" in file6:
    ext = "_.mp3"
    new_name_file6 = file6.replace(".mp3", "")
elif ".mp4" in file6:
    ext = "_.mp4"
    new_name_file6 = file6.replace(".mp4", "")
elif ".wmv" in file6:
    ext = "_.mp4"
    new_name_file6 = file6.replace(".wmv", "")
new_name_file6 = new_name_file6+ext

if ".mp3" in file7:
    ext = "_.mp3"
    new_name_file7 = file7.replace(".mp3", "")
elif ".mp4" in file7:
    ext = "_.mp4"
    new_name_file7 = file7.replace(".mp4", "")
elif ".wmv" in file7:
    ext = "_.mp4"
    new_name_file7 = file7.replace(".wmv", "")
new_name_file7 = new_name_file7+ext

if ".mp3" in file8:
    ext = "_.mp3"
    new_name_file8 = file8.replace(".mp3", "")
elif ".mp4" in file8:
    ext = "_.mp4"
    new_name_file8 = file8.replace(".mp4", "")
elif ".wmv" in file8:
    ext = "_.mp4"
    new_name_file8 = file8.replace(".wmv", "")
new_name_file8 = new_name_file8+ext

if ".mp3" in file9:
    ext = "_.mp3"
    new_name_file9 = file9.replace(".mp3", "")
elif ".mp4" in file9:
    ext = "_.mp4"
    new_name_file9 = file9.replace(".mp4", "")
elif ".wmv" in file9:
    ext = "_.mp4"
    new_name_file9 = file9.replace(".wmv", "")
new_name_file9 = new_name_file9+ext

if ".mp3" in file10:
    ext = "_.mp3"
    new_name_file10 = file10.replace(".mp3", "")
elif ".mp4" in file10:
    ext = "_.mp4"
    new_name_file10 = file10.replace(".mp4", "")
elif ".wmv" in file10:
    ext = "_.mp4"
    new_name_file10 = file10.replace(".wmv", "")
new_name_file10 = new_name_file10+ext

delornotfile1 = input(f"Do you want {file1} to be deleted after the conversion and compression? (Y/N)\n")
if delornotfile1=="Y":
    code = f"""
    ffmpeg -i "{file1}" "{new_name_file1}"
    del "{file1}"""
elif delornotfile1=="N":
    code = f"""ffmpeg -i "{file1}" "{new_name_file1}"
    """
file = open("Converter and Compressor for file1.bat", "w")
file.write(code)
file.close()
print(f"A batch (.bat) file has been created for {file1}")

delornotfile2 = input(f"Do you want {file2} to be deleted after the conversion and compression? (Y/N)\n")
if delornotfile2=="Y":
    code = f"""
    ffmpeg -i "{file2}" "{new_name_file2}"
    del "{file2}"""
elif delornotfile2=="N":
    code = f"""ffmpeg -i "{file2}" "{new_name_file2}"
    """

file = open("Converter and Compressor for file2.bat", "w")
file.write(code)
file.close()
print(f"A batch (.bat) file has been created for {file2}")

delornotfile3 = input(f"Do you want {file3} to be deleted after the conversion and compression? (Y/N)\n")
if delornotfile3=="Y":
    code = f"""
    ffmpeg -i "{file3}" "{new_name_file3}"
    del "{file3}"""
elif delornotfile3=="N":
    code = f"""ffmpeg -i "{file3}" "{new_name_file3}"
    """

file = open("Converter and Compressor for file3.bat", "w")
file.write(code)
file.close()
print(f"A batch (.bat) file has been created for {file3}")

delornotfile4 = input(f"Do you want {file4} to be deleted after the conversion and compression? (Y/N)\n")
if delornotfile4=="Y":
    code = f"""
    ffmpeg -i "{file4}" "{new_name_file4}"
    del "{file4}"""
elif delornotfile4=="N":
    code = f"""ffmpeg -i "{file4}" "{new_name_file4}"
    """

file = open("Converter and Compressor for file4.bat", "w")
file.write(code)
file.close()
print(f"A batch (.bat) file has been created for {file4}")

delornotfile5 = input(f"Do you want {file5} to be deleted after the conversion and compression? (Y/N)\n")
if delornotfile5=="Y":
    code = f"""
    ffmpeg -i "{file5}" "{new_name_file5}"
    del "{file5}"""
elif delornotfile5=="N":
    code = f"""ffmpeg -i "{file5}" "{new_name_file5}"
    """

file = open("Converter and Compressor for file5.bat", "w")
file.write(code)
file.close()
print(f"A batch (.bat) file has been created for {file5}")

delornotfile6 = input(f"Do you want {file6} to be deleted after the conversion and compression? (Y/N)\n")
if delornotfile6=="Y":
    code = f"""
    ffmpeg -i "{file6}" "{new_name_file6}"
    del "{file6}"""
elif delornotfile6=="N":
    code = f"""ffmpeg -i "{file6}" "{new_name_file6}"
    """

file = open("Converter and Compressor for file6.bat", "w")
file.write(code)
file.close()
print(f"A batch (.bat) file has been created for {file6}")

delornotfile7 = input(f"Do you want {file7} to be deleted after the conversion and compression? (Y/N)\n")
if delornotfile7=="Y":
    code = f"""
    ffmpeg -i "{file7}" "{new_name_file7}"
    del "{file7}"""
elif delornotfile7=="N":
    code = f"""ffmpeg -i "{file7}" "{new_name_file7}"
    """

file = open("Converter and Compressor for file7.bat", "w")
file.write(code)
file.close()
print(f"A batch (.bat) file has been created for {file7}")

delornotfile8 = input(f"Do you want {file8} to be deleted after the conversion and compression? (Y/N)\n")
if delornotfile8=="Y":
    code = f"""
    ffmpeg -i "{file8}" "{new_name_file8}"
    del "{file8}"""
elif delornotfile8=="N":
    code = f"""ffmpeg -i "{file8}" "{new_name_file8}"
    """

file = open("Converter and Compressor for file8.bat", "w")
file.write(code)
file.close()
print(f"A batch (.bat) file has been created for {file8}")

delornotfile9 = input(f"Do you want {file9} to be deleted after the conversion and compression? (Y/N)\n")
if delornotfile9=="Y":
    code = f"""
    ffmpeg -i "{file9}" "{new_name_file9}"
    del "{file9}"""
elif delornotfile9=="N":
    code = f"""ffmpeg -i "{file9}" "{new_name_file9}"
    """

file = open("Converter and Compressor for file9.bat", "w")
file.write(code)
file.close()
print(f"A batch (.bat) file has been created for {file9}")

delornotfile10 = input(f"Do you want {file10} to be deleted after the conversion and compression? (Y/N)\n")
if delornotfile10=="Y":
    code = f"""
    ffmpeg -i "{file10}" "{new_name_file10}"
    del "{file10}"""
elif delornotfile10=="N":
    code = f"""ffmpeg -i "{file10}" "{new_name_file10}"
    """

file = open("Converter and Compressor for file10.bat", "w")
file.write(code)
file.close()
print(f"A batch (.bat) file has been created for {file10}")

os.startfile("Converter and Compressor for file1.bat")
os.startfile("Converter and Compressor for file2.bat")
os.startfile("Converter and Compressor for file3.bat")
os.startfile("Converter and Compressor for file4.bat")
os.startfile("Converter and Compressor for file5.bat")
os.startfile("Converter and Compressor for file6.bat")
os.startfile("Converter and Compressor for file7.bat")
os.startfile("Converter and Compressor for file8.bat")
os.startfile("Converter and Compressor for file9.bat")
os.startfile("Converter and Compressor for file10.bat")


startdeletionprocess = input("When all the files are compressed, then type Y here and press enter to start the deletion process or type N is you don't want this process to be done\n")
if startdeletionprocess=="Y":
    
    if delornotfile1=="N":
        file1size = os.path.getsize(file1)
        new_name_file1_size = os.path.getsize(new_name_file1)
        if file1size>new_name_file1_size:
            os.remove(file1)
        elif file1size<new_name_file1_size:
            os.remove(new_name_file1)
        elif file1size==new_name_file1_size:
            os.remove(new_name_file1)
            
    if delornotfile2=="N":
        file2size = os.path.getsize(file2)
        new_name_file2_size = os.path.getsize(new_name_file2)
        if file2size>new_name_file2_size:
            os.remove(file2)
        elif file2size<new_name_file2_size:
            os.remove(new_name_file2)
        elif file2size==new_name_file2_size:
            os.remove(new_name_file2)

    if delornotfile3=="N":
        file3size = os.path.getsize(file3)
        new_name_file3_size = os.path.getsize(new_name_file3)
        if file3size>new_name_file3_size:
            os.remove(file3)
        elif file3size<new_name_file3_size:
            os.remove(new_name_file3)
        elif file3size==new_name_file3_size:
            os.remove(new_name_file3)
            
    if delornotfile4=="N":
        file4size = os.path.getsize(file4)
        new_name_file4_size = os.path.getsize(new_name_file4)
        if file4size>new_name_file4_size:
            os.remove(file4)
        elif file4size<new_name_file4_size:
            os.remove(new_name_file4)
        elif file4size==new_name_file4_size:
            os.remove(new_name_file4)

    if delornotfile5=="N":
        file5size = os.path.getsize(file5)
        new_name_file5_size = os.path.getsize(new_name_file5)
        if file5size>new_name_file5_size:
            os.remove(file5)
        elif file5size<new_name_file5_size:
            os.remove(new_name_file5)
        elif file5size==new_name_file5_size:
            os.remove(new_name_file5)

    if delornotfile6=="N":
        file6size = os.path.getsize(file6)
        new_name_file6_size = os.path.getsize(new_name_file6)
        if file6size>new_name_file6_size:
            os.remove(file6)
        elif file6size<new_name_file6_size:
            os.remove(new_name_file6)
        elif file6size==new_name_file6_size:
            os.remove(new_name_file6)

    if delornotfile7=="N":
        file7size = os.path.getsize(file7)
        new_name_file7_size = os.path.getsize(new_name_file7)
        if file7size>new_name_file7_size:
            os.remove(file7)
        elif file7size<new_name_file7_size:
            os.remove(new_name_file7)
        elif file7size==new_name_file7_size:
            os.remove(new_name_file7)        

    if delornotfile8=="N":
        file8size = os.path.getsize(file8)
        new_name_file8_size = os.path.getsize(new_name_file8)
        if file8size>new_name_file8_size:
            os.remove(file8)
        elif file8size<new_name_file8_size:
            os.remove(new_name_file8)
        elif file8size==new_name_file8_size:
            os.remove(new_name_file8)

    if delornotfile9=="N":
        file9size = os.path.getsize(file9)
        new_name_file9_size = os.path.getsize(new_name_file9)
        if file9size>new_name_file9_size:
            os.remove(file9)
        elif file9size<new_name_file9_size:
            os.remove(new_name_file9)
        elif file9size==new_name_file9_size:
            os.remove(new_name_file9)

    if delornotfile10=="N":
        file10size = os.path.getsize(file10)
        new_name_file10_size = os.path.getsize(new_name_file10)
        if file10size>new_name_file10_size:
            os.remove(file10)
        elif file10size<new_name_file10_size:
            os.remove(new_name_file10)
        elif file10size==new_name_file10_size:
            os.remove(new_name_file10)
    os.remove("Converter and Compressor for file1.bat")
    os.remove("Converter and Compressor for file2.bat")
    os.remove("Converter and Compressor for file3.bat")
    os.remove("Converter and Compressor for file4.bat")
    os.remove("Converter and Compressor for file5.bat")
    os.remove("Converter and Compressor for file6.bat")
    os.remove("Converter and Compressor for file7.bat")
    os.remove("Converter and Compressor for file8.bat")
    os.remove("Converter and Compressor for file9.bat")
    os.remove("Converter and Compressor for file10.bat")
else:
    os.remove("Converter and Compressor for file1.bat")
    os.remove("Converter and Compressor for file2.bat")
    os.remove("Converter and Compressor for file3.bat")
    os.remove("Converter and Compressor for file4.bat")
    os.remove("Converter and Compressor for file5.bat")
    os.remove("Converter and Compressor for file6.bat")
    os.remove("Converter and Compressor for file7.bat")
    os.remove("Converter and Compressor for file8.bat")
    os.remove("Converter and Compressor for file9.bat")
    os.remove("Converter and Compressor for file10.bat")
    exit()
