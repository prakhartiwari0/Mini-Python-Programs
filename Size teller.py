import os

file = input("Enter the name of the file: ")

def convert_bytes(size, unit=None):
    if unit== "Bits":
        return print('File size: ' + str(round(size*8, 3)) + ' bits')
    elif unit == "KB":
        return print('File size: ' + str(round(size / 1024, 3)) + ' Kilobytes')
    elif unit == "MB":
        return print('File size: ' + str(round(size / (1024 * 1024), 3)) + ' Megabytes')
    elif unit == "GB":
        return print('File size: ' + str(round(size / (1024 * 1024 * 1024), 3)) + ' Gigabytes')
    else:
        return print('File size: ' + str(size) + ' bytes')


size = os.stat(file).st_size
rcode = f"""
{convert_bytes(size, "Bits")}
{convert_bytes(size)}
{convert_bytes(size, "KB")}
{convert_bytes(size, "MB")}
{convert_bytes(size, "GB")}
"""
