import os
import platform
import datetime
import sys
def system_info_tool(): 
    print("Welcome to System Info Tool") 
    print(f"Operating System name is: {os.name}")   
    print(f"system informatin is: {platform.uname()}") 
    print(f"Python version is: {platform.python_version}")
    print(f"The processor is: {platform.processor}")
    print(f"Current date & time is: {datetime.datetime.now()}")
    print(sys.executable)

