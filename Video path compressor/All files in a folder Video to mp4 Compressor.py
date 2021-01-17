import os
def main():
    path = input("Enter the full path of the video: ")
    path = path.replace("/", "\\")
    delornot = input("Do you want to delete the original file or not? (y/n): ")
    def full_name():
        p1 = path[::-1]
        if "/" in p1:
            full_name = p1[0:p1.index("/")]
            full_name = full_name[::-1]
        elif "\\" in p1:
            full_name = p1[0:p1.index("\\")]
            full_name = full_name[::-1]
        return full_name

    def name():
        p1 = path[::-1]
        if "/" in p1:
            name = p1[p1.index(".")+1:p1.index("/")]
            name = name[::-1]
        elif "\\" in p1:
            name = p1[p1.index(".")+1:p1.index("\\")]
            name = name[::-1]
        return name

    full_name_ = full_name()
    name = name()
    name_new  = f"{name}_"
    ext = full_name_.replace(name, "")
    new_full_name = full_name_.replace(ext, ".mp4")
    new_full_name = new_full_name.replace(name, name_new)
    new_path = path.replace(full_name_, new_full_name)
    path1 = path.replace("\\", r"\\")
    new_path1 = new_path.replace("\\", r"\\")
    code_for_size_checker_py = rf"""

import os
a = os.stat(r"{path}").st_size
b = os.stat(r"{new_path}").st_size
if a>b:
    file = open("deleting_original_file.bat", "w")
    c = f"del \"{path1}\" \"code_for_size_checker.py\" \"deleting_original_file.bat\""
    file.write(c)
    file.close()
    os.startfile("deleting_original_file.bat")

elif a<b:
    file = open("deleting_compressed_file.bat", "w")
    c = f"del \"{new_path1}\" \"deleting_compressed_file.bat\""
    file.write(c)
    file.close()
    os.startfile("deleting_compressed_file.bat")

"""
    
    if delornot=="y":
        
        file = open("code_for_size_checker.py", "w")
        file.write(code_for_size_checker_py)
        file.close()
        file = open("Compressor.bat", "w")
        code = f"""
        ffmpeg -i "{path}" "{new_path}"
        code_for_size_checker.py
        del "Compressor.bat"
        """
        file.write(code)
        file.close()
        os.startfile("Compressor.bat")
    elif delornot=="n":
        file = open("Compressor.bat", "w")
        code = f"""
                ffmpeg -i "{path}" "{new_path}"
                del "Compressor.bat"
                """
        file.write(code)
        file.close()
        os.startfile("Compressor.bat")

    else:
        print("BADLUCK")
    main()

main()
