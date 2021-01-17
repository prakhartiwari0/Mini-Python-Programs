# A program that creates a list of details of all the files and directories with their details. Version 1.0 (Will be modified further)
import os
import time


todel = [] 
textforeachfile =str(f""" """) 
list = os.listdir()
list.remove("list maker2.2.py") 
total_size_of_all_files = 0
no_types_cat = [[], [], [], [],[], [] ,[],[], [] , [], [],[]]
# no_types_cat = [["vids0"], ["images1"], ["gifs2"], ["txts3"],["python_files4"], ["html_files5"] ,["pdfs6"],["audios7"], ["zips8"] , ["css9"], ["programs10"],["others11"]]



##global total_size_of_all_files
q = 0
while q<len(list):
    name = str(list[q])
    if "." in name:
        todel.append(name)
        size = os.path.getsize(list[q])
        total_size_of_all_files = total_size_of_all_files+size
        if size<=8:
            size = str(size) + " Bits"
        elif 8<size<1000:
            size = str(size) + " Bytes"
        elif 1000<=size<1000000:
            size = str(size/1000) + " KB" + f" ({size} Bytes)"
        elif 1000000<=size<1000000000:
            size = str(size/1000000) + " MB" + f" ({size} Bytes)"
        elif 1000000000<=size:
            size = str(size/1000000000) + " GB" + f" ({size} Bytes)"
        sizer = f"\nSize           --   {size}"
        tyf = "File"
    if not "." in name:
        sizer = ""
        tyf = "Folder"
    Access_time = str(time.ctime(os.path.getatime(name)))
    Modified_time = str(time.ctime(os.path.getmtime(name)))
    Change_time = str(time.ctime(os.path.getctime(name)))
    name = name.replace(".vpsh", "")
    if tyf=="File":
        name_syntax = f"{tyf} Name      --   {name}{sizer}"
    elif tyf=="Folder":
        name_syntax = f"{tyf} Name    --   {name}{sizer}"
    text = f"""
{q}.
{name_syntax}
Last Accessed  --   {Access_time}
Last Modified  --   {Modified_time}
Last Changed   --   {Change_time}
    """
    textforeachfile = textforeachfile+text
    q = q+1

no_of_files = len(todel)
no_of_folders = (len(list)-len(todel))

if total_size_of_all_files<=8:
    total_storage_occupied = str(total_size_of_all_files) + " Bits"
elif 8<total_size_of_all_files<1000:
    total_storage_occupied = str(total_size_of_all_files) + " Bytes"
elif 1000<=total_size_of_all_files<1000000:
    total_storage_occupied = str(total_size_of_all_files/1000) + " KB" + f" ({total_size_of_all_files} Bytes)"
elif 1000000<=total_size_of_all_files<1000000000:
    total_storage_occupied = str(total_size_of_all_files/1000000) + " MB" + f" ({total_size_of_all_files} Bytes)"
elif 1000000000<=total_size_of_all_files:
    total_storage_occupied = str(total_size_of_all_files/1000000000) + " GB" + f" ({total_size_of_all_files} Bytes)"


last_text = f"""\n-----------------------------------------------
Files {no_of_files}, Folders {no_of_folders}
Total Size of all files - {total_storage_occupied}
"""
textforeachfile = textforeachfile+last_text


##todel.remove("List.txt")
q2 = 0
while q2<len(todel):
    filenamed = str(todel[q2])
    os.remove(filenamed)
    q2 = q2+1

with open("List.txt", 'a', encoding='utf-8') as f:
    f.write(textforeachfile)
    
os.remove("list maker2.2.py")
