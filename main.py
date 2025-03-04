# Importing Library
from toolkit import EDAToolkit
import time

print(r"""
 /$$$$$$$$ /$$$$$$$   /$$$$$$       /$$$$$$$$                  /$$ /$$       /$$   /$$    
| $$_____/| $$__  $$ /$$__  $$     |__  $$__/                 | $$| $$      |__/  | $$    
| $$      | $$  \ $$| $$  \ $$        | $$  /$$$$$$   /$$$$$$ | $$| $$   /$$ /$$ /$$$$$$  
| $$$$$   | $$  | $$| $$$$$$$$ /$$$$$$| $$ /$$__  $$ /$$__  $$| $$| $$  /$$/| $$|_  $$_/  
| $$__/   | $$  | $$| $$__  $$|______/| $$| $$  \ $$| $$  \ $$| $$| $$$$$$/ | $$  | $$    
| $$      | $$  | $$| $$  | $$        | $$| $$  | $$| $$  | $$| $$| $$_  $$ | $$  | $$ /$$
| $$$$$$$$| $$$$$$$/| $$  | $$        | $$|  $$$$$$/|  $$$$$$/| $$| $$ \  $$| $$  |  $$$$/
|________/|_______/ |__/  |__/        |__/ \______/  \______/ |__/|__/  \__/|__/   \___/                                              
""")

filePath = input("Enter File Path> ")
print("""
Possible File Types
1> .csv (Comma Seperated Values)
2>  .xslx (Excel)
3> .json (JavaScript Object Notation)
""")
time.sleep(0.5)
fileType = input("Enter File Type> ")

usrCls = EDAToolkit(filePath, fileType)

while(True):
    usrCls.loadData()
    print('''
        1> Check File Path And Type
        2> Inspect Data
        3> Information on Data (Quick)
        4> Measure of Central Tendency
        Q/q> Quit
    ''')

    usrInput = input("> ")
    if usrInput == '1':
        print(f"File Path: {usrCls.filePath}")
        print(f"File Type: {usrCls.fileType}")
    elif usrInput == '2':
        usrCls.peek()
    elif usrInput == '3':
        usrCls.info()
    elif usrInput == '4':
        usrCls.centralTendency()
    elif usrInput == 'Q' or 'q':
        exit()
    else:
        print("Command Not Found")
        exit()