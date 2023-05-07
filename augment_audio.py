import os
import math
import random
import numpy as np
from pydub import AudioSegment

def calculate_rms(audio):
    # Convert the audio segment to a numpy array
    audio_array = np.array(audio.get_array_of_samples())

    # Calculate Root Mean Square (RMS) energy of the audio
    rms = math.sqrt(np.mean(audio_array**2))
    return rms

def calculate_noise_rms(audio, target_snr):
    # Calculate the RMS energy of the noise required to achieve the target SNR
    signal_rms = calculate_rms(audio)
    noise_rms = signal_rms / (10 ** (target_snr / 20.0))
    return noise_rms

def add_noise_to_wav_files(directory, noise_file, target_snr):
    # Load the noise audio file
    noise = AudioSegment.from_wav(noise_file)

    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            file_path = os.path.join(directory, filename)
            print(f"Processing file: {file_path}")

            # Load the original audio file
            audio = AudioSegment.from_wav(file_path)

            # Calculate the RMS energy of the noise required for the target SNR
            noise_rms = calculate_noise_rms(audio, target_snr)

            # Adjust the noise audio to match the required RMS energy
            adjusted_noise = noise - (calculate_rms(noise) - noise_rms)

            # Repeat the adjusted noise to match the duration of the original audio
            repeated_noise = adjusted_noise * (len(audio) // len(adjusted_noise) + 1)
            repeated_noise = repeated_noise[:len(audio)]  # Trim excess noise

            # Add the repeated noise to the original audio
            noisy_audio = audio.overlay(repeated_noise)

            # Export the resulting audio with noise
            noisy_file_path = os.path.splitext(file_path)[0] + f"_noisy_{target_snr}dB.wav"
            noisy_audio.export(noisy_file_path, format="wav")

            print(f"Noise added to {filename}. Result saved as {noisy_file_path}\n")

# Provide the directory path containing the .wav files
directory_path = r"C:\Users\oriel\Desktop\audio\Data - Ozen\augmented_files\SNR_10"

# Provide the path to the noise audio file
noise_file_path = "noise_a.wav"

# Provide the target SNR (in decibels) for the augmentation
target_snr = 10

# Call the function to add noise to the .wav files with the specified SNR
add_noise_to_wav_files(directory_path, noise_file_path, target_snr)