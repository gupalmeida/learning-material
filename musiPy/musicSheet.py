"""
musiPy is a simple python code to play along with some music while
having some fun at programming.

created by: Gustavo P. V. Almeida
date: Aug/22/2020
"""

import numpy as np
import sounddevice as sd
import wave
from scipy.io.wavfile import write
import scitools.sound as snd
import matplotlib.pyplot as plt

class NotesData:
    """ Class with frequency of notes from C0 to C7 in Hz. The data
    is stored into a dictionary for easier access. The members of this
    class are made private in order to be accessed without any change
    of modifying data from outside."""

    def __init__(self):
        # C4 = middle C
        self.__notesData = {
            "c0":16.351,"d0":18.354,"e0":20.601,
            "f0":21.827,"g0":24.499,"a0":27.500,
            "b0":30.868,"c1":32.703,"d1":36.708,
            "e1":41.203,"f1":43.654,"g1":48.999,
            "a1":55.000,"b1":61.735,"c2":65.406,
            "d2":73.416,"e2":80.407,"f2":87.307,
            "g2":97.999,"a2":110.00,"b2":123.47,
            "c3":130.81,"d3":148.83,"e3":164.81,
            "f3":174.61,"g3":198.00,"a3":220.00,
            "b3":246.94,"c4":261.63,"d4":293.88,
            "e4":329.63,"f4":349.23,"g4":391.99,
            "a4":440.00,"b4":493.88,"c5":523.25,
            "d5":587.33,"e5":659.26,"f5":698.46,
            "g5":783.99,"a5":880.00,"b5":987.77,
            "c6":1046.5,"d6":1174.7,"e6":1318.5,
            "f6":1396.9,"g6":1568.0,"a6":1760.0,
            "b6":1975.5,"c7":2093.0
                }

    def getfrequency(self,note):
        """ Returns the frequency of a given note. """
        return self.__notesData.get(note)

class Note(NotesData):
    """ Class with data stored for a given musical note. Data such
    as note frequency (Hz), duration (s) and pitch may be accessed.
    """

    def __init__(self,duration_s,samplingrate):
        super().__init__()
        self.freq_hz = 0.0
        self.duration_s = duration_s
        self._sps = samplingrate
        self.pitch = 1.0

    def setfrequency(self,note):
        self.freq_hz = self.getfrequency(note)

    def getwave(self,damping=0.0):
        t = np.linspace(0,self.duration_s,
                int(self.duration_s*self._sps))
        w = 2 * np.pi * self.freq_hz
        envelope = np.exp(- damping * w * t)
        data = self.pitch * np.sin( w * t) * envelope
        return data

class Sheet:
    """ Class with some interesting music sheets. """

    def __init__(self):
        self._sps = 44100
        self._tempo = 1.0
        self._k = 0.0015
        self.__write_file = False
        self.__plot = False
        self.__play = False

    def setsamplingrate(self,samplingrate):
        self._sps = samplingrate

    def settempo(self,tempo):
        self._tempo = tempo

    def setdamping(self,damping):
        self._k = damping

    def __play_music(self, sheet):
        if self.__play:
            for i in range(sheet.shape[1]):
                sd.play(sheet[:,i])
                sd.wait()
    
    def output_wav_file(self):
        self.__write_file = True

    def plot(self):
        self.__plot = True

    def player_on(self):
        self.__play = True

    def __plot_data(self,data):
        plt.xlim([0,2000])
        if self.__plot:
            plt.plot(data)
            plt.show()

    def __write_wav_file(self,music,fname='sound.wav'):
        if self.__write_file:
            write(fname,self._sps,music)

    def playSineA440(self):
        n = Note(self._tempo,self._sps)
        n.setfrequency('a4')
        n.duration_s = 5.0
        data = n.getwave(0)

        if self.__play:
            sd.play(data)
            sd.wait()
        self.__write_wav_file(data)
        self.__plot_data(data)

    def playCDEFG(self):
        sheet = np.empty(6,dtype=object)
        music = np.empty((self._sps,6),dtype=float)
        data = list()

        # creating notes for the music
        for i in range(sheet.size):
            sheet[i] = Note(self._tempo,self._sps)

        # setting notes duration
        for i in range(sheet.size):
            sheet[i].duration_s = self._tempo

        sheet[0].setfrequency('c4')
        sheet[1].setfrequency('d4')
        sheet[2].setfrequency('e4')
        sheet[3].setfrequency('f4')
        sheet[4].setfrequency('g4')

        for i in range(sheet.size):
            music[:,i] = sheet[i].getwave(self._k)
            data.append(music[:,i])

        data = np.array(data)
        c_data = np.concatenate(data)

        self.__play_music(music)
        self.__write_wav_file(c_data)
        self.__plot_data(music)

    def playAx_b(self,duration=0.2,damp_k=0.75):
        t = np.linspace(0,duration,int(duration*self._sps))
        damp = np.exp(-damp_k * t)
        freqs = np.linspace(0,1,10)
        f = 440 + 220 * freqs
        data = []
        for freq in f:
            sound = damp * np.sin( 2 * np.pi * freq * t)
            data.append(sound)
        data = np.concatenate(data)
        data = np.reshape(data,(data.size,1))
		
        self.__play_music(data)
        self.__write_wav_file(data)
        self.__plot_data(data)

    def playPhi(self,duration=0.2,damp_k=0.75):
        t = np.linspace(0,duration,int(duration*self._sps))
        damp = np.exp(-damp_k * t)
        notes = {
            "c4":261.63,"d4":293.88,
            "e4":329.63,"f4":349.23,"g4":391.99,
            "a4":440.00,"b4":493.88,
            "c5":523.25,"d5":587.33,"e5":659.26
            }
        # fibonacci sequence
        #[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987]
        seq = ['c4','d4','d4','e4','f4','a4','d5','d4','f4',
                'e4','d4','f4','g4','a4','a4','d5','e5',
                'd4','g4','g4','e4','f4','f4','f4',
                'c5','c5','b4','d4','c4']
        data = []
        for n in seq:
            s = Note(0.4,self._sps)
            s.setfrequency(n)
            data.append(s.getwave(0))
        data = np.concatenate(data)
        data = np.reshape(data,(data.size,1))
		
        self.__play_music(data)
        self.__write_wav_file(data)
        self.__plot_data(data)

    def playFactorial(self,duration=0.2,damp_k=0.75):
        t = np.linspace(0,duration,int(duration*self._sps))
        damp = np.exp(-damp_k * t)
        notes = {
            "c4":261.63,"d4":293.88,
            "e4":329.63,"f4":349.23,"g4":391.99,
            "a4":440.00,"b4":493.88,
            "c5":523.25,"d5":587.33,"e5":659.26
            }
        # fibonacci sequence
        #[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987]
        seq = ['c4','d4','d4','e4','f4','a4','d5','d4','f4',
                'e4','d4','f4','g4','a4','a4','d5','e5',
                'd4','g4','g4','e4','f4','f4','f4',
                'c5','c5','b4','d4','c4']
        data = []
        for n in seq:
            s = Note(0.4,self._sps)
            s.setfrequency(n)
            data.append(s.getwave(0))
        data = np.concatenate(data)
        data = np.reshape(data,(data.size,1))
		
        self.__play_music(data)
        self.__write_wav_file(data)
        self.__plot_data(data)

