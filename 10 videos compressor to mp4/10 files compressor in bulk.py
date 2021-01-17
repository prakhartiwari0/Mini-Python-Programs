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
    new_name_file1 = new_name_file1.replace(".mp4", "")
elif ".wmv" in file1:
    ext = "_.mp4"
    new_name_file1 = new_name_file1.replace(".wmv", "")
new_name_file1 = new_name_file1+ext

if ".mp3" in file2:
    ext = "_.mp3"
    new_name_file2 = file2.replace(".mp3", "")
elif ".mp4" in file2:
    ext = "_.mp4"
    new_name_file2 = new_name_file2.replace(".mp4", "")
elif ".wmv" in file2:
    ext = "_.mp4"
    new_name_file2 = new_name_file2.replace(".wmv", "")
new_name_file2 = new_name_file2+ext

if ".mp3" in file3:
    ext = "_.mp3"
    new_name_file3 = file3.replace(".mp3", "")
elif ".mp4" in file3:
    ext = "_.mp4"
    new_name_file3 = new_name_file3.replace(".mp4", "")
elif ".wmv" in file3:
    ext = "_.mp4"
    new_name_file3 = new_name_file3.replace(".wmv", "")
new_name_file3 = new_name_file3+ext

if ".mp3" in file4:
    ext = "_.mp3"
    new_name_file4 = file4.replace(".mp3", "")
elif ".mp4" in file4:
    ext = "_.mp4"
    new_name_file4 = new_name_file4.replace(".mp4", "")
elif ".wmv" in file4:
    ext = "_.mp4"
    new_name_file4 = new_name_file4.replace(".wmv", "")
new_name_file4 = new_name_file4+ext

if ".mp3" in file5:
    ext = "_.mp3"
    new_name_file5 = file5.replace(".mp3", "")
elif ".mp4" in file5:
    ext = "_.mp4"
    new_name_file5 = new_name_file5.replace(".mp4", "")
elif ".wmv" in file5:
    ext = "_.mp4"
    new_name_file5 = new_name_file5.replace(".wmv", "")
new_name_file5 = new_name_file5+ext

if ".mp3" in file6:
    ext = "_.mp3"
    new_name_file6 = file6.replace(".mp3", "")
elif ".mp4" in file6:
    ext = "_.mp4"
    new_name_file6 = new_name_file6.replace(".mp4", "")
elif ".wmv" in file6:
    ext = "_.mp4"
    new_name_file6 = new_name_file6.replace(".wmv", "")
new_name_file6 = new_name_file6+ext

if ".mp3" in file7:
    ext = "_.mp3"
    new_name_file7 = file7.replace(".mp3", "")
elif ".mp4" in file7:
    ext = "_.mp4"
    new_name_file7 = new_name_file7.replace(".mp4", "")
elif ".wmv" in file7:
    ext = "_.mp4"
    new_name_file7 = new_name_file7.replace(".wmv", "")
new_name_file7 = new_name_file7+ext

if ".mp3" in file8:
    ext = "_.mp3"
    new_name_file8 = file8.replace(".mp3", "")
elif ".mp4" in file8:
    ext = "_.mp4"
    new_name_file8 = new_name_file8.replace(".mp4", "")
elif ".wmv" in file8:
    ext = "_.mp4"
    new_name_file8 = new_name_file8.replace(".wmv", "")
new_name_file8 = new_name_file8+ext

if ".mp3" in file9:
    ext = "_.mp3"
    new_name_file9 = file9.replace(".mp3", "")
elif ".mp4" in file9:
    ext = "_.mp4"
    new_name_file9 = new_name_file9.replace(".mp4", "")
elif ".wmv" in file9:
    ext = "_.mp4"
    new_name_file9 = new_name_file9.replace(".wmv", "")
new_name_file9 = new_name_file9+ext

if ".mp3" in file10:
    ext = "_.mp3"
    new_name_file10 = file10.replace(".mp3", "")
elif ".mp4" in file10:
    ext = "_.mp4"
    new_name_file10 = new_name_file10.replace(".mp4", "")
elif ".wmv" in file10:
    ext = "_.mp4"
    new_name_file10 = new_name_file10.replace(".wmv", "")
new_name_file10 = new_name_file10+ext

delornot = input("Do you want all these files to be deleted after the conversion and compression? (Y/N)\n")


if delornot=="Y":
    code = f"""
    ffmpeg -i "{file1}" "{new_name_file1}"
    del "{file1}"
    ffmpeg -i "{file2}" "{new_name_file2}"
    del "{file2}"
    ffmpeg -i "{file3}" "{new_name_file3}"
    del "{file3}"
    ffmpeg -i "{file4}" "{new_name_file4}"
    del "{file4}"
    ffmpeg -i "{file5}" "{new_name_file5}"
    del "{file5}"
    ffmpeg -i "{file6}" "{new_name_file6}"
    del "{file6}"
    ffmpeg -i "{file7}" "{new_name_file7}"
    del "{file7}"
    ffmpeg -i "{file8}" "{new_name_file8}"
    del "{file8}"
    ffmpeg -i "{file9}" "{new_name_file9}"
    del "{file9}"
    ffmpeg -i "{file10}" "{new_name_file10}"
    del "{file10}"
    """

elif delornot=="N":
    code = f"""
    ffmpeg -i "{file1}" "{new_name_file1}"
    ffmpeg -i "{file2}" "{new_name_file2}"
    ffmpeg -i "{file3}" "{new_name_file3}"
    ffmpeg -i "{file4}" "{new_name_file4}"
    ffmpeg -i "{file5}" "{new_name_file5}"
    ffmpeg -i "{file6}" "{new_name_file6}"
    ffmpeg -i "{file7}" "{new_name_file7}"
    ffmpeg -i "{file8}" "{new_name_file8}"
    ffmpeg -i "{file9}" "{new_name_file9}"
    ffmpeg -i "{file10}" "{new_name_file10}"
    """
file = open("Converter and Compressor.bat", "w")
file.write(code)
file.close()

print("A batch (.bat) file has been created")
