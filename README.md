# SendToMaya
This is a function for executing Maya python script from commandline or editor like Visual Studio Code.

# Environment
 Python 2.7
 Maya2018

# Installation
## 1. Create a userSetup.py (if you don't have)

Windows: <User>\My Documents\maya\<version>\scripts\userSetup.py
Mac OS X: ~/Library/Preferences/Autodesk/maya/<version>/scripts/userSetup.py 
Linux: ~/maya/<version>/scripts/userSetup.py 

## 2. Add the following in userSetup.py
userSetup.py
```
open port
import maya.cmds as cmds
cmds.commandPort(name="127.0.0.1:7002", stp="python", echoOutput=True)
```
fix encoding bug
```
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
```

# Usage
python SendToMaya.py --file *FILENAME*


# Additional Usage

execute active python file with command in Visual Studio Code
tasks.json
```
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "SendToMaya",
            "type": "shell",
            "command": "Python",
            "args": [<SendToMaya.py full path>,"--file","${file}"]
        }
    ]
}
```
keybindings.json (ctrl+alt+m)
```
[
    {
        "key": "ctrl+alt+m",
        "command": "workbench.action.tasks.runTask",
        "args":"SendToMaya"
    }
]
```
