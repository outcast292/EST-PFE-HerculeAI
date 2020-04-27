import ctypes
import sys
import subprocess
import sys
import os
import requests

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # Code of your program here
    os.system('cmd /c "pip install virtualenv"')
    print("creating virtual environement")
    os.system('cmd /c "python -m venv herculeai_env"')
    print("installing dependencies")
    os.system('cmd /c"herculeai_env\Scripts\\activate.bat && pip install -r .\\requirements.txt && python .\\downloader.py "')
    print("DONE!!!!")

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
