"""
Pynightcore gui project by Insertx2k Dev

A simple gui for the python module pynightcore made by insertx2k dev for the nightcore community, uses python tkinter (tcl)

Uses as little as possible external python modules, they are just the module pynightcore and python tcl/tk support (py tkinter)

Free to redistribute and modify under the terms of the GNU General Public License v2.0 or later at Free Software Foundation.

You should not call this a Python module.


When exporting this using pyinstaller don't forget to include the modules 'pydub' and 'awesometkinter' and 'simpleaudio' and 'pynightcore' using the '--hidden-import [module-name]' option

If you want to include an icon for the program's window, please be sure to name it 'prog_icon.ico' and place it in the same directory as the program's executable.
"""

# Importing the required tkinter modules
from tkinter import *
# Importing the OS module/library
import os
# Importing the filedialog module from the Python tkinter module
from tkinter import filedialog
# Importing the pynightcore module by Insertx2k Dev.
import pynightcore as pync
# Importing the messagebox tkinter module (Tcl/Tk)
from tkinter import messagebox
# Importing the Python Tk/Tcl Theming Module
from tkinter import ttk
# Importing the AwesomeTkinter Library/Module.
import awesometkinter as atk
# Importing the webbrowser module to hyperlink the twitter.
import webbrowser


# Defining the root window.
root = Tk()
root.title("PyNightcore gui for Windows")

# Defining the root window properties.
# Storing the width and height of the root window into variables.
root_width = 600
root_height = 400
# Determining the real screen width and height.
real_screen_width = root.winfo_screenwidth()
real_screen_height = root.winfo_screenheight()
# Defining the variables of the new root spawn geometry (both the x's and y's).
new_root_spawn_x = (real_screen_width / 2) - (root_width / 2)
new_root_spawn_y = (real_screen_height / 2) - (root_height / 2)
root.geometry(f'{root_width}x{root_height}+{int(new_root_spawn_x)}+{int(new_root_spawn_y)}')
root.config(background=atk.DEFAULT_COLOR)
style_var = ttk.Style()
style_var.theme_use('default')
# The window should never be resizable ok?
root.resizable(False,False)


# Defining the function used to show the user the "?" button beside the .wav file name label.
def show_info():
    messagebox.showinfo("Don't worry", """Don't worry about the .wav output format, as it can be opened by almost all media players in this world, and almost all video editing software that exists in this world.
""")

# Defining the apply effects function (it does include a tkinter and an awesome tkinter window).
def apply_effects_activity():
    # Importing all the required modules/libraries
    import tkinter as tk
    from tkinter import ttk
    import awesometkinter as atk
    # Defining the window telling the user that everything is going to be done.
    progress_root = tk.Tk()
    # Defining the window properties.
    progress_root.title("Applying Nightcore Effects...")
    
    # Defining the real width and height of such tk/tcl window.
    progress_root_width = 400
    progress_root_height = 50
    # Determining the real screen/monitor width and height.
    screen_width = progress_root.winfo_screenwidth()
    screen_height = progress_root.winfo_screenheight()
    # Defining some other variables used as the new spawn geometry of the progress_root.
    new_spawn_x = (screen_width / 2) - (progress_root_width / 2)
    new_spawn_y = (screen_height / 2) - (progress_root_height / 2)
    progress_root.geometry(f'{progress_root_width}x{progress_root_height}+{int(new_spawn_x)}+{int(new_spawn_y)}')
    progress_root.resizable(False,False)
    # Defining the styler of such root (window).
    styler0_var = ttk.Style()
    styler0_var.theme_use('default')
    # Changing the background color of such window.
    progress_root.config(background=atk.DEFAULT_COLOR)
    # Defining some labels inside of such window.
    lbl_0 = Label(progress_root, text="Please wait, nightcoring your song...", fg='white', bg='#333333', font=("Arial Bold", 15))
    lbl_0.place(x=0 ,y=10)
    # Defining the icon of the progress_root, I made it here to prevent people from glitching the runtime core (i.e. the mainloop).
    try:
        progress_root.iconbitmap("prog_icon.ico")
    except:
        print("The icon file 'prog_icon.ico' is either corrupted or doesn't exist in the current program working directory (i.e. path), The window will continue without an icon, but be sure to know that this can cause future exceptions, so please keep that in your mind.")

    # Ok, right now we should obtain all the required information from the user and then make a good nightcore remix out of it.
    # Configuring variables.
    quality_rate_choice = quality_rate_combo.get()
    if quality_rate_choice == "44100 (Lowest Quality)":
        quality_rate_int = 44100
    if quality_rate_choice == "48000 (Good Quality) (Audio DVD Quality)":
        quality_rate_int = 48000
    if quality_rate_choice == "96000 (Very Good Quality) (Low Quality Studio Quality)":
        quality_rate_int = 96000
    if quality_rate_choice == "192000 (The best quality) (Recommended to choose when possible)":
        quality_rate_int = 192000
    
    # Sending the commands to the module 'pynightcore' to apply effects.
    try:
       full_out_file = output_dir_enter.get() + '/' + new_filename_input.get() + '.wav'
       pync.apply_effects(str(input_file_enter.get()), str(full_out_file), int(speed_change_percentage_variable.get()), int(quality_rate_int))
       messagebox.showinfo("Nightcoring is done!", f"Everything is done!, Feel free to listen to the output, it is on {full_out_file}\nHowever, if you are not satisfied with the results, feel free to increase the percentage of speed change, consider going more than 20% for true nightcore effect.")
       progress_root.destroy()
    except:
        messagebox.showerror("An Exception has occured", """An ERROR has occured.
It looks like you did something wrong causing this to happen to the program, but don't worry, nothing has happened to your files, everything is fine.
Consider asking yourself these questions if you really want to help fix this exception:
1-Did you specify a valid file in the 'Enter the file you want to apply effects to'?
2-Did you specify a valid directory in the file 'Enter the output directory'
3-Did you even write any file name in the field 'Enter the output file name'?
4-Did you specify a correct quality rate?.
If yes, you did all this, and you are sure you did all this, and you think there is a problem with this program, feel free to screenshot this messagebox including the program's main window, and start an issue on this program's Github page, and don't forget to include the screenshot.
""")
    # After everything is going to be done, I think it is the time to terminate the program's working activity/window.
    progress_root.destroy()

    # Calling the mainloop of such root
    progress_root.mainloop()

# Defining the browse for wav file function.
def browse_input_file_function():
    input_raw_file_dialog = filedialog.askopenfilename(filetypes = (("WAV Audio Files","*.wav"),("Other Audio Files (Requires FFmpeg, Not recommended)","*.*")))
    final_input_var = input_raw_file_dialog
    input_file_enter.delete(0, END)
    input_file_enter.insert(INSERT, final_input_var)

# Defining the browse for output directory function.
def browser_for_dir_output_function():
    output_dir_choosed = filedialog.askdirectory()
    output_dir_final_result = output_dir_choosed
    output_dir_enter.delete(0, END)
    output_dir_enter.insert(INSERT, output_dir_final_result)

# Defining the call back url function.
def callback(url):
    webbrowser.open_new(url)

# Defining the widgets inside of the tkinter (root) window.
lbl0 = Label(root, text="Pynightcore gui for Windows", fg='yellow', bg='#333333', font=("Arial", 9))
lbl0.grid(column=0, row=1, sticky='w')
lbl1 = Label(root, text="A Simple GUI for nightcoring your songs.", fg='white', bg='#333333', font=("Arial", 10))
lbl1.grid(column=0, row=2, sticky='w')
lbl2 = Label(root, text="Choose the audio file you want to apply nightcore effects to : ", fg='white', bg='#333333', font=("Arial", 10))
lbl2.grid(column=0, row=3, sticky='w')
# Defining the entry widget used to get input from the user.
input_file_enter = ttk.Entry(root, width=90)
input_file_enter.grid(column=0, row=4, sticky='w')
browse_input_file_button = ttk.Button(root, text="...", command=browse_input_file_function)
browse_input_file_button.place(x=547, y=65, relwidth=0.050, relheight=0.047)
# Defining again some labels.
lbl3 = Label(root, text="Choose the output directory : ", fg='white', bg='#333333', font=("Arial", 10))
lbl3.grid(column=0, row=5, sticky='w')
output_dir_enter = ttk.Entry(root, width=90)
output_dir_enter.grid(column=0, row=6, sticky='w')
# Defining the browse output directory button.
browse_output_dir_button = ttk.Button(root, text="...", command=browser_for_dir_output_function)
browse_output_dir_button.place(x=547, y=107, relwidth=0.050, relheight=0.047)
# Defining some additional labels.
lbl4 = Label(root, text="Enter the output file name, It will exported as a wav file:", fg='white', bg='#333333', font=("Arial", 10))
lbl4.grid(column=0, row=7, sticky='w')
# Defining the place where the user must enter the new file name in.
new_filename_input = ttk.Entry(root, width=98)
new_filename_input.grid(column=0, row=8, sticky='w')
# Defining the information button that is showed in the right corner of the button. 
info_show_button = ttk.Button(root, text="!", cursor='hand2', command=show_info)
info_show_button.place(x=330, y=127, relwidth=0.035, relheight=0.045)
# Defining other labels. 
lbl5 = Label(root, text="Enter the percentage to speed up the clip by : (Affects both tempo and pitch)", fg='white', bg='#333333', font=("Arial", 10))
lbl5.grid(column=0, row=9, sticky='w')
# Defining the spinbox variable (of course it is a integer var)
speed_change_percentage_variable = IntVar()
# Defining the default value of the speed_change_percentage_variable to 1 
speed_change_percentage_variable.set(1)
# Defining the spinbox used to describe the speed change percentage.
speed_change_percentage_spin = ttk.Spinbox(root, from_=0, to=1000, width=91, textvariable=speed_change_percentage_variable)
speed_change_percentage_spin.grid(column=0, row=10, sticky='w')
# Defining the "%" label beside the speed change percentage spinbox.
lbl6 = Label(root, text="%", fg='white', bg='#333333', font=("Arial", 12))
lbl6.place(x=570 ,y=186)
# Defining other labels (uhh, again).
lbl7 = Label(root, text="Choose the new Sample/Quality Rate : ", fg='white', bg='#333333', font=("Arial", 10))
lbl7.grid(column=0, row=11, sticky='w')
# Defining the combobox used to define the sample/quality rate of the output file (it is also a wav file).
quality_rate_combo = ttk.Combobox(root, width=96)
quality_rate_combo['values']= ("44100 (Lowest Quality)", "48000 (Good Quality) (Audio DVD Quality)", "96000 (Very Good Quality) (Low Quality Studio Quality)", "192000 (The best quality) (Recommended to choose when possible)")
quality_rate_combo.grid(column=0, row=12, sticky='w')
quality_rate_combo.current(0)
# Defining some other labels.
lbl8 = Label(root, text="Provided to you by Insertx2k Dev, uses the Python module 'pynightcore'.", fg='white', bg='#333333', font=("Arial", 10))
lbl8.grid(column=0, row=13, sticky='w')
lbl9 = Label(root, text="Follow me on : ", fg='white', bg='#333333', font=("Arial", 11))
lbl9.grid(column=0, row=14, sticky='w')
twitter_hyperlink_label = Label(root, text="Twitter : @insertplayztw", fg='lightblue', bg='#333333', font=("Arial Bold", 10), cursor='hand2')
twitter_hyperlink_label.grid(column=0, row=15, sticky='w')
twitter_hyperlink_label.bind("<Button-1>", lambda e: callback("https://twitter.com/insertplayztw"))
# Defining the go button (The button that exports everything).
apply_effects_go_button = atk.Button3d(root, text="Nightcore it!", cursor='hand2', command=apply_effects_activity)
apply_effects_go_button.place(x=245 ,y=330, relwidth=0.2, relheight=0.1)




# Defining the new icon file, I made it here to prevent people from glitching the mainloop (or the runtime core of the program)..
try:
    root.iconbitmap("prog_icon.ico")
except:
    messagebox.showerror("Icon file does not exist", "The icon file 'prog_icon.ico' either doesn't exist or is corrupted, the program will continue without a window icon.")


# Calling the mainloop of the tkinter (root) window.
root.mainloop()