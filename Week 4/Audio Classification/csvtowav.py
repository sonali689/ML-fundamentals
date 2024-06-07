import wave
import numpy as np
import struct
import sys
import csv
import resampy

def write_wav(data, filename, framerate, amplitude):
    wavfile = wave.open(filename, "w")
    nchannels = 1
    sampwidth = 2
    nframes = len(data)
    comptype = "NONE"
    compname = "not compressed"
    wavfile.setparams((nchannels,
                       sampwidth,
                       framerate,
                       nframes,
                       comptype,
                       compname))
    
    frames = []
    for s in data:
        mul = int(s * amplitude)
        frames.append(struct.pack('h', mul))
    
    frames = b''.join(frames)
    wavfile.writeframes(frames)
    wavfile.close()
    print(f"{filename} written")

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("You must supply a filename to generate")
        exit(-1)
    
    for fname in sys.argv[1:]:
        data = []
        with open(fname, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for time, value in csv_reader:
                try:
                    data.append(float(value))
                except ValueError:
                    pass # Just skip it
        
        print(f"This is data length: {len(data)}")
        arr = np.array(data)
        print(arr)
        
        # Normalize data
        arr /= np.max(np.abs(data))
        print(arr)
        
        filename_head, extension = fname.rsplit(".", 1)
        
        # Resample normalized data to 2000 Hz
        target_samplerate = 3600
        sampled = resampy.resample(arr,sr_orig=3600,sr_new=target_samplerate)
        sampled = np.clip(sampled, -1, 1)

        write_wav(sampled, "wavfile.wav", target_samplerate, 32700)
        print("File written successfully!")
