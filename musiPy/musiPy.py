"""
musiPy is a simple python code to play along with some music while
having some fun at programming.

created by: Gustavo P. V. Almeida
date: Aug/22/2020
"""

from musicSheet import Note
from musicSheet import Sheet
from scipy.io.wavfile import write
import numpy as np

# set some parameters
wrt = False
plot = False
play = False

# samples per second
f = 440
duration = 4.0
sps = 44100
k = 0.75
k = 0.0015
sheet = Sheet()
sheet.setsamplingrate(sps)
sheet.setdamping(k)
sheet.output_wav_file()
#sheet.player_on()
#sheet.plot()
#sheet.playCDEFG()
#sheet.playSineA440()
#sheet.playAx_b(0.5,1.2)
#sheet.playPhi()


###########################################
# careful with the sections below...
# the writing, plotting and playing were
# written for debugging purposes...

# writing wav file
if wrt:
    write('sound.wav',sps,m1)
    write('sound.wav',sps,m2)
    #write('first_sound.wav',sps,carrier_ints)

# plotting signal waves
if plot:
    plt.plot(carrier)
    for sound in s:
        plt.plot(sound)

    plt.xlim([0,2000])
    plt.show()

# play sound with sounddevice library
if play:
    for sound in s:
        sd.play(sound,sheet._sps)
        sd.wait()

