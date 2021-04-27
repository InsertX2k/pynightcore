"""
============================
pynightcore by Insertx2k Dev
============================

A simple Python 3.x module made to help you apply the nightcore effect to your audio files (wav only), and then export it to another audio file (wav too).

You may freely redistribute it under the terms of the GNU General Public License v2.0 or later.

Use it as in the following syntax : 
pynightcore.apply_effects(in_file, out_file, speed_change_percentage, new_sample_rate)

Where : 
in_file - Must be the name and the full path of the file you want to apply the nightcore effects to.
out_file - Must be the full name and the full path of the output file (The final file) which you will hear the nightcore edits in.
speed_change_percentage - Must be the percentage of the speed change you want to apply to the audio file 'in_file', You don't need to write the % to describe this as a percentage, as this module automatically does it for you.
(Pro tip : for a daycore effect, go lower than 0.5)
new_sample_rate - Must be the new sample/quality rate of the file, the higher the value, the better the song output quality (But keep in mind to use common sample rates).

Oh and, about the file type, the 'wav' format can be played by almost all media players in this world, including all video editing software, that's why this python module uses it.

If you need any kind of support, feel free to contact me at Twitter : @insertplayztw, or my Github : insertx2k

It uses little external modules where possible, only the 'pydub' module is what is required.

For the version information, simply write pynightcore.version() or however you loaded it.

"""
# The code of the module continues here...
# Importing all the required modules.
from pydub import AudioSegment
from pydub.playback import play

# Defining the class.

class apply_effects:
    def __init__(self, in_file, out_file, speed_change_percentage, new_sample_rate):
        self.input_file = in_file
        self.output_file = out_file
        self.speed_change_percentage_level = speed_change_percentage
        self.update_sample_rate = new_sample_rate
        # Importing the required files.
        sound = AudioSegment.from_file(self.input_file, format="wav")

        # The variable which the speed changes by (May be manually changed by the user later).
        speed_change_percentage = self.speed_change_percentage_level
        new_sample_rate = int(sound.frame_rate + 100 * speed_change_percentage)

        # Overwriting the .wav output file's frame_rate (Basically changing the clip speed).
        hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        # Now let's change the .wav file's sample rate to what the user has gave to us.
        hipitch_sound = hipitch_sound.set_frame_rate(self.update_sample_rate)
        #export / save pitch changed sound
        hipitch_sound.export(self.output_file, format="wav")

def version():
    print("r0.0.1")

# Defining the function to be executed when this module runs as a Python script.
if __name__ == '__main__':
    print("You are running this as a Python script, you are supposed to run this as a module to work.")