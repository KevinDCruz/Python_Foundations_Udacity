import os
import string
def rename_files():
    #1. get file names from the folder
    file_list = os.listdir(r"C:\Users\Kevin D'Cruz\PycharmProjects\Python_Foundations_Udacity\prank")
    print(file_list)
    os.chdir(r"C:\Users\Kevin D'Cruz\PycharmProjects\Python_Foundations_Udacity\prank")
    print(os.getcwd())
    #2. Rename the files
    for file_name in file_list:
        os.rename(file_name, file_name.strip('0123456789'))
rename_files()