#cut mp3 file

import config
from pydub import AudioSegment
import math

def cutMP3(sound_file_name, author_name):
    
    print(sound_file_name)
    mp3_audio = AudioSegment.from_file(author_name+".mp3", format="mp3")

    start = 0.0
    end = len(mp3_audio)

    interval = math.ceil(end/60000)

    len_part = end/interval

    if (end > 60000):
        index = 1
        for i in range(start,end,len_part):

            vid1 = mp3_audio[i:i+len_part]

            vid1.export(author_name+"("+str(index)+").mp3", format = "mp3")

            index = index + 1

