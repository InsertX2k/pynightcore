# `Pynightcore` Python module and `Pynightcore GUI` Project
**A free and an Open-Source Tool for Nightcoring your songs.** <br/>
<br/>
This Github repository contains the source code of the project I told everyone about in the **Amino Nightcore Community**, See [this link](https://aminoapps.com/c/nightcore/page/blog/grettings-from-the-pynightcore-gui-project-by-insertx2k-dev/q5PM_8jtRuVDk88K5DNwV0Gx0YlkkXEPv) <br/>
<br/>
## What does it have/contain? <br/>
It contains the source code of both the **Python** module **'pynightcore'** and the program **'pynightcore GUI'**. <br/>
<br/>
## Download Links? <br/>
Coming soon. <br/>
## Bad `README.md`?, I know it is. <br/>
This `README.md` will remain like this until I complete the development of the project, don't worry, if you want to speed up the process, you can create a '**pull request**' to help provide me with resources, I currently need only the icon file for the program, Which is supposed to be a `64x64` file, don't worry if you can't convert it to an `.ico` file, just pull it here, and I will convert it myself. <br/>
## Credits <br/>
As promised, if you give an icon file for the program, your name will be listed here, and in the `README` file in the installer program. <br/>
**To :** <br/>
**Insertx2k Dev** - for writing the whole code. <br/>
## `pynightcore` Module, Quick Start <br/>
Take a quick look at this example : <br/>

```py
import pynightcore as pync
# Ok, right now, let's nightcore the file 'in.wav' by changing it's speed by 25%
pync.apply_effects("in.wav", "out.wav", 25, 192000)
```
<br/>

**If you don't want to use the `.wav` audio format**, simply download and install `ffmpeg` and you will be running fine. <br/>
## How to compile `pynightcore GUI` <br/>
**You will need :** <br/>
* The **Python** module `pynightcore` <br/>
* The **Python** module `awesometkinter` <br/>
* The **Python** module `pydub` and all of it's '**requirements**' <br/>
* The **Python** module `simpleaudio` <br/>
* **Python 3.x** installed on your computer, and it must be **added to PATH** (Just select the option to **add Python to PATH**), and is configured to work with **Tk/Tcl**. <br/>
* `pyinstaller` or `auto-py-to-exe` if you consider using a **GUI** to compile it. <br/>
Compile it using `pyinstaller` in `windowed` mode, **DO not integrate (add) the source code files into the compiled file.**, also, **don't forget to use the `--hidden-import` option with all of the required modules in order for the program to work.** <br/>
### How to install `pyinstaller` and `auto-py-to-exe` and `pydub` and `simpleaudio` and `awesometkinter` and `pynightcore` ? <br/>
After you have **Python** installed, and **added to PATH**, all what you have to do is just starting a new '**Notepad**' window, and writing all of the following into it. <br/>

```bat
@echo off
cls
title Installing 3rd party dependencies for pync-gui
echo.
echo Please wait, Installing all required 3rd party Python dependencies for compiling Pynightcore GUI.
echo.
echo This shouldn't take so long...
echo.
echo Using Python PIP, if you have wheel installed, this won't work properly.
echo.
pip install pyinstaller
echo Successfully installed pyinstaller
echo.
pip install auto-py-to-exe
echo Successfully installed auto-py-to-exe
echo.
pip install simpleaudio
echo Successfully installed simpleaudio
echo.
pip install pydub
echo Successfully installed pydub
echo.
pip install simpleaudio
echo Successfully installed simpleaudio
echo.
pip install awesometkinter
echo Successfully installed awesometkinter.
echo.
echo All 3rd party dependencies were successfully installed.
echo Press any key to close this window.
pause >nul
exit
```

<br/>

Then, click on File > "Save as..." > Choose in File type as "All files", and save it as `dependency-installer.bat` on your **Desktop** or wherever you wish. <br/>
Then, when it is done saving the file, simply double click on it to run it. <br/>
Once it has started, Please wait for the installation of all of the **3rd party dependencies** to be done. <br/>
Once done, Open the file `pync-gui.py` using a compatible code editor (I recommend using [Visual Studio Code](https://code.visualstudio.com/)), then don't forget to store the file `pynightcore.py` in the same directory the file `pync-gui.py` is in. <br/>
**Here is a simple directory tree giving you an idea of how your directory structure should be looking like :** <br/>

```
pync-gui work
         |
         ____ pync-gui.py
         ____ pynightcore.py

* Both of the files pync.gui.py and pynightcore.py must be in the same directory.
```

<br/>
**OK, after having both of them in the same directory, feel free to debug the source code file, or to compile it into a working `.exe` file** for **Windows-based PCs** <br/>

*More is coming soon.* <br/>
-Insert (or **Mr.X**)
