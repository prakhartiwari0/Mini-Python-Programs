import os


# mypath = os.getcwd()
all_files2 = os.listdir()
all_files2.remove("All files in a folder Video to mp4 Compressor.py")

# length = len(all_files2)
i = 0
for b in all_files2:
    prcess_no = i+1
    vfile = open(f"Process_{prcess_no}_done.vbs", "w")
    vcode = f"""
    dim speechobject
    set speechobject=createobject("sapi.spvoice")
    speechobject.speak "Process {prcess_no} done"
    """
    vfile.write(vcode)
    vfile.close()
    tcfile = all_files2[i]
    name_file = tcfile[0:(len(tcfile)-4)]

    compressor_file = open(f"Compressor for {tcfile}.bat", "w")
    code = f"""
    ffmpeg -i "{tcfile}" "_{name_file}.mp4"
    del "{tcfile}"
    Process_{prcess_no}_done.vbs
    del "Process_{prcess_no}_done.vbs"
    del "Compressor for {tcfile}.bat"
    """
    compressor_file.write(code)
    compressor_file.close()
    os.startfile(f"Compressor for {tcfile}.bat")
    
    i = i+1
exit()







