import os
import soundfile as sf
import sys
import matplotlib.pyplot as plt
import numpy as np
import wave

def convert_mp3_to_wav(input_file, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get the output file path
    input_filename = os.path.basename(input_file)
    output_filename = os.path.splitext(input_filename)[0] + ".wav"
    output_path = os.path.join(output_folder, output_filename)
    


    # Read the MP3 file and write it as WAV
    data, sample_rate = sf.read(input_file)
    print("data",data)
    print('\n')
    print('sample_rate',sample_rate)
    sf.write(output_path, data, sample_rate)
    wave_file=output_path
    wav = wave.open(wave_file, "r")
    signal = wav.readframes(-1)
    signal = np.frombuffer(signal, dtype=np.int16)
    sample_rate = wav.getframerate()
    duration = wav.getnframes() / sample_rate
    time = np.linspace(0, duration, len(signal))
    # Plot the waveform
    plt.figure()
    plt.plot(time, signal)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Waveform")
    output_file = output_path+"plot.jpg"
    plt.savefig(output_file)
    wav.close()

    print(f"File converted successfully. Saved as: {output_path}")

# Check if the script is run with the correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python convert.py <input_folder> <output_folder>")
    sys.exit(1)

input_folder = sys.argv[1]
output_folder = sys.argv[2]


# Process all the MP3 files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp3"):
        input_file = os.path.join(input_folder, filename)
        convert_mp3_to_wav(input_file, output_folder)
